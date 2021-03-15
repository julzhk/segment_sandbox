from django.shortcuts import render


def home(request):

    a = 1 + 2 + 4
    return render(request=request, template_name="homepage/home.html")
