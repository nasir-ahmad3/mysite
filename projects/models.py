from django.db import models
from django.utils import timezone

# my manager
class ProjectManager(models.Manager):
	def published(self):
		return self.filter(statuc='p')

# Create your models here.
class Project(models.Model):
	STATUS_CHOICES = (
		('d' , 'Draft'),
		('p' , 'publish'),
	)
	LANGUAGE_CHOICES = (
		('p', 'python'),
		('d', 'django'),
		('c', 'css'),
		('h', 'html'),
		('b', 'bootstrap'),
		('j', 'javascript'),
	)
	title  		    = models.CharField(max_length=200)
	is_private 		= models.BooleanField(default=False)
	slug            = models.SlugField(unique=True, max_length=100)
	description     = models.TextField()
	language_type   = models.CharField(max_length=1, choices=LANGUAGE_CHOICES)
	thumbnail 	    = models.ImageField(upload_to='images')
	html_code 	    = models.TextField(null=True, blank=True)
	css_code 	    = models.TextField(null=True, blank=True)
	javascript_code = models.TextField(null=True, blank=True)
	publish  		= models.DateTimeField(default=timezone.now)
	created  		= models.DateTimeField(auto_now_add=True)
	updated  		= models.DateTimeField(auto_now=True)
	# Project 		= models.FileField(upload_to="projects", null=True, blank=True)
	downlaod_link   = models.URLField(null=True)
	statuc			= models.CharField(max_length=1, choices=STATUS_CHOICES)


	def __str__(self):
		return self.title

	objects = ProjectManager()


