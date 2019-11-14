from django.urls import path
from wiki.views import PageListView, PageDetailView, SignUpView, LogInView


urlpatterns = [
    path('', PageListView.as_view(), name='wiki-list-page'),
    path('accounts/signup', SignUpView.as_view(), name='wiki-signup-page'),
    path('accounts/login', LogInView.as_view(), name='login'),
    path('<str:slug>/', PageDetailView.as_view(), name='wiki-details-page'),
]
