from django.shortcuts import render


def home(req):

    context = {}
    template = 'home.html'

    return render(req, template, context)