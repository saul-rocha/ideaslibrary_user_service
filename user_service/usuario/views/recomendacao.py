from django.shortcuts import render
from ..models import Profile
from django.contrib.auth.models import User
import requests
from django.contrib.auth.decorators import login_required


@login_required(login_url='login')
def recomendacao(request, post_id):
    url_da_api = f"http://127.0.0.1:8001/posts/{post_id}/"
    resposta = requests.get(url_da_api)

    if resposta.status_code == 200:
        post = resposta.json()
    else:
        post = None

    return render(request, 'recomendacao.html', {'post': post})


@login_required(login_url='login')
def recomendacoes(request):
    url_da_api = "http://127.0.0.1:8001/posts/"

    resposta = requests.get(url_da_api)

    if resposta.status_code == 200:
        posts = resposta.json()
    else:
        posts = []

    return render(request, 'recomendacoes.html', {'posts': posts})
