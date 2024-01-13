package com.example.newapp;

import androidx.appcompat.app.AppCompatActivity;

import android.annotation.SuppressLint;
import android.content.Intent;
import android.os.Bundle;
import android.os.CountDownTimer;
import android.view.View;
import android.widget.Button;
import android.widget.TextView;

public class ThridExerciseActivity extends AppCompatActivity {

    String buttonvalue;
    Button StartBtn;
    private CountDownTimer countDownTimer;
    TextView mtextview;
    private boolean MTimeRunning;
    private long MTimeLeftinmills;

    @SuppressLint("MissingInflatedId")
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_thrid_exercise);

        Intent intent = getIntent();
        buttonvalue = intent.getStringExtra("value");

        int intvalue = Integer.valueOf(buttonvalue);

        switch (intvalue) {

            case 1:
                setContentView(R.layout.activity_pose1);
                break;
            case 2:
                setContentView(R.layout.activity_pose2);
                break;
            case 3:
                setContentView(R.layout.activity_pose3);
                break;
            case 4:
                setContentView(R.layout.activity_pose4);
                break;
            case 5:
                setContentView(R.layout.activity_pose5);
                break;
            case 6:
                setContentView(R.layout.activity_pose6);
                break;
            case 7:
                setContentView(R.layout.activity_pose7);
                break;
            case 8:
                setContentView(R.layout.activity_pose8);
                break;
            case 9:
                setContentView(R.layout.activity_pose10);
                break;
            case 10:
                setContentView(R.layout.activity_pose11);
                break;
            case 11:
                setContentView(R.layout.activity_pose12);
                break;
            case 12:
                setContentView(R.layout.activity_pose13);
                break;
        }
        StartBtn = findViewById(R.id.startbutton);
        mtextview = findViewById(R.id.time);

        StartBtn.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                if (MTimeRunning)

                {
                    stoptimer();



                }

                else {

                    starttimer();


                }
            }
        });



    }

    private void stoptimer()
    {
        countDownTimer.cancel();
        MTimeRunning = false;
        StartBtn.setText("START");
    }

    private void starttimer()
    {
        final CharSequence value1 = mtextview.getText();
        String num1 = value1.toString();
        String num2 = num1.substring(0,2);
        String num3 = num1.substring(3,5);

        final int number = Integer.valueOf(num2) * 60 + Integer.valueOf(num3);
        MTimeLeftinmills = number*1000;

        countDownTimer = new CountDownTimer(MTimeLeftinmills,1000) {
            @Override
            public void onTick(long millisUntilFinished) {

                MTimeLeftinmills = millisUntilFinished;
                updateTimer();

            }

            @Override
            public void onFinish() {

                int newvalue = Integer.valueOf(buttonvalue) + 1;
                if (newvalue<=7) {
                    Intent intent = new Intent(ThridExerciseActivity.this,ThridExerciseActivity.class);
                    intent.addFlags(Intent.FLAG_ACTIVITY_CLEAR_TASK);
                    intent.putExtra("value",String.valueOf(newvalue));
                    startActivity(intent);
                }
                else {
                    newvalue =1;
                    Intent intent = new Intent(ThridExerciseActivity.this, ThridExerciseActivity.class);
                    intent.addFlags(Intent.FLAG_ACTIVITY_CLEAR_TASK);
                    intent.putExtra("value",String.valueOf(newvalue));
                    startActivity(intent);
                }

            }
        }.start();
        StartBtn.setText("Pause");
        MTimeRunning=true;
    }

    private void updateTimer() {
        int minutes = (int) MTimeLeftinmills/60000;
        int seconds = (int) MTimeLeftinmills%60000 /1000;

        String timeLeftText="";
        if(minutes<10)
            timeLeftText ="0" ;
        timeLeftText = timeLeftText+minutes+":";
        if (seconds<10)
            timeLeftText+="0";
        timeLeftText+=seconds;
        mtextview.setText(timeLeftText);
    }

    @Override
    public void onBackPressed() {
        super.onBackPressed();
    }
}
