from django.urls import reverse_lazy
from django.views import generic

from .forms import UserCreationForm

class SignupView(generic.CreateView):
    form_class= UserCreationForm
    template_name= 'registration/signup.html'
    success_url= reverse_lazy('login')