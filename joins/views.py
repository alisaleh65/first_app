from django.shortcuts import render
from .forms import EmailForm, JoinForm
from .models import Join


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
        new_join.save()

    context = {'form': form}
    template = 'home.html'

    return render(request, template, context)
