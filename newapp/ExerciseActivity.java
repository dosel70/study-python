package com.example.newapp;

import androidx.appcompat.app.AppCompatActivity;
import androidx.appcompat.widget.Toolbar;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;

public class ExerciseActivity extends AppCompatActivity {
    Button btn_exercise1, btn_exercise2;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_exercise);

        Toolbar toolbar = findViewById(R.id.toolBar);
        setSupportActionBar(toolbar);

        btn_exercise1 = findViewById(R.id.btn_exercise1);
        btn_exercise2 = findViewById(R.id.btn_exercise2);

        btn_exercise1.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Intent intent = new Intent(ExerciseActivity.this,SecondExerciseActivity.class);
                startActivity(intent);
            }
        });

        btn_exercise2.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Intent intent = new Intent(ExerciseActivity.this,SecondExerciseActivity.class);
                startActivity(intent);
            }
        });

    }
    public void beforeage18(View view) {
        Intent intent = new Intent(ExerciseActivity.this, SecondExerciseActivity.class);
        startActivity(intent);
    }

    public void afterage18(View view) {
        Intent intent = new Intent(ExerciseActivity.this, SecondExerciseActivity.class);
        startActivity(intent);
    }

    public void otherexercise(View view) {
        Intent intent = new Intent(ExerciseActivity.this, OtherExerciseActivity.class);
        startActivity(intent);

    }

}