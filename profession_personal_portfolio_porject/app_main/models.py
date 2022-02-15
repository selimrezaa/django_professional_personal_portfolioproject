from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Home(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
    image = models.ImageField(upload_to='home_image', blank=True, null=True)
    professions = models.CharField(max_length=200, blank=True, null=True)
    facebook = models.URLField(blank=True, null=True)
    twitter = models.URLField(blank=True, null=True)
    instagram = models.URLField(blank=True, null=True)
    pinterest = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.user.username


class Service(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    title_image = models.ImageField(upload_to = 'service_images')
    short_desc = models.CharField(max_length=264)
    description = models.TextField()
    desc_title = models.CharField(max_length=100)
    desc_link = models.URLField(blank=True, null=True)
    desc_servciec_include = models.CharField(max_length=264)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
    full_name = models.CharField(max_length=100 ,blank=True, null=True)
    image = models.ImageField(upload_to='profile_img_and_files', blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    phone = models.CharField(max_length=15, blank=True, null=True)
    address = models.TextField( blank=True, null=True)
    twitter = models.URLField( blank=True, null=True)
    short_msg = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField( blank=True, null=True)
    cv = models.FileField(upload_to='profile_img_and_files', )

    def __str__(self):
        return self.full_name

class Skills(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    skill = models.CharField(max_length=50)
    skill_percentage = models.IntegerField()

    def __str__(self):
        return self.skill


class Portfolio(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=15)
    short_title = models.CharField(max_length=15)
    image = models.ImageField(upload_to='portfolio_images')

    def __str__(self):
        return self.name

class CountDown(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    clients = models.IntegerField()
    projects = models.IntegerField()
    awards = models.IntegerField()
    years_experience = models.IntegerField()

    def __str__(self):
        return self.user.username


class Testimonial(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField()
    client_name = models.CharField(max_length=30)
    client_name_title = models.CharField(max_length=50)

    def __str__(self):
        return "Testimonial"

    def __str__(self):
        return self.user.username

class Partners(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    company_logo = models.ImageField(upload_to='testimonial_images')

    def __str__(self):
        return "Partners"


class Contact(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=55)
    message = models.TextField()

    def __str__(self):
        return self.full_name+"'s Messages'"

class Lets_Connect(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    facebook = models.URLField(blank=True, null=True)
    twitter = models.URLField(blank=True, null=True)
    instagram = models.URLField(blank=True, null=True)
    pinterest = models.URLField(blank=True, null=True)
    skype = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.facebook+"Connecting link"

class Footer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    copy_right_text = models.CharField(max_length=264, blank=True, null=True)
