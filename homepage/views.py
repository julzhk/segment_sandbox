from django.shortcuts import render


def home(request):




    a=1+2+4

    #  some things
    #  that should be
    #  reformatted!

    print(
        1 + 2 + 4 +
        4 + 45 + 444 * 888 * 88
        *222
        *3

    );

    return render(request=request, template_name="homepage/home.html")
