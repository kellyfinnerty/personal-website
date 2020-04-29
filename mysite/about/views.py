from django.shortcuts import render
from projects.models import Project


# Create your views here.
def about(request):
    projects = Project.objects.filter(current=True)
    context = {'projects': projects}
    return render(request, 'about/index.html', context)


def info(request):
    return render(request, 'about/info.html')


def resume(request):
    return render(request, 'about/resume.html')
