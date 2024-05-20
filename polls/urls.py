from django.urls import path
# from polls.views import home
from . import views
app_name = 'poll'
urlpatterns = [
    path('', views.home, name="home"),
    path('polls/', views.get_polls, name="get_polls"),
    path('<int:q_id>/vote/', views.vote, name="vote"),
    path('<int:q_id>/result/', views.result, name="result"),
]