from django.shortcuts import render
from django.views.generic import ListView
from alumni.models import Alumni
from django.db.models import Q
# Create your views here.
class SearchList(ListView):
	template_name = 'search_result.html'
	context_object_name = 'search_list'

	def get_context_data(self, *args, **kwargs):
		context = super(SearchList, self).get_context_data(*args, **kwargs)
		context['query'] = self.request.GET.get('q')
		return context

	def get_queryset(self, *args, **kwargs):
		request = self.request
		query = request.GET.get('q', None)
		if query is not None:
			return Alumni.objects.filter(Q(user__username__icontains=query)|Q(graduation__faculty__icontains=query)|Q(graduation__yearOfGraduation__icontains=query)|Q(graduation__groupNumber__icontains=query)|Q(company__name__icontains=query)).distinct()
		return Alumni.objects.none()

	