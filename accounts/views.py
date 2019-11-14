from django.shortcuts import render

from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView

# Create your views here.
class SignUpView(CreateView):
    """Renders a sign up page."""

    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

# class LogInView(CreateView):
#     """ Renders a log in page."""

#     def get(self, request):
#         """ Returns a log in page. """
#         return render(request, 'registration/login.html', {
#         })