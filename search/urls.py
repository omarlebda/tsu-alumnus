from django.urls import path
from django.conf.urls import url
from .views import SearchList

urlpatterns = [
	path('', SearchList.as_view(), name='SearchList'),
]