from ckeditor.fields import RichTextField
from django.core.mail import send_mail
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class DoctorInfo(models.Model):
    name = models.CharField(max_length=300, verbose_name="Enter name in BANGLA")
    certification = models.CharField(max_length=300, verbose_name="Enter certification in BANGLA")
    profile_picture = models.ImageField(null=True, blank=True, upload_to="DoctorInfo")
    phone_number = models.IntegerField()
    mail_address = models.EmailField(max_length=200)
    chember_location = models.CharField(max_length=500)

class SiteUtilitie(models.Model):
    Home_page_text = RichTextField(verbose_name="Home page text BANGLA")
    google_map_embed_link = models.CharField(max_length=1000)

class AboutText(models.Model):
    heading = models.CharField(max_length=1500)
    description = RichTextField(verbose_name="Enter Description")

class Subscriber(models.Model):
    email = models.EmailField(max_length=500)

class Blog(models.Model):
    author = models.ForeignKey(DoctorInfo, on_delete=models.CASCADE)
    heading = models.CharField(max_length=1500, verbose_name="Blog heading")
    image = models.ImageField(null=True, blank=True, upload_to="blogs", verbose_name="Select an image if you want to add one")
    description = RichTextField(verbose_name="Write your blog here")
    published_date = models.DateTimeField(auto_now=True)

@receiver(post_save, sender=Blog)
def at_ending_save(sender, instance, created, **kwargs):
    if created:
        subscribers_list = []
        subs = Subscriber.objects.all()

        for subscribers in subs:
            subscribers_list.append(subscribers.email)

        send_mail(
            "New Post Uploaded",
            "A new post just been uploaded on **organonhomeochember.com** \n Visit the new post from here : **organonhomeochember.com/blogs** \n\n - From Abdul Wadud\nOrganon Homeo Chember",
            'doctor@organonhomeochember.com',
            subscribers_list,
            fail_silently=False
        )

class Treatment(models.Model):
    treatment_type = models.CharField(max_length=200, verbose_name="Enter a treatment type name")

