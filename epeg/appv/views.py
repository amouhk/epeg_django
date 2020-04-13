import pprint

from django.http import Http404
from django.shortcuts import render
from django.core.mail import send_mail


from appv.models import Gallery
from appv.models import Predication
from .forms import ContactForm


def home(request):
    sermon_latest = Predication.objects.order_by('date').reverse()[0]
    return render(request, 'appv/index.html', locals())


def about(request):
    welcome = "Bienvenue à l 'Église Protestante Évangélique \n aux Gobelins"

    # Mail sending request
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = ContactForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            send_mail(
                subject=str(form["subject"].value()),
                message=str(form['message'].value()),
                from_email='kevin.amouh@gmail.com',
                recipient_list=[str(form['email'].value())],
                fail_silently=False
            )

        form.clean()
        form = ContactForm()

    else:
        form = ContactForm()

    return render(request, 'appv/about-us.html', locals())


def activity(request):
    welcome = "Bienvenue à l 'Eglise Protestante Evangélique \n aux Gobelins"
    announce = "appv/pdf/programme_avril_2020.pdf"
    return render(request, 'appv/activity.html', locals())


def gallery(request):
    welcome = "Bienvenue à l 'Eglise Protestante Evangélique \n aux Gobelins"
    albums = Gallery.objects.values('album').distinct()
    photos = Gallery.objects.filter(type="Photo")
    videos = Gallery.objects.filter(type="Video")
    return render(request, 'appv/gallery.html', locals())


def sermon(request):
    welcome = "Bienvenue à l 'Eglise Protestante Evangélique \n aux Gobelins"
    sermons = Predication.objects.order_by('date').reverse()
    return render(request, 'appv/sermon.html', locals())
