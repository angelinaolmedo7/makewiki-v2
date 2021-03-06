from django.urls import path

from api.views import PageList, PageDetail

urlpatterns = [
    path('wiki/', PageList.as_view(), name='pages_list'),
    path('wiki/<int:pk>', PageDetail.as_view(), name='pages_detail')
]
