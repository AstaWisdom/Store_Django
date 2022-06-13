from django.shortcuts import render, redirect
from .forms import UserForm, SpecialBuyForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth import login, authenticate
from .models import UserDashboard
from django.shortcuts import HttpResponse
# Create your views here.


def register(request):
    user_dashboard_id = request.session.get('ref_invite')
    if request.method != 'POST':
        user_form = UserForm()
    else:
        user_form = UserForm(data=request.POST)
        if user_form.is_valid():
            if user_dashboard_id is not None:
                recomended_by_user = UserDashboard.objects.get(id=user_dashboard_id)
                user_form.save(commit=False)
                username = user_form.cleaned_data.get('username')
                email = user_form.cleaned_data.get('email')
                password1 = user_form.cleaned_data.get('password1')
                trading_link = user_form.cleaned_data.get('trading_link')
                user = User.objects.create_user(username=username, password=password1, email=email)
                UserDashboard(name=username, trading_link=trading_link, user=user, invited_users=recomended_by_user.user).save()

                login(request, user)
                return redirect('Thoth_Gaming.urls:homepage')

            else:
                user_form.save(commit=False)
                username = user_form.cleaned_data.get('username')
                email = user_form.cleaned_data.get('email')
                password1 = user_form.cleaned_data.get('password1')
                trading_link = user_form.cleaned_data.get('trading_link')
                user = User.objects.create_user(username=username, password=password1, email=email)
                UserDashboard(name=username, trading_link=trading_link, user=user).save()
                login(request, user)
                return redirect('Thoth_Gaming.urls:homepage')

    context = {'user_form': user_form}
    return render(request, 'users/register.html', context)



@login_required()
def user_dashboard(request, user_id):
    url = request.get_full_path_info().split("/")
    user_dashboard = UserDashboard.objects.get(id=user_id)
    for i in url:
        if i == str(request.user.userdashboard.id):
            if request.method == 'POST':
                email = request.POST['email']
                trade_link = request.POST['trade_link']
                first_name = request.POST['first_name']
                last_name = request.POST['last_name']
                user_dashboard.trading_link = trade_link
                user_dashboard.user.email = email
                user_dashboard.user.first_name = first_name
                user_dashboard.user.last_name = last_name
                user_dashboard.save()
                user_dashboard.user.save()
            context = {'user_dashboard': user_dashboard}
            return render(request, 'users/user_dashboard.html', context)
        else:
            pass
    return res_404(request)


def res_404(request):
    return HttpResponse('<h1 style="margin-left:625px;margin-top:100px">Page Is not Accessible</h1>')


def ref_code(request, ref_code):
    try:
        user_dashboard = UserDashboard.objects.get(invite_link=ref_code)
        request.session['ref_invite'] = user_dashboard.id
    except:
        res_404(request)

    return redirect('Thoth_Gaming.urls:users.urls:register')


def special_order(request):
    if request.method == 'GET':
        buy_form = SpecialBuyForm()
    else:
        buy_form = SpecialBuyForm(request.POST)
        buy_form.save()
        _complete(request)
    context = {'buy_form': buy_form}
    return render(request, 'users/special_order.html', context)


def _complete(request):
    return HttpResponse('<h1 style="margin-left:625px;margin-top:100px">Your Request Has Been Sent</h1>')