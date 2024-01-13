package com.example.newapp;

import androidx.annotation.NonNull;
import androidx.annotation.Nullable;
import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.content.SharedPreferences;
import android.net.Uri;
import android.os.Bundle;
import android.provider.MediaStore;
import android.util.Log;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.ImageView;
import android.widget.TextView;
import android.widget.Toast;

import com.bumptech.glide.Glide;
import com.example.newapp.model.UserData;
import com.google.android.gms.tasks.OnCompleteListener;
import com.google.android.gms.tasks.OnFailureListener;
import com.google.android.gms.tasks.OnSuccessListener;
import com.google.android.gms.tasks.Task;
import com.google.firebase.auth.FirebaseAuth;
import com.google.firebase.database.DataSnapshot;
import com.google.firebase.database.DatabaseError;
import com.google.firebase.database.DatabaseReference;
import com.google.firebase.database.FirebaseDatabase;
import com.google.firebase.database.ValueEventListener;
import com.google.firebase.storage.FirebaseStorage;
import com.google.firebase.storage.StorageReference;
import com.google.firebase.storage.UploadTask;

import java.io.File;

public class ProfileActivity extends AppCompatActivity {
    private static final int PICK_IMAGE = 100;
    private ImageView profileImageView;
    private TextView tv_name, tv_email;
    private Button btnPhoto, btnComplete;
    private EditText phoneNumberEditText, addressEditText, ageEditText;
    private FirebaseAuth mAuth;
    private StorageReference storageRef;
    private DatabaseReference mDatabaseRef;
    private Uri selectedImageUri;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_profile);

        tv_name = findViewById(R.id.tv_name);
        tv_email = findViewById(R.id.tv_email);
        btnComplete = findViewById(R.id.btn_complete);
        profileImageView = findViewById(R.id.profile);
        btnPhoto = findViewById(R.id.btn_photo);
        phoneNumberEditText = findViewById(R.id.phone);
        addressEditText = findViewById(R.id.home);
        ageEditText = findViewById(R.id.agree1);

        // firebase 관련
        mAuth = FirebaseAuth.getInstance(); // 계정 고유값인 uid를 가져오기 위해 초기화
        FirebaseStorage storage = FirebaseStorage.getInstance(); // 이미지 저장, 로드 처리를 하기 위해 초기화
        storageRef = storage.getReference(); // 이미지 저장, 로드 처리를 하기 위해 초기화
        mDatabaseRef = FirebaseDatabase.getInstance().getReference(); // 프로필 유저정보를 db에 저장하기 위해 초기화

        // 최종 프로필 저장 데이터 로드
        getLastProfileData();

        btnPhoto.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                changeProfileImage();
            }
        });

        btnComplete.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                // 회원 정보를 SharedPreferences에 저장
                SharedPreferences sharedPreferences = getSharedPreferences("user_info", MODE_PRIVATE);
                SharedPreferences.Editor editor = sharedPreferences.edit();
                editor.putString("address", addressEditText.getText().toString());
                editor.putString("phone", phoneNumberEditText.getText().toString());
                editor.putInt("age", Integer.parseInt(ageEditText.getText().toString()));
                editor.apply();

                mDatabaseRef.child("user_info").child(mAuth.getCurrentUser().getUid()).child("address").setValue(addressEditText.getText().toString());
                mDatabaseRef.child("user_info").child(mAuth.getCurrentUser().getUid()).child("phone").setValue(phoneNumberEditText.getText().toString());
                mDatabaseRef.child("user_info").child(mAuth.getCurrentUser().getUid()).child("age").setValue(Integer.parseInt(ageEditText.getText().toString()));

                Toast.makeText(ProfileActivity.this, "프로필 정보가 업데이트 되었습니다", Toast.LENGTH_SHORT).show();
            }
        });
    }

    private void getLastProfileData() {
        // 최종적으로 저장되어있던 프로핊 데이터들을 모두 로드 해온다
        mDatabaseRef.child("user_info").child(mAuth.getCurrentUser().getUid()).addListenerForSingleValueEvent(new ValueEventListener() {
            @Override
            public void onDataChange(@NonNull DataSnapshot snapshot) {
                UserData userData = snapshot.getValue(UserData.class);
                tv_name.setText(userData.getName());
                tv_email.setText(userData.getEmail());

                if (!userData.getAddress().equals("nothing"))
                    addressEditText.setText(userData.getAddress());
                if (!userData.getPhone().equals("nothing"))
                    phoneNumberEditText.setText(userData.getPhone());
                if (userData.getAge() != 999)
                    ageEditText.setText(String.valueOf(userData.getAge()));

                if (!userData.getProfileUrl().equals("nothing")) {
                    Glide.with(ProfileActivity.this)
                            .load(userData.getProfileUrl())
                            .circleCrop()
                            .into(profileImageView);
                }
            }

            @Override
            public void onCancelled(@NonNull DatabaseError error) {
                Log.e("firebase db error", error.getMessage());
            }
        });
    }

    public void uploadProfileImage() {
        if (selectedImageUri != null) {
            String uid = mAuth.getCurrentUser().getUid();
            StorageReference profileImageRef = storageRef.child("profile" + File.separator + uid + ".png");

            profileImageRef.putFile(selectedImageUri)
                    .addOnCompleteListener(this, task -> {
                        if (task.isSuccessful()) {
                            // 이미지 업로드 성공

                            // 프로필 이미지 다운로드 url 추출
                            getDownloadUrl(profileImageRef);
                        } else {
                            // 이미지 업로드 실패
                            Log.w("UploadImage", "uploadProfileImage:failure", task.getException());
                            Toast.makeText(ProfileActivity.this, "프로필 이미지 업로드 실패", Toast.LENGTH_SHORT).show();
                        }
                    });

        } else {
            Toast.makeText(this, "이미지를 선택해주세요.", Toast.LENGTH_SHORT).show();
        }
    }

    // 업로드 후에 이미지의 다운로드 URL을 가져오기 위한 메서드
    private void getDownloadUrl(StorageReference storageReference) {
        storageReference.getDownloadUrl()
                .addOnSuccessListener(uri -> {
                    // 성공적으로 다운로드 URL을 얻은 경우
                    String downloadUrl = uri.toString();

                    // 추출한 이미지 url을 firebase user db update
                    mDatabaseRef.child("user_info").child(mAuth.getCurrentUser().getUid()).child("profileUrl").setValue(downloadUrl);

                    // 정보를 저장했음을 알리는 메시지를 사용자에게 표시
                    Toast.makeText(ProfileActivity.this, "프로필 이미지 정보를 업데이트 하였습니다!", Toast.LENGTH_SHORT).show();
                    finish();

                    Log.d("DownloadUrl", "Image download URL: " + downloadUrl);
                })
                .addOnFailureListener(new OnFailureListener() {
                    @Override
                    public void onFailure(Exception exception) {
                        // 다운로드 URL을 가져오는 데 실패한 경우
                        Log.w("DownloadUrl", "Error getting download URL", exception);
                    }
                });
    }

    public void changeProfileImage() {
        Intent intent = new Intent(Intent.ACTION_PICK, MediaStore.Images.Media.EXTERNAL_CONTENT_URI);
        startActivityForResult(intent, PICK_IMAGE);
    }

    @Override
    protected void onActivityResult(int requestCode, int resultCode, @Nullable Intent data) {
        super.onActivityResult(requestCode, resultCode, data);

        if (requestCode == PICK_IMAGE && resultCode == RESULT_OK && data != null && data.getData() != null) {
            selectedImageUri = data.getData();
            Glide.with(ProfileActivity.this)
                    .load(selectedImageUri)
                    .circleCrop()
                    .into(profileImageView);

            // firebase storage & firebase database 업데이트
            uploadProfileImage();
        }
    }

    // 이미지 선택과 관련된 코드는 이전 답변에서 이미 제공되었으므로 중복되는 내용은 생략합니다.
}