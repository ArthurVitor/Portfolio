from django.shortcuts import render, redirect
from .models import *
from .forms import *


# Create your views here.
def index(request):
    return render(request, 'portfolio_templates/index.html')


def projects(request):
    mod = ProjectsModel.objects.all()
    cont = mod.count()
    return render(request, 'portfolio_templates/projetos.html', context={'mod': mod})


def detailed_project(request, id):
    objects = ProjectsModel.objects.filter(pk=id)
    context = {'obj': objects}
    return render(request, 'portfolio_templates/detailed_project.html', context=context)



################## Deprecated #################
# def projects_form(request):
#     form = ProjectsForm(request.POST or None)
#
#     if form.is_valid():
#         form.save()
#         return redirect('projects')
#     else:
#         form = ProjectsForm(request.POST or None)
#     return render(request, 'portfolio_templates/detailed_project.html', context={'form': form})
