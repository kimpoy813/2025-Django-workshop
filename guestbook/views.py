from webbrowser import get
from django.http import Http404, HttpResponse
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from . import models
from . import forms
from django.urls import reverse_lazy

class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("guestbook_login")
    template_name = "registration/signup.html"

class MyLoginView(LoginView):
    template_name = "auth/login.html"        

class CommonViewSettings(LoginRequiredMixin):
    template_name = "guestbook/add.html"
    model = models.Guest
    form_class = forms.CreateEntryForm
    success_url = reverse_lazy("guestbook_home")

class CreateEntryView(CommonViewSettings, CreateView):
    template_name = "guestbook/add.html"

    def form_valid(self, form):
        # if not self.request.user.is_authenticated:
        #     form.add_error(None, "Login first")

        #     return super().form_invalid(form)
        
        if "shit" in form.data["message"].lower():
            form.add_error("message", "Inappropriate word detected")

            return super().form_invalid(form)

        form.instance.owner = self.request.user

        return super().form_valid(form)

class UpdateEntryView(CommonViewSettings, UpdateView):
    template_name = "guestbook/update.html"

class DeleteEntryView(DeleteView):
    model = models.Guest
    success_url = reverse_lazy("guestbook_home")
    template_name = "guestbook/delete.html"

    def get_object(self, *args, **kwargs):
        if not self.request.user.is_authenticated:
            return None
        
        obj = None 
        try:
            if self.request.user.is_superuser:
                obj = super().get_object(*args, **kwargs)
        except Http404:
            return None
        
        return obj

class HomeView(ListView):
    template_name = "guestbook/index.html"
    model = models.Guest
    #queryset = models.Guest.objects.filter(active=True).order_by("-date_posted")
    
    def get_queryset(self):
        qs = super().get_queryset()
        qs = qs.order_by("-date_posted")

        return qs

class MessageView(DetailView):
    template_name = "guestbook/message.html"
    model = models.Guest
    pk_url_kwarg = "id"


