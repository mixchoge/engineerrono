from django.urls import path
from .import views

urlpatterns = [
   path('', views.index, name="index"),
   path('me', views.me, name="me"),
   path('comment', views.comment, name="comment"),
   path('commenting', views.commenting, name="commenting"),
   path('contact', views.contact, name="contact"),
   path('chat', views.chat, name="chat"),
   path('register/', views.register, name="register"),
   path('login', views.login, name="login"),
   path('logout', views.logout, name="logout"),
   path('private', views.private, name="private"),
   path('texts', views.texts, name="texts")
]
