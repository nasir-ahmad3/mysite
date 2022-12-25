from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, FormView, TemplateView
from projects.models import Project
from skills.models import Skill
from about.models import About
from .models import contact
from .forms import ContactForm
from django.urls import reverse_lazy
from .models import contact
from django.http import HttpResponseRedirect


# Create your views here.
def home (request):

	if request.method == 'POST':
		form = ContactForm(request.POST)
		if form.is_valid():
			form.send()
			return redirect('base:success')
	else:
		form = ContactForm()
	context = {
		'projec_list' : Project.objects.published()[:6],
		'skill_list'  : Skill.objects.all(),
		'about_list'  : About.objects.all(),
		'contact' 	  : contact,
		'form'  	  : ContactForm
	}

	return render(request, 'base/home.html', context)



class ContactSuccessView(TemplateView):
	template_name = 'contact/success.html'