from django.urls import path

from . import views

app_name = "blog"
urlpatterns = [
    path('', views.post_list, name='index'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),

    path('<int:post_id>/', views.post_view, name='post_view'),
    path('<int:post_id>/comment', views.new_comment, name='new_comment'),

    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    
    path('dashboard/', views.dashboard_posts, name='dashboard_posts'),
    path('dashboard/posts/', views.dashboard_posts, name='dashboard_posts'),
    path('dashboard/posts/<int:post_id>/', views.dashboard_posts_with_post, name='dashboard_posts_with_post'),
    path('dashboard/posts/new/', views.new_post, name='new_post'),
    path('dashboard/posts/edit/<int:post_id>/', views.edit_post, name='edit_post'),
    path('dashboard/posts/delete/<int:post_id>/', views.delete_post, name='delete_post'),
    path('dashboard/posts/publish/<int:post_id>/', views.publish_post, name='publish_post'),
    path('dashboard/posts/<int:post_id>/delete/<int:comment_id>', views.dashboard_post_delete_comment, name='dashboard_post_delete_comment'),

    path('dashboard/comments/', views.dashboard_comments, name='dashboard_comments'),
    path('dashboard/comments/delete/<int:comment_id>/', views.delete_comment, name='delete_comment'),

    path('dashboard/static/', views.dashboard_static, name='dashboard_static'),
    path('dashboard/static/about', views.edit_about, name='edit_about'),
    path('dashboard/static/contact', views.edit_contact, name='edit_contact'),

    path('dashboard/page/', views.dashboard_page, name='dashboard_page'),
    
]