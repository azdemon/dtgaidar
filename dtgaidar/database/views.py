from django.shortcuts import render
from .models import Base


def base(request):
    base = Base.objects.all()
    return render(request, 'database/base.html', {'base':base})
