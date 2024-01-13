package com.example.newapp;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.RadioButton;
import android.widget.TextView;

public class PoundActivity extends AppCompatActivity {

    private EditText editTextHeight;
    private EditText editTextWeight;
    private RadioButton radioButtonMale;
    private TextView textViewResult;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_pound);

        editTextHeight = findViewById(R.id.editTextHeight);
        editTextWeight = findViewById(R.id.editTextWeight);
        radioButtonMale = findViewById(R.id.radioButtonMale);
        textViewResult = findViewById(R.id.textViewResult);

        Button buttonCalculate = findViewById(R.id.buttonCalculate);
        buttonCalculate.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                calculateBMI();
            }
        });
    }

    private void calculateBMI() {
        // 입력값을 가져옴
        String heightStr = editTextHeight.getText().toString();
        String weightStr = editTextWeight.getText().toString();

        if (heightStr.isEmpty() || weightStr.isEmpty()) {
            textViewResult.setText("키와 몸무게를 모두 입력하세요.");
            return;
        }

        // 문자열로 입력된 키와 몸무게를 숫자로 변환
        double height = Double.parseDouble(heightStr) / 100; // cm를 m로 변환
        double weight = Double.parseDouble(weightStr);

        // BMI 계산
        double bmi = weight / (height * height);

        // 결과 출력
        String result;
        if (bmi < 18.5) {
            result = "저체중";
        } else if (bmi >= 18.5 && bmi < 23) {
            result = "정상";
        } else if (bmi >= 23 && bmi < 25) {
            result = "과체중";
        } else {
            result = "비만";
        }

        if (radioButtonMale.isChecked()) {
            result = "남성 " + result;
        } else {
            result = "여성 " + result;
        }

        textViewResult.setText("BMI: " + String.format("%.2f", bmi) + "\n" + result);
    }
}