import uuid

from django.shortcuts import render, HttpResponseRedirect

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


def get_ref_id():

    ref_id = str(uuid.uuid4())[:11].replace('-', '').lower()

    try:
        id_exists = Join.objects.get(ref_id=ref_id)
        return get_ref_id()
    except:
        return ref_id


def share(request, ref_id):
    # print("ref Id is ", ref_id)
    context = {'ref_id': ref_id}
    template = "share.html"
    return render(request, template, context)


def home(request):
    try:
        ref_id = request.session['join_id_ref']
        obj = Join.objects.get(id=ref_id)
    except:
        ref_id = None
        obj = None
    # print(obj, " is the id.")
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
        # new_join = form.save(commit=False)
        # we might do something.
        email = form.cleaned_data['email']
        new_join_old, created = Join.objects.get_or_create(email=email)
        if created:
            new_join_old.ref_id = get_ref_id()
            new_join_old.ip_address = get_ip(request)
            new_join_old.save()

        return HttpResponseRedirect("/%s" % new_join_old.ref_id)

    context = {'form': form}
    template = 'home.html'

    return render(request, template, context)
