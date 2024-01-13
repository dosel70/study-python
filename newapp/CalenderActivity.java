package com.example.newapp;

import androidx.annotation.NonNull;
import androidx.appcompat.app.AppCompatActivity;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.widget.ArrayAdapter;
import android.widget.Button;
import android.widget.CalendarView;
import android.widget.EditText;
import android.widget.ListView;
import android.widget.TextView;
import android.widget.Toast;

import com.example.newapp.model.ExerciseHistory;
import com.example.newapp.model.UserData;
import com.google.firebase.auth.FirebaseAuth;
import com.google.firebase.database.DataSnapshot;
import com.google.firebase.database.DatabaseError;
import com.google.firebase.database.DatabaseReference;
import com.google.firebase.database.FirebaseDatabase;
import com.google.firebase.database.ValueEventListener;

import java.text.SimpleDateFormat;
import java.util.ArrayList;
import java.util.Locale;

public class CalenderActivity extends AppCompatActivity {
    private CalendarView calendarView;
    private EditText editTextEvent;
    private Button buttonSave;

    private TextView textViewSavedEvent;
    private ArrayList<ExerciseHistory> mLstExerciseHistory; // 운동 기록 배열 객체
    private ArrayList<String> mLstContent; // 리스트 뷰에 content 만 뿌리면 되서 별도 문자열 배열 객체 선언

    private ArrayAdapter<String> mAdapter; // 리스트 뷰에 실제적으로 연동된 어댑터이며 , refresh 도 이 객체로 함

    private DatabaseReference mDatabaseRef; // firebase db
    private String mCurrentSelectedDate; // 현재 선택 되어진 일시

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_calender);

        calendarView = findViewById(R.id.calendarView);
        editTextEvent = findViewById(R.id.editTextEvent);
        buttonSave = findViewById(R.id.buttonSave);
        textViewSavedEvent = findViewById(R.id.textViewSavedEvent);


        // array list 객체 초기화
        mLstContent = new ArrayList<>();
        mLstExerciseHistory = new ArrayList<>();

        // 운동 기록 보여줄 리스트 뷰 초기화
        ListView lvExercise = findViewById(R.id.lv_exercise);
        // 어댑터 초기화
        mAdapter = new ArrayAdapter<>(this, android.R.layout.simple_list_item_1, mLstContent);

        // ListView에 Adapter 설정
        lvExercise.setAdapter(mAdapter);

        String todayDateStr = new SimpleDateFormat("yyyy-MM-dd").format(System.currentTimeMillis());
        mCurrentSelectedDate = todayDateStr;
        // 선택한 날짜를 TextView에 표시
        textViewSavedEvent.setText("선택한 날짜: " + todayDateStr);

        // firebase db 조회 - uid 고유값을 활용하여 로그인된 계정의 운동 기록 가져오기
        mDatabaseRef = FirebaseDatabase.getInstance().getReference();
        mDatabaseRef.child("exercise_history").orderByChild("uid").equalTo(FirebaseAuth.getInstance().getUid()).addListenerForSingleValueEvent(new ValueEventListener() {
            @Override
            public void onDataChange(@NonNull DataSnapshot snapshot) {
                if (snapshot.getChildrenCount() != 0) {
                    for (DataSnapshot childSnapshot : snapshot.getChildren()) {
                        ExerciseHistory exerciseHistory = childSnapshot.getValue(ExerciseHistory.class);
                        mLstExerciseHistory.add(exerciseHistory);

                        if (todayDateStr.equals(exerciseHistory.getExerciseDate())) {
                            mLstContent.add(exerciseHistory.getContent());
                        }
                    }
                    textViewSavedEvent.setText("선택한 날짜: " + todayDateStr);
                    mAdapter.notifyDataSetChanged();
                }
            }

            @Override
            public void onCancelled(@NonNull DatabaseError error) {
                Log.e("firebase db error", error.getMessage());
            }
        });

        // CalendarView에서 선택한 날짜 이벤트 처리
        calendarView.setOnDateChangeListener(new CalendarView.OnDateChangeListener() {
            @Override
            public void onSelectedDayChange(CalendarView view, int year, int month, int dayOfMonth) {
                // 여기에서 선택한 날짜를 사용하여 기록된 이벤트를 표시하거나 기록할 수 있습니다.
                String selectedDate = year + "-" + String.format(Locale.KOREA, "%02d", (month + 1)) + "-" + String.format(Locale.KOREA, "%02d", dayOfMonth);
                if (!mLstContent.isEmpty()) {
                    mLstContent.clear();
                }

                // firebase database 에서 가져온 내 운동 기록들 중 선택된 date string 에 해당하는 일자 비교
                for (ExerciseHistory exerciseHistory : mLstExerciseHistory) {
                    if (exerciseHistory.getExerciseDate().equals(selectedDate)) {
                        mLstContent.add(exerciseHistory.getContent());
                    }
                }

                // refresh listview
                mAdapter.notifyDataSetChanged();

                // update current selected date
                mCurrentSelectedDate = selectedDate;

                // 선택한 날짜를 TextView에 표시
                textViewSavedEvent.setText("선택한 날짜: " + selectedDate);

            }
        });

        // "저장" 버튼 클릭 이벤트 처리
        buttonSave.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                String event = editTextEvent.getText().toString();
                if (event.isEmpty()) {
                    Toast.makeText(CalenderActivity.this, "이벤트를 입력하세요", Toast.LENGTH_SHORT).show();
                    return;
                }

                // 운동 기록 객체 인스턴스 생성
                ExerciseHistory exerciseHistory = new ExerciseHistory();
                exerciseHistory.setUid(FirebaseAuth.getInstance().getUid());
                exerciseHistory.setExerciseDate(mCurrentSelectedDate);
                exerciseHistory.setContent(event);

                // update exercise history to firebase db
                mDatabaseRef.child("exercise_history").push().setValue(exerciseHistory);

                // refresh listview
                mLstExerciseHistory.add(exerciseHistory);
                mLstContent.add(exerciseHistory.getContent());
                mAdapter.notifyDataSetChanged();
                Toast.makeText(CalenderActivity.this, "이벤트가 저장 되었습니다", Toast.LENGTH_SHORT).show();
            }
        });
    }
}
