from django.shortcuts import render, redirect
from django.views.generic.edit import FormView
from .forms import RegisterForm, LoginForm
from .models import Fcuser
from django.contrib.auth.hashers import make_password
# Create your views here.


def index(request):
    return render(request, 'index.html', {'email': request.session.get('user')})


class RegisterView(FormView):
    template_name = 'register.html'
    form_class = RegisterForm
    success_url = '/'

    # clean이 끝나고 호출되는 함수

    def form_valid(self, form):
        fcuser = Fcuser(
            email=form.data.get('email'),
            password=make_password(form.data.get('password')),
            level='user'
        )
        fcuser.save()
        return super().form_valid(form)


class LoginView(FormView):
    template_name = 'login.html'
    form_class = LoginForm
    success_url = '/'

    # 모든 것이 정상일 때 들어가는 예약 함수
    def form_valid(self, form):
        self.request.session['user'] = form.data.get('email')

        return super().form_valid(form)


def logout(request):
    if 'user' in request.session:
        del(request.session['user'])

    return redirect('/')
