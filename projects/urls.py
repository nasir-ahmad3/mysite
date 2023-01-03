from django.urls import path
from .views import ProjectList, ProjectDetail, BackendLanguages

app_name= 'projects'
urlpatterns = [
	path('', ProjectList.as_view(), name='ProjectList'),
	path('detail/<slug:slug>', ProjectDetail.as_view(), name='ProjectDetail'),
	path('backend_projects/<slug:slug>', BackendLanguages.as_view(), name="backend_languages")
]

