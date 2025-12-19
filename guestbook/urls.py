from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns = [
    path("", views.HomeView.as_view(), name="guestbook_home"),
    path("<int:id>", views.MessageView.as_view(), name="guestbook_message"),
    path("add", views.CreateEntryView.as_view(), name="guestbook_add"),
    path("update/<int:pk>", views.UpdateEntryView.as_view(), name="guestbook_update"),
    path("delete/<int:pk>", views.DeleteEntryView.as_view(), name="guestbook_delete"),
    path("login", views.MyLoginView.as_view(), name="guestbook_login"),
    path("logout", LogoutView.as_view(), name="guestbook_logout"),
    path("signup", views.SignUpView.as_view(), name="guestbook_signup"),
]