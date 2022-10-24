from django.shortcuts import render


def Fitnessgraph(request):
    return render(request, 'blog/Fitnessgraph.html', {})
