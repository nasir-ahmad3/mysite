from django import template 
from ..models import Project
from django.db.models  import Q


register = template.Library()


@register.inclusion_tag('partials/projects.html')
def last_projects():
	projects = Project.objects.published().order_by('-publish')[:10]

	html_projects 		= Project.objects.filter(Q(language_type="h") & Q(statuc="p")).order_by('-publish')[:10]
	css_projects 		= Project.objects.filter(Q(language_type="c") & Q(statuc="p")).order_by('-publish')[:10]
	python_projects 	= Project.objects.filter(Q(language_type="p") & Q(statuc="p")).order_by('-publish')[:10]
	django_projects 	= Project.objects.filter(Q(language_type="d") & Q(statuc="p")).order_by('-publish')[:10]
	javascript_projects = Project.objects.filter(Q(language_type="j") & Q(statuc="p")).order_by('-publish')[:10]
	bootstrap_projects 	= Project.objects.filter(Q(language_type="b") & Q(statuc="p")).order_by('-publish')[:10]


	return {
		'project_list' 			: projects,
		'html_projects' 		: html_projects,
		'css_projects' 			: css_projects,
		'python_projects' 		: python_projects,
		'django_projects' 		: django_projects,
		'javascript_projects'	: javascript_projects,
		'bootstrap_projects' 	: bootstrap_projects,
	}
