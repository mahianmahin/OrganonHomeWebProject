from chember_app import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

admin.site.site_header = "Organon Homeo Chember Administration"
admin.site.site_title = "Organon Homeo Chember admin portal"
admin.site.index_title = "Organon Homeo Chember Admin Portal"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('blogs/', views.blogs, name="blogs"),
    path('contact/', views.contact, name="contact"),
    path('post_actions/subscription/', views.subs_done, name="subs_done"),
    path('post_actions/contact/', views.contact_done, name="contact_done"),
    path('post_actions/already_subscribed/', views.already_subs, name="already_subs")
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
