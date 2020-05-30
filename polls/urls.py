from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
	path('users',views.users),
	path('register',views.register, name='register'),
	path('<int:question_id>/', views.detail, name='detail'), 
	path('<int:question_id>/results/', views.results, name='results'),
	path('<int:question_id>/vote/', views.vote, name='vote'),
	path('test', views.test, name='test'),
]