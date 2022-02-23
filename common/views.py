from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from common.forms import UserForm


def signup(request):
    """
    계정생성
    """
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')  # 사용자 이름 추출
            raw_password = form.cleaned_data.get('password1')  # 비밀번호 추출
            user = authenticate(username=username, password=raw_password)  # 사용자 인증
            login(request, user)  # 로그인
            return redirect('/pybo/')
    else:
        form = UserForm()
    return render(request, 'common/signup.html', {'form': form})
