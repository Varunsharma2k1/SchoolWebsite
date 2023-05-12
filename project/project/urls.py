"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.contrib import admin
from django.urls import path
from chanakya import views
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name="home"),
    path('schoolprofile',views.schoolprofile,name="schoolprofile"),
    path('principal',views.principal,name="principal"),
    path('founder',views.founder,name="founder"),
    path('gallery',views.gallery,name="gallery"),
    path('faculty',views.faculty,name="faculty"),
    path('career',views.career,name="career"),
    path('admission',views.admission,name="admission"),
    path('privacyPolicy',views.privacy,name="privacyPolicy"),
    path('affiliation',views.affiliation,name="affiliation"),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
else:
    urlpatterns += staticfiles_urlpatterns()
