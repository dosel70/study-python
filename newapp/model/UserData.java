package com.example.newapp.model;

/**
 * firebase db에서 관리하는 유저 데이터 모델 객체
 */
public class UserData {
    private String name; // 성함
    private String email; // 이메일 주소 (로그인 아이디)
    private String profileUrl; // 프로필 이미지 url (from firebase storage)
    private String phone; // 휴대폰 번호
    private String address; // 주소
    private int age; // 나이

    public UserData() { }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }

    public String getProfileUrl() {
        return profileUrl;
    }

    public void setProfileUrl(String profileUrl) {
        this.profileUrl = profileUrl;
    }

    public String getPhone() {
        return phone;
    }

    public void setPhone(String phone) {
        this.phone = phone;
    }

    public String getAddress() {
        return address;
    }

    public void setAddress(String address) {
        this.address = address;
    }

    public int getAge() {
        return age;
    }

    public void setAge(int age) {
        this.age = age;
    }
}
