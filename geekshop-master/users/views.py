from django.shortcuts import render, HttpResponseRedirect
from users.forms import UserLoginForm, UserRegistrationForm, UserProfileForm
from django.contrib import auth, messages
from django.urls import reverse
from baskets.models import Basket 

from django.contrib.auth.decorators import login_required

def login (request):
    # это обрабатывается POST
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid(): # если данные в форме валидны (а данные тут - кусок html кода)
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password) # результат прохождения аутентификации
            if user and user.is_active:
                auth.login(request, user) # авторизоваться этим пользователем
                return HttpResponseRedirect(reverse('index')) # перенаправить на главную
        # else:
            # print(form.errors)    # это мы вывели ошибки валидации формы    
    else:
        form = UserLoginForm()
    # Это обрабатывается GET запрос
    context = {
        'title': 'Авторизация в GeekShop',
        'form': form,
    }
    return render(request, 'users/login.html', context)

def registration(request):
    if request.method == 'POST':
        form=UserRegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            # создадим сообщение
            messages.success(request, 'Вы успешно зарегистрировались! Введите ваш аватар в личном кабинете ;)') 
            # теперь это сообщение стало доступно из шаблона
            return HttpResponseRedirect(reverse('users:login'))
        # else:
            # print(form.errors) # это мы вывели ошибки валидации формы
    else:
        form = UserRegistrationForm()

    context= {
        'title': 'GeekShop - Регистрация',
        'form': form,
    }
    return render(request,'users/register.html', context)

def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('index'))

@login_required
def profile(request):
    if request.method == 'POST':
        form = UserProfileForm(instance = request.user, data = request.POST, files= request.FILES) # сказали что менять будем у этого пользователя, что пришел в запросе и работать с приложенным в запросе файлом (аватаром).
        if form.is_valid(): 
            form.save()
            messages.success(request, 'Изменения успешно сохранены!')
            return HttpResponseRedirect(reverse('users:profile'))
    else:
        form = UserProfileForm(instance=request.user) # передали текущего пользователя дял отображания его «ТТХ»
    
    context = {
        'title': 'Профиль пользователя',
        'form': form,
#        'backets': Basket.objects.all(), # тут написано с опечаткой
        'baskets': Basket.objects.filter(user=request.user), 
        # этот фильтр, чтобы выводились только по заданному пользователю.
        # исправлена опечатка в baskets…

    }
    return render(request, 'users/profile.html', context)
