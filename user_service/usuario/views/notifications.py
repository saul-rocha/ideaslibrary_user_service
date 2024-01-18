from django.shortcuts import render
from ..models import Profile
from django.contrib.auth.models import User
import requests
from django.contrib.auth.decorators import login_required


@login_required(login_url='login')
def notifications(request):
    url_da_api = "http://43.202.46.173:8000/notifications/"
    # Ou a forma como você obtém o nome do usuário logado
    username = request.user.username

    resposta = requests.get(url_da_api)

    if resposta.status_code == 200:
        todas_notificacoes = resposta.json()
        notifications = [
            notif for notif in todas_notificacoes if notif['receiver'] == username]
    else:
        notifications = []
    
    return render(request, 'notifications.html', {'notifications': notifications})
