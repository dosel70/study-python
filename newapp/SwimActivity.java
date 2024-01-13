package com.example.newapp;

import androidx.appcompat.app.AppCompatActivity;
import androidx.appcompat.widget.Toolbar;

import android.content.Intent;
import android.os.Bundle;
import android.util.Log;
import android.view.View;

public class SwimActivity extends AppCompatActivity {
    int[] newArray;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_swim);

        Toolbar toolbar = findViewById(R.id.oolBar);
        setSupportActionBar(toolbar);

        newArray = new int[]{
                R.id.boat_seoul, R.id.boat_kyungki, R.id.boat_incheon, R.id.boat_kb, R.id.boat_kn, R.id.boat_cb, R.id.boat_cn, R.id.boat_jb, R.id.boat_jn
        };
    }

    public void Imagebuttoncliked(View view) {
        for(int i = 0; i < newArray.length; i++) {

            if(view.getId() == newArray[i]) {
                int value = i+1;
                Log.i("FIRST" , String.valueOf(value));
                Intent intent = new Intent(SwimActivity.this, Swim1.class);
                intent.putExtra("value",String.valueOf(value));
                startActivity(intent);
            }
        }
    }
}