from django.shortcuts import render


# Create your views here.
from portfolio.models import Profile, Projects, Skills, Education, Contacts


def home(request):
    return render(request, 'home.html')


def portfolio(request):
    profile = Profile.objects.all()
    projects = Projects.objects.filter(username=profile)
    skills = Skills.objects.filter(username=profile)
    education = Education.objects.filter(username=profile)
    contacts = Contacts.objects.filter(username=profile)
    context = {'profile': profile,
               'projects': projects,
               'skills': skills,
               'education': education,
               'contacts': contacts}

    return render(request, 'portfolio.html', context)