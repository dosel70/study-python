package com.example.newapp;

import androidx.appcompat.app.AppCompatActivity;
import androidx.appcompat.widget.Toolbar;

import android.content.Intent;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.widget.ImageButton;

public class OtherExerciseActivity extends AppCompatActivity {


    int[] newArray;


    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_other_exercise);

        // swimming 아이디를 가진 LinearLayout에 대한 클릭 이벤트 등록
        findViewById(R.id.swimming).setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                // 클릭 시 실행할 동작
                startActivity(new Intent(OtherExerciseActivity.this, SwimActivity.class));
            }
        });

        // hiking 아이디를 가진 LinearLayout에 대한 클릭 이벤트 등록
        findViewById(R.id.hiking).setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                // 클릭 시 실행할 동작
                startActivity(new Intent(OtherExerciseActivity.this, HikeActivity.class));
            }
        });

        // health 아이디를 가진 LinearLayout에 대한 클릭 이벤트 등록
        findViewById(R.id.health).setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                // 클릭 시 실행할 동작
                startActivity(new Intent(OtherExerciseActivity.this, HealActivity.class));
            }
        });




        Toolbar toolbar = findViewById(R.id.toolBar);
        setSupportActionBar(toolbar);

        newArray = new int[]{

                R.id.other1,R.id.other2,R.id.other3,R.id.other4
        };

    }


    public void Imagebuttoncliked(View view) {
        for(int i = 0; i< newArray.length; i++) {

            if (view.getId() == newArray[i]) {
                int value = i+1;
                Log.i("FIRST", String.valueOf(value));
                Intent intent = new Intent(OtherExerciseActivity.this, Third1.class);
                intent.putExtra("value",String.valueOf(value));
                startActivity(intent);

            }
        }

    }
}