package com.example.newapp;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;

public class MainActivity2 extends AppCompatActivity {
    Button btnDiet, btnMuscle, btnPound;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main2);

        btnDiet = findViewById(R.id.btn_diet);
        btnMuscle = findViewById(R.id.btn_muscle);
        btnPound = findViewById(R.id.btn_weight);



        btnDiet.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Intent intent = new Intent(MainActivity2.this, DietActivity.class);
                startActivity(intent);
            }
        });
        btnMuscle.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Intent intent = new Intent(MainActivity2.this, MuscleActivity.class);
                startActivity(intent);
            }
        });
        btnPound.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Intent intent = new Intent(MainActivity2.this, PoundActivity.class);
                startActivity(intent);
            }
        });


    }
}