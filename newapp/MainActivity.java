package com.example.newapp;

import androidx.appcompat.app.AppCompatActivity;
import android.net.Uri;
import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.ImageButton;
import android.widget.ImageView;
import android.widget.TextView;

public class MainActivity extends AppCompatActivity {

    private ImageButton iv_exercise;
    private ImageButton foodeat;
    private ImageButton calender1;
    private ImageView iv_Profile;
    private EditText editTextText;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);


        editTextText = findViewById(R.id.editTextText);


        // 이미지 버튼 초기화
        ImageView ivSetting = findViewById(R.id.iv_setting);
        iv_exercise = findViewById(R.id.iv_exercise);
        foodeat = findViewById(R.id.foodeat);
        iv_Profile = findViewById(R.id.iv_profile);
        calender1 = findViewById(R.id.calender1);
        ImageView ivCafe = findViewById(R.id.iv_cafe);
        TextView tv_name = findViewById(R.id.tv_name);

        // 로그인 한 닉네임 헤더 텍스트에 불러오기
        Intent intent = getIntent();
        if (intent.getExtras() != null) {
            tv_name.setText(intent.getStringExtra("name") + "님 안녕하세요");
        }



        // iv_exercise 이미지 버튼 클릭 리스너
        iv_exercise.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                // ExerciseActivity로 이동하는 Intent 생성
                Intent intent = new Intent(MainActivity.this, ExerciseActivity.class);
                startActivity(intent);
            }
        });
       foodeat.setOnClickListener(new View.OnClickListener() {
           @Override
           public void onClick(View v) {
               Intent intent = new Intent(MainActivity.this, MainActivity2.class);
               startActivity(intent);
           }
       });
       ivCafe.setOnClickListener(new View.OnClickListener() {
           @Override
           public void onClick(View v) {
               String youtubeUrl = "https://cafe.naver.com/black6yiib";
               Uri uri = Uri.parse(youtubeUrl);
               Intent intent = new Intent(Intent.ACTION_VIEW, uri);

               startActivity(intent);
           }
       });

        ivSetting.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                String communityUrl = "https://youtu.be/NcgQje8m0Y0";
                Uri uri = Uri.parse(communityUrl);
                Intent intent = new Intent(Intent.ACTION_VIEW, uri);

                startActivity(intent);
            }
        });

       calender1.setOnClickListener(new View.OnClickListener() {
           @Override
           public void onClick(View v) {
               Intent intent = new Intent(MainActivity.this, CalenderActivity.class);
               startActivity(intent);
           }
       });

       iv_Profile.setOnClickListener(new View.OnClickListener() {
           @Override
           public void onClick(View v) {
               Intent intent = new Intent(MainActivity.this, ProfileActivity.class);
               startActivity(intent);
           }
       });

    }




    private void saveAndOpenCalendar() {
        String exerciseText = editTextText.getText().toString().trim();
        if (!exerciseText.isEmpty()) {
            Intent intent = new Intent(this, CalenderActivity.class);
            intent.putExtra("exerciseText", exerciseText);
            startActivity(intent);
        }
    }
}