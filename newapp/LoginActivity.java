package com.example.newapp;

import androidx.annotation.NonNull;
import androidx.appcompat.app.AppCompatActivity;

import android.content.Context;
import android.content.Intent;
import android.content.SharedPreferences;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.widget.Button;
import android.widget.CheckBox;
import android.widget.EditText;
import android.widget.Toast;

import com.example.newapp.model.UserData;
import com.google.android.gms.tasks.OnCompleteListener;
import com.google.android.gms.tasks.Task;
import com.google.firebase.auth.AuthResult;
import com.google.firebase.auth.FirebaseAuth;
import com.google.firebase.database.DataSnapshot;
import com.google.firebase.database.DatabaseError;
import com.google.firebase.database.DatabaseReference;
import com.google.firebase.database.FirebaseDatabase;
import com.google.firebase.database.ValueEventListener;

import org.json.JSONException;
import org.json.JSONObject;

/**
 * 로그인 화면
 */
public class LoginActivity extends AppCompatActivity {

    private EditText et_id, et_pass;
    private Button btn_login, btn_register;
    private CheckBox chkRemeberLogin;
    private FirebaseAuth mAuth;
    private DatabaseReference mDatabaseRef;
    private UserData loginUserData; // 로그인에 성공한 유저 정보

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_login);

        mAuth = FirebaseAuth.getInstance();
        mDatabaseRef = FirebaseDatabase.getInstance().getReference();

        et_id = findViewById(R.id.et_id);
        et_pass = findViewById(R.id.et_pass);
        btn_login = findViewById(R.id.btn_login);
        btn_register = findViewById(R.id.btn_register);
        chkRemeberLogin = findViewById(R.id.chk_remeber_login);

        // 이전에 로그인 정보 저장한 적 있다면 불러오기
        SharedPreferences sharedPref = getSharedPreferences("user_info", Context.MODE_PRIVATE);
        et_id.setText(sharedPref.getString("email", ""));
        et_pass.setText(sharedPref.getString("password", ""));
        chkRemeberLogin.setChecked(sharedPref.getBoolean("isSaveLoginInfo", false));

        btn_register.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                startActivity(new Intent(LoginActivity.this,RegisterActivity.class));
            }
        });

        btn_login.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                String email = et_id.getText().toString();
                String password = et_pass.getText().toString();

                // 유효성 검사 입력필드 empty 체크
                if (email.isEmpty() || password.isEmpty()) {
                    Toast.makeText(LoginActivity.this, "입력필드가 비어있습니다", Toast.LENGTH_SHORT).show();
                    return;
                }

                // firebase auth request login
                mAuth.signInWithEmailAndPassword(email, password)
                        .addOnCompleteListener(LoginActivity.this, (OnCompleteListener<AuthResult>) task -> {
                            if (task.isSuccessful()) {
                                // 로그인 성공
                                Log.d("SignIn", "signInWithEmail:success");

                                mDatabaseRef.child("user_info").child(task.getResult().getUser().getUid()).addListenerForSingleValueEvent(new ValueEventListener() {
                                    @Override
                                    public void onDataChange(@NonNull DataSnapshot snapshot) {
                                        loginUserData = snapshot.getValue(UserData.class);

                                        SharedPreferences sharedPref = getSharedPreferences("user_info", Context.MODE_PRIVATE);
                                        SharedPreferences.Editor editor = sharedPref.edit();
                                        if (chkRemeberLogin.isChecked()) {
                                            // 로그인 정보 저장 옵션이 켜져 있는 경우
                                            // 기타 용도로 쓰일 수 있기에 내부 디비로 SharedPreferences를 사용하여 사용자 정보 저장

                                            editor.putString("email", email);
                                            editor.putString("password", password);
                                            editor.putString("name", loginUserData.getName());
                                            editor.putString("address", loginUserData.getAddress());
                                            editor.putString("phone", loginUserData.getPhone());
                                            editor.putInt("age", loginUserData.getAge());
                                            editor.putBoolean("isSaveLoginInfo", true);
                                            editor.apply();
                                        } else {
                                            editor.clear();
                                        }

                                        Toast.makeText(LoginActivity.this, "로그인 성공", Toast.LENGTH_SHORT).show();
                                        Intent intent = new Intent(LoginActivity.this, MainActivity.class);
                                        intent.putExtra("name", loginUserData.getName());
                                        startActivity(intent);
                                        finish();
                                    }

                                    @Override
                                    public void onCancelled(@NonNull DatabaseError error) {
                                        Log.e("firebase db error", error.getMessage());
                                    }
                                });

                            } else {
                                // 로그인 실패
                                Log.w("SignIn", "signInWithEmail:failure", task.getException());
                                Toast.makeText(LoginActivity.this, "로그인 실패", Toast.LENGTH_SHORT).show();
                            }
                        });

            }
        });


    }
}