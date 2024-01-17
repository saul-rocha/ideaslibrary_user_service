from django.shortcuts import get_object_or_404, redirect
from django.db.models import F
from django.contrib.auth.decorators import login_required


@login_required(login_url='login')
def avaliacao(request):
    pass
