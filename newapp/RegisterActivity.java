package com.example.newapp;

import android.annotation.SuppressLint;
import android.content.Context;
import android.content.SharedPreferences;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.Toast;

import androidx.appcompat.app.AppCompatActivity;

import com.example.newapp.model.UserData;
import com.google.firebase.auth.FirebaseAuth;
import com.google.firebase.database.DatabaseReference;
import com.google.firebase.database.FirebaseDatabase;

/**
 * 회원가입 화면
 */
public class RegisterActivity extends AppCompatActivity {

    private EditText etName;
    private EditText etEmail;
    private EditText etPassword;
    private Button btnRegister;

    private FirebaseAuth mAuth;
    private DatabaseReference mDatabaseRef;

    @SuppressLint("WrongViewCast")
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_register);

        // firebase auth 초기화
        mAuth = FirebaseAuth.getInstance();
        // firebase realtime db 초기화
        mDatabaseRef = FirebaseDatabase.getInstance().getReference();

        etName = findViewById(R.id.et_name);
        etEmail = findViewById(R.id.et_email1);
        etPassword = findViewById(R.id.et_password1);
        btnRegister = findViewById(R.id.btn_register1);

        btnRegister.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                // 사용자 입력을 가져옴
                String name = etName.getText().toString();
                String email = etEmail.getText().toString();
                String password = etPassword.getText().toString();

                // 입력 검증: 모든 필드가 비어 있지 않아야 함
                if (name.isEmpty() || email.isEmpty() || password.isEmpty()) {
                    // 경고 메시지 표시
                    Toast.makeText(RegisterActivity.this, "정보를 기입해주세요!", Toast.LENGTH_SHORT).show();
                    return;
                }
                // 모든 필드가 입력되면 회원 정보를 저장하고 LoginActivity로 이동
                saveUserInfo(email, password, name);
            }
        });
    }

    private void saveUserInfo(String email, String password, String name) {
        mAuth.createUserWithEmailAndPassword(email, password)
                .addOnCompleteListener(this, task -> {
                    if (task.isSuccessful()) {
                        // 회원가입 성공
                        Log.d("SignUp", "createUserWithEmail:success");
                        Toast.makeText(RegisterActivity.this, "회원가입 성공", Toast.LENGTH_SHORT).show();

                        // 유저 모델 객체 인스턴스 생성
                        UserData userData = new UserData();
                        userData.setEmail(email);
                        userData.setName(name);
                        // 최초 가입시엔 프로필 관련 정보들은 임의의 값을 넣어둔다.
                        userData.setProfileUrl("nothing");
                        userData.setPhone("nothing");
                        userData.setAddress("nothing");
                        userData.setAge(999);
                        // insert user data to firebase db
                        mDatabaseRef.child("user_info").child(task.getResult().getUser().getUid()).setValue(userData);

                        finish();
                    } else {
                        // 회원가입 실패
                        Log.w("SignUp", "createUserWithEmail:failure", task.getException());
                        Toast.makeText(RegisterActivity.this, "회원가입 실패", Toast.LENGTH_SHORT).show();
                    }
                });
    }
}
