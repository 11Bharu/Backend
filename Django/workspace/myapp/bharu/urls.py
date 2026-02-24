from django.urls import path
from . import views
app_name = 'bharu'
urlpatterns = [
    path("",views.index, name="index" ),
    path("post/<str:post_id>", views.menus, name="menu" ),
    path("details/<int:post_id>", views.details, name="details" ),
    path("old_url",views.old_url_redirect, name="old_url" ), 
    path("new_something_url",views.new_url_view, name="new_page_url" ),
    path("contact",views.contact_view, name="contact" ), 
    path("about",views.about_view, name="about" ),
]