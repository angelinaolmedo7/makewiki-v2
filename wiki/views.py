from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from wiki.models import Page


class PageListView(ListView):
    """ Renders a list of all Pages. """
    model = Page

    def get(self, request):
        """ GET a list of Pages. """
        pages = self.get_queryset().all()
        return render(request, 'list.html', {
          'pages': pages
        })

class PageDetailView(DetailView):
    """ Renders a specific page based on it's slug."""
    model = Page

    def get(self, request, slug):
        """ Returns a specific wiki page by slug. """
        page = self.get_queryset().get(slug__iexact=slug)
        return render(request, 'page.html', {
          'page': page
        })

class SignUpView(DetailView):
    """Renders a sign up page."""
    model = Page

    def get(self, request):
        """ Returns a sign up page. """
        return render(request, 'registration/signup.html', {
        })

class LogInView(DetailView):
    """ Renders a log in page."""
    model = Page

    def get(self, request):
        """ Returns a log in page. """
        return render(request, 'registration/login.html', {
        })
