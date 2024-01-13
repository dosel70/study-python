package com.example.newapp;

import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.RadioButton;
import android.widget.TextView;
import androidx.appcompat.app.AppCompatActivity;

public class WeightActivity extends AppCompatActivity {
    private EditText editTextHeight;
    private EditText editTextWeight;
    private RadioButton radioButtonMale;
    private TextView textViewResult;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_weight);

        editTextHeight = findViewById(R.id.editTextHeight);
        editTextWeight = findViewById(R.id.editTextWeight);
        radioButtonMale = findViewById(R.id.radioButtonMale);
        textViewResult = findViewById(R.id.textViewResult);

        Button buttonCalculate = findViewById(R.id.buttonCalculate);
        buttonCalculate.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                calculatePIBW();
            }
        });
    }

    private void calculatePIBW() {
        // 여기에서 PIBW를 계산하고 체중 범주를 결정하는 로직을 추가하세요.
        // 사용자의 키, 몸무게, 성별을 가져와 계산을 수행합니다.
        // 계산 결과를 textViewResult에 표시하세요.

        // 예시: 계산 결과를 문자열로 설정
        String resultText = "결과: 여기에 계산 결과 표시";

        // 계산 결과 표시
        textViewResult.setText(resultText);
    }
}
