from django.shortcuts import render, get_object_or_404
from .models import Profile, Skill, Experience, Education, Certification, Project

def home(request):
    profile = Profile.objects.first()
    featured_projects = Project.objects.all()[:3]
    return render(request, 'portfolio/home.html', {'profile': profile, 'featured_projects': featured_projects})

def about(request):
    profile = Profile.objects.first()
    return render(request, 'portfolio/about.html', {'profile': profile})

def projects(request):
    projects_list = Project.objects.all()
    return render(request, 'portfolio/projects.html', {'projects_list': projects_list})

def project_detail(request, slug):
    project = get_object_or_404(Project, slug=slug)
    return render(request, 'portfolio/project_detail.html', {'project': project})

def skills(request):
    skills_technical = Skill.objects.filter(category='technical')
    skills_analytical = Skill.objects.filter(category='analytical')
    skills_soft = Skill.objects.filter(category='soft')
    languages = Skill.objects.filter(category='language')
    return render(request, 'portfolio/skills.html', {
        'skills_technical': skills_technical,
        'skills_analytical': skills_analytical,
        'skills_soft': skills_soft,
        'languages': languages
    })

def certifications(request):
    certifications_list = Certification.objects.all()
    return render(request, 'portfolio/certifications.html', {'certifications_list': certifications_list})

def resume(request):
    experiences = Experience.objects.all().order_by('-start_date')
    education = Education.objects.all().order_by('-graduation_date')
    certifications = Certification.objects.all()
    return render(request, 'portfolio/resume.html', {
        'experiences': experiences,
        'education': education,
        'certifications': certifications
    })

def contact(request):
    profile = Profile.objects.first()
    return render(request, 'portfolio/contact.html', {'profile': profile})
