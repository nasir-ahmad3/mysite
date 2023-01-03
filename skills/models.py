from django.db import models

# Create your models here.
class Skill(models.Model):
	title = models.CharField(max_length=200, help_text="This title will be show on the top of the card and also in the button")
	learn_presentage = models.IntegerField(null=True)
	logo = models.CharField(max_length=500, null=True, help_text="This is an important field, in this project only font (fontawesome) is used, so according to your skill, find a suitable icon from fontawesome and enter it, for example: <i class='fa-brands fa-html5'></i>")
	description = models.TextField(null=True)
	bg_color = models.CharField(max_length=200, null=True, help_text="This field is for the background color, as in the following example: linear-gradient(45deg, #56f58d, #00ff04);")

	def __str__(self):
		return self.title 
