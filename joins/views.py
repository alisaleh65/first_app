from django.shortcuts import render
from .forms import EmailForm, JoinForm
from .models import Join


def get_ip(req):
    try:
        x_forward = req.META.get("HTTP_X_FORWARDED_FOR")
        if x_forward:
            ip = x_forward.split(",")[0]
        else:
            ip = req.META.get('REMOTE_ADDR')

    except:

        ip = ""

    return ip


def home(request):
    #
    # form = EmailForm(request.POST or None)
    # if form.is_valid():
    #
    #     email = form.cleaned_data['email']
    #     new_join, created = Join.objects.get_or_create(email=email)
    #     print("ok email :) ", new_join, created)
    #
    #     if created:
    #         print("this email was created")

    form = JoinForm(request.POST or None)

    if form.is_valid():
        new_join = form.save(commit=False)
        # we might do something.
        new_join.ip_address = get_ip(request)
        new_join.save()

    context = {'form': form}
    template = 'home.html'

    return render(request, template, context)
