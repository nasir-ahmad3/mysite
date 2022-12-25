from django import template 

register = template.Library()


# @register.inclusion_tag('partials/django_projects.html')
# def django_projects():
# 	projects = DjangoProjects.objects.filter(status="p")
# 	return {
# 		'projec_list' : projects
# 	}