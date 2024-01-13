package com.example.newapp;

import android.content.Intent;
import android.net.Uri;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;

import androidx.appcompat.app.AppCompatActivity;

public class HealActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_heal);

        // 첫 번째 버튼에 대한 클릭 이벤트 처리
        Button btnChest = findViewById(R.id.btn_chest);
        btnChest.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                openYouTubeVideo("https://youtu.be/toXIw6HvQvU?si=4I1kZTyu_QuF90Rf");
            }
        });

        // 두 번째 버튼에 대한 클릭 이벤트 처리
        Button btnBack = findViewById(R.id.btn_back);
        btnBack.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                openYouTubeVideo("https://youtu.be/YHZSd5H6ppY?si=_mrWfmQMzOAz57tF");
            }
        });

        // 세 번째 버튼에 대한 클릭 이벤트 처리
        Button btnLeg = findViewById(R.id.btn_leg);
        btnLeg.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                openYouTubeVideo("https://youtu.be/6yKIke-VY7Q?si=gD1pgJFX6X1fanxa");
            }
        });
    }

    // 유튜브 비디오 링크로 이동하는 메서드
    private void openYouTubeVideo(String videoUrl) {
        Intent intent = new Intent(Intent.ACTION_VIEW, Uri.parse(videoUrl));
        startActivity(intent);
    }
}
