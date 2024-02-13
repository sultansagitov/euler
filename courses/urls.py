from django.urls import path
from . import views
from . import api_views


urlpatterns = [
    path('', views.levels, name="levels"),
    path('create/level', views.createlevel, name="createlevel"),
    path('create/course', views.createcourse, name="createcourse"),
    path('<int:lvl>', views.level, name="level"),
    path('tutorial/<int:lvl>', views.tutorial, name="tutorial"),
    path('<int:lvl>/<int:que>', views.question, name="question"),
    path('getanswer/<int:lvl>/<int:que>/<int:ans>', api_views.getanswer, name="answer"),
    path('math', views.math_course, name='math')
]