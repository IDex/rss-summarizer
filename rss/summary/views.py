from django.shortcuts import render


def main(request):
    context = dict()
    return render(request, 'summary/dash.html', context)
