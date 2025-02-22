from django import forms
from django.contrib.auth.hashers import check_password
from .models import Fcuser


class RegisterForm(forms.Form):
    email = forms.EmailField(
        error_messages={
            'required': '이메일을 입력해주세요'
        },
        max_length=64,
        label='이메일'
    )
    password = forms.CharField(
        error_messages={
            'required': '비밀번호를 입력해주세요'
        },
        widget=forms.PasswordInput,
        label='비밀번호'
    )
    re_password = forms.CharField(
        error_messages={
            'required': '비밀번호를 한번 더 입력해주세요'
        },
        widget=forms.PasswordInput,
        label='비밀번호 확인'
    )

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get('email')
        password = cleaned_data.get('password')
        re_password = cleaned_data.get('re_password')

        if password and re_password:
            if password != re_password:
                self.add_error('password', '비밀번호가 서로 다릅니다.')
                self.add_error('re_password', '비밀번호가 서로 다릅니다.')


class LoginForm(forms.Form):
    email = forms.CharField(max_length=32, label="사용자 이름", error_messages={
        'required': '아이디를 입력해 주세요'}, help_text="32자 이내로 입력해주세요.")
    password = forms.CharField(widget=forms.PasswordInput, label="비밀번호", error_messages={
                               'required': '비밀번호를 입력해 주세요'}, help_text="길이 무제한")

    def clean(self):  # is_valid를 호출하면 자동으로 호출됨.
        cleaned_data = super().clean()
        email = cleaned_data.get('email')
        password = cleaned_data.get('password')

        if email and password:
            try:
                fcuser = Fcuser.objects.get(email=email)
            except Fcuser.DoesNotExist:
                self.add_error('email', '아이디가 없습니다.')
                return

            if not check_password(password, fcuser.password):
                # password.errors에 자동으로 들어감.
                self.add_error('password', '비밀번호가 틀렸습니다.')
