from django.urls import path

from . import views

app_name = "blog"
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:post_id>/', views.post_view, name='post_view'),
    path('<int:post_id>/comment', views.new_comment, name='new_comment'),
]