from django.shortcuts import render


# Create your views here.
def about(request):
    return render(request, 'about/index.html')


def info(request):
    return render(request, 'about/info.html')


def resume(request):
    return render(request, 'about/resume.html')
