import os
import django
import json
from django.core import serializers

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio_project.settings')
django.setup()

from portfolio.models import Project, Profile, Skill, Experience, Education, Certification

def dump_data():
    models = [Profile, Skill, Experience, Education, Certification, Project]
    all_objects = []
    for model in models:
        all_objects.extend(list(model.objects.all()))
    
    data = serializers.serialize('json', all_objects, indent=2)
    with open('data.json', 'w', encoding='utf-8') as f:
        f.write(data)
    print("Successfully dumped data to data.json with UTF-8 encoding")

if __name__ == '__main__':
    dump_data()
