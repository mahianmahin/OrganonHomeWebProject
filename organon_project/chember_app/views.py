from django.conf import settings
from django.core.mail import EmailMessage, send_mail
from django.db.models.fields import EmailField
from django.http.response import HttpResponse
from django.shortcuts import redirect, render

from .models import *


# Create your views here.
def home(request):
    site_utils = SiteUtilitie.objects.all()
    treatments = Treatment.objects.all()

    if request.method == "POST":
        subs_mail = request.POST.get('email')

        subscribers = Subscriber.objects.all()
        match = False

        for subscribers in subscribers:
            if subs_mail == subscribers.email:
                match = True

        if match:
            return redirect('post_actions/already_subscribed')
        
        else:
            subs_ins = Subscriber(email=subs_mail)
            subs_ins.save()

            send_mail(
                "Thanks for Subscribing!",
                "Thanks for subscribing to **organonhomeochember.com** \n\n From now you will get a notification by email whenever a new blog is uploaded to **organonhomeochember.com/blogs** \n Thanks again, stay tuned! \n\n - From Abdul Wadud\nOrganon Homeo Chember",
                "doctor@organonhomeochember.com",
                [subs_mail],
                fail_silently=False
            )
            
            return redirect('post_actions/subscription')

    dict = {'home' : 'active', 'site_utils': site_utils, 'treatment' : treatments }
    return render(request, 'index.html', dict)

def about(request):
    about_db = AboutText.objects.all()

    dict = {'about' : 'active', 'about_db' : about_db}
    return render(request, 'about.html', dict)

def blogs(request):
    blogs = Blog.objects.order_by('-published_date')

    dict = {'blogs' : 'active', 'blogs_db' : blogs}
    return render(request, 'blogs.html', dict)

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')

        subject = name + " from " + email
        message_body = "Name: " + name + "\n" + "Phone: " + phone + "\n" + "E-mail: " + subject + "\n\n" + message

        send_mail(
            subject,
            message_body,
            'mollahwadud7@gmail.com',
            ['mahianmahin@yahoo.com', 'mollahwadud@yahoo.com']
        )

        return redirect('/post_actions/contact/')
    
    site_utils = SiteUtilitie.objects.all()

    dict = {'contact' : 'active', 'site_utils' : site_utils}
    return render(request, 'contact.html', dict)

def subs_done(request):
    return render(request, 'subs_done.html')

def contact_done(request):
    return render(request, 'contact_done.html')

def already_subs(request):
    return render(request, 'already_subscribed.html')
