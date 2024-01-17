from django.shortcuts import redirect
from django.shortcuts import get_object_or_404


from django.contrib.auth.decorators import login_required


@login_required(login_url='login')
def comentario(request):
    return redirect('/')
