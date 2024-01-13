package com.example.newapp;

import androidx.appcompat.app.AppCompatActivity;

import android.annotation.SuppressLint;
import android.content.Intent;
import android.os.Bundle;
import android.os.CountDownTimer;
import android.view.View;
import android.widget.Button;
import android.widget.TextView;

public class Swim1 extends AppCompatActivity {

    String buttonvalue;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_swim1);
        Intent intent = getIntent();
        buttonvalue = intent.getStringExtra("value");

        int intvalue = Integer.valueOf(buttonvalue);

        switch (intvalue) {

            case 1:
                setContentView(R.layout.activity_swim01);
                break;
            case 2:
                setContentView(R.layout.activity_swim02);
                break;
            case 3:
                setContentView(R.layout.activity_swim03);
                break;
            case 4:
                setContentView(R.layout.activity_swim04);
                break;
            case 5:
                setContentView(R.layout.activity_swim04);
                break;
            case 6:
                setContentView(R.layout.activity_swim05);
                break;
            case 7:
                setContentView(R.layout.activity_swim05);
                break;
            case 8:
                setContentView(R.layout.activity_swim06);
                break;
            case 9:
                setContentView(R.layout.activity_swim06);
                break;

        }
    }
}