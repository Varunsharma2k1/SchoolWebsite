from django.conf import settings
from django.shortcuts import redirect, render
from django.core.mail import send_mail
# from project.chanakya.utils import send_email_to
from .models import Teacher,Event,Sport,Achievement
from .forms import *
from django.shortcuts import render
# from .utils import send_email_to
def home(request):
    notices= NoticeBoard.objects.all()
    print(notices.count())
    return render(request,'chanakya/index.html',{'notices':notices})

def schoolprofile(request):
    return render(request,'chanakya/schoolprofile.html')

def principal(request):
    return render(request,'chanakya/principal.html')

def founder(request):
    return render(request,'chanakya/founder.html')

def gallery(request):
    event = Event.objects.all()
    sport = Sport.objects.all()
    achievement= Achievement.objects.all()
    return render(request,'chanakya/gallery.html',{'sport':sport,'achievement':achievement, 'event':event})

def faculty(request):
    faculties = Teacher.objects.all()
    return render(request,'chanakya/faculty.html',{'faculties':faculties})

def affiliation(request):
    return render(request,'chanakya/affiliation.html')

def admission(request):
    form= RegistrationForm()
    
    if(request.method=='POST'):
        print("hi")
        form=RegistrationForm(request.POST)
        if form.is_valid():
            form.save() 
            subject = "New Registration Candidate"
            message = "Kindly Check the database for the new entry as someone just filled your Registration form"
            from_email = settings.EMAIL_HOST_USER
            recipient_list = ["vishu200k1@gmail.com"]
            send_mail(subject, message ,from_email, recipient_list)
            return render (request,'chanakya/index.html')
    return render(request,'chanakya/admission.html',{'form':form})

# def send_email(request):
#     send_email_to()
#     return redirect('/')

def career(request):
    form= CareerForm()
    if(request.method=='POST'):
        print("hi")
        form=CareerForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            subject = "New Career Candidate"
            message = "Kindly Check the database for the new entry as someone just filled your Career form"
            from_email = settings.EMAIL_HOST_USER
            recipient_list = ["vishu200k1@gmail.com"]
            send_mail(subject, message ,from_email, recipient_list)
            return render(request,'chanakya/index.html')
    return render(request,'chanakya/career.html',{'form':form})

def privacy(request):
    return render(request,'chanakya/privacy.html')

