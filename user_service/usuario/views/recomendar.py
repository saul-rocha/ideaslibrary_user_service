from django.shortcuts import render, redirect

from django.contrib.auth.decorators import login_required
import requests
from django.urls import reverse
from ..models import Follower


@login_required(login_url='login')
def recomendar(request):

    if request.method == 'POST':

        if request.FILES.get('image_upload') == None:
            image = 'https://i.imgur.com/2ZtU6O2.png'
        else:
            image = request.FILES.get('image_upload')

        user = request.user.username
        livro = request.POST.get('livro')
        review = request.POST.get('review')
        link = request.POST.get('link')

        url_da_api = "http://3.8.2.21:8000/posts/"
        dados = {
            "username": user,
            "nm_livro": livro,
            "review": review,
            "link": link
        }
        files = {"image": image}

        resposta = requests.post(url_da_api, data=dados, files=files)

        # Obtém os seguidores do usuário que fez a postagem e notifica
        followers = Follower.objects.filter(user=user)
        followers = followers.values_list('follower', flat=True)
        message = f'{user} fez uma nova postagem: "{livro}"'
        for follower in followers:
            noti_data = {"username_ator": user,
                         "receiver": follower, "message": message}
            notifica = requests.post(
                "http://43.201.147.97:8000/notifications/", data=noti_data)
            if notifica.status_code != 201:
                print("Erro ao notificar seguidor.")

        if resposta.status_code == 201:
            # Certifique-se de que 'recomendacoes' é um nome de url válido em seu urls.py
            return redirect(reverse('recomendacoes'))
        else:
            # Caso a resposta não seja 201, você pode querer adicionar lógica adicional aqui, como mostrar uma mensagem de erro
            return render(request, 'recomendar.html', {'erro': 'Erro ao criar post.'})

    else:
        return render(request, 'recomendar.html')
