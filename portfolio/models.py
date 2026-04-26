from django.db import models

class Profile(models.Model):
    name = models.CharField(max_length=100)
    about_me = models.TextField()
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    linkedin = models.URLField(blank=True)
    github = models.URLField(blank=True)
    
    def __str__(self):
        return self.name

class Skill(models.Model):
    CATEGORY_CHOICES = [
        ('technical', 'Technical Skills'),
        ('analytical', 'Analytical Skills'),
        ('soft', 'Soft Skills'),
        ('language', 'Languages'),
    ]
    name = models.CharField(max_length=50)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    proficiency = models.CharField(max_length=50, blank=True) # e.g. "Native", "Fluent"

    def __str__(self):
        return f"{self.name} ({self.get_category_display()})"

class Experience(models.Model):
    job_title = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    start_date = models.CharField(max_length=50)
    end_date = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self):
        return f"{self.job_title} at {self.company}"

class Education(models.Model):
    institution = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    degree = models.CharField(max_length=100)
    graduation_date = models.CharField(max_length=50)
    gpa = models.CharField(max_length=10, blank=True)
    details = models.TextField(blank=True)

    def __str__(self):
        return f"{self.degree} from {self.institution}"

class Certification(models.Model):
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name

class Project(models.Model):
    title = models.CharField(max_length=200)
    summary = models.CharField(max_length=255)
    business_problem = models.TextField()
    tools_used = models.CharField(max_length=200) # e.g. "Python, Scikit-learn, Pandas"
    key_features = models.TextField()
    role = models.TextField()
    biggest_challenge = models.TextField()
    what_you_learned = models.TextField()
    image = models.ImageField(upload_to='projects/', blank=True, null=True)
    icon_class = models.CharField(max_length=50, default='bi-terminal')
    video_static_path = models.CharField(max_length=255, blank=True, null=True)
    static_image_1 = models.CharField(max_length=255, blank=True, null=True) # New field
    static_image_2 = models.CharField(max_length=255, blank=True, null=True) # New field
    github_link = models.URLField(blank=True)
    demo_link = models.URLField(blank=True)
    slug = models.SlugField(unique=True, blank=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            from django.utils.text import slugify
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
