package com.example.newapp.model;

/**
 * 운동 or 식단 모델 클래스
 */
public class ExerciseHistory {
    private String uid; // firebase uid
    private String content; // 온둥 또는 식단 데이터 입력 내용
    private String exerciseDate; // yyyy-MM-dd 형식의 date string

    public ExerciseHistory() { }

    public String getUid() {
        return uid;
    }

    public void setUid(String uid) {
        this.uid = uid;
    }

    public String getContent() {
        return content;
    }

    public void setContent(String content) {
        this.content = content;
    }

    public String getExerciseDate() {
        return exerciseDate;
    }

    public void setExerciseDate(String exerciseDate) {
        this.exerciseDate = exerciseDate;
    }
}
