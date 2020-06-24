from django.shortcuts import render, get_object_or_404
from .models import Alumni, Graduation, GraduationProject, Company, Job
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
# Create your views here.

class AlumniList(ListView):
	model = Alumni
	template_name = 'alumni_list.html'
	context_object_name = 'alumni_list'

class AlumniDetail(DetailView):
	model = Alumni
	template_name = 'alumni_detail.html'

class AlumniEdit(LoginRequiredMixin, UpdateView):
	model = Alumni
	template_name = 'alumni_edit.html'
	fields = ('image',)
	def get_success_url(self):
		return reverse('AlumniDetail',args=(self.request.user.id,))

class GraduationCreateView(LoginRequiredMixin, CreateView):
	model = Graduation
	template_name = "graduation_new.html"
	fields = ('faculty', 'degree', 'yearOfGraduation', 'groupNumber')
	def get_success_url(self):
		return reverse('AlumniDetail',args=(self.request.user.id,))

	def form_valid(self, form):
		self.object = form.save(commit=False)
		alumni = get_object_or_404(Alumni, pk=self.kwargs['pk'])
		self.object.alumni = alumni
		self.object.save()
		return super(GraduationCreateView, self).form_valid(form)
	def dispatch(self, request, *args, **kwargs):
		obj = get_object_or_404(Alumni, pk=self.kwargs['pk'])
		if obj.user != self.request.user:
			raise PermissionDenied
		return super().dispatch(request, *args, **kwargs)

class GraduationUpdateView(UpdateView):
	model = Graduation
	template_name = "graduation_edit.html"
	fields = ('faculty', 'degree', 'yearOfGraduation', 'groupNumber')
	def get_success_url(self):
		return reverse('AlumniDetail',args=(self.request.user.id,))
	def dispatch(self, request, *args, **kwargs):
		obj = get_object_or_404(Graduation, pk=self.kwargs['pk'])
		if obj.alumni.user != self.request.user:
			raise PermissionDenied
		return super().dispatch(request, *args, **kwargs)

class GraduationDeleteView(DeleteView):
	model = Graduation
	template_name = "graduation_delete.html"
	def get_success_url(self):
		return reverse('AlumniDetail',args=(self.request.user.id,))
	def dispatch(self, request, *args, **kwargs):
		obj = get_object_or_404(Graduation, pk=self.kwargs['pk'])
		if obj.alumni.user != self.request.user:
			raise PermissionDenied
		return super().dispatch(request, *args, **kwargs)


class GraduationProjectCreateView(CreateView):
	model = GraduationProject
	template_name = "graduation_project_new.html"
	fields = ('title', 'description', 'mark', 'gitLink')
	def get_success_url(self):
		return reverse('AlumniDetail',args=(self.request.user.id,))
	def form_valid(self, form):
		self.object = form.save(commit=False)
		grad = get_object_or_404(Graduation, pk=self.kwargs['pk'])
		self.object.graduation = grad
		self.object.save()
		return super(GraduationProjectCreateView, self).form_valid(form)
	def dispatch(self, request, *args, **kwargs):
		obj = get_object_or_404(Graduation, pk=self.kwargs['pk'])
		if obj.alumni.user != self.request.user:
			raise PermissionDenied
		return super().dispatch(request, *args, **kwargs)
class GraduationProjectUpdateView(UpdateView):
	model = GraduationProject
	template_name = "graduation_project_edit.html"
	fields = ('title', 'description', 'mark', 'gitLink')
	def get_success_url(self):
		return reverse('AlumniDetail',args=(self.request.user.id,))
	def dispatch(self, request, *args, **kwargs):
		obj = get_object_or_404(Graduation, pk=self.kwargs['pk'])
		if obj.alumni.user != self.request.user:
			raise PermissionDenied
		return super().dispatch(request, *args, **kwargs)

class GraduationProjectDeleteView(DeleteView):
	model = GraduationProject
	template_name = "graduation_project_delete.html"
	context_object_name = "project"
	def get_success_url(self):
		return reverse('AlumniDetail',args=(self.request.user.id,))
	def dispatch(self, request, *args, **kwargs):
		obj = get_object_or_404(Graduation, pk=self.kwargs['pk'])
		if obj.alumni.user != self.request.user:
			raise PermissionDenied
		return super().dispatch(request, *args, **kwargs)

class CompanyCreateView(CreateView):
	model = Company
	template_name = "company_new.html"
	fields = ('name','address','email','information')
	def get_success_url(self):
		return reverse('AlumniDetail',args=(self.request.user.id,))
	def form_valid(self, form):
		self.object = form.save(commit=False)
		alumni = get_object_or_404(Alumni, pk=self.kwargs['pk'])
		self.object.alumni = alumni
		self.object.save()
		return super(CompanyCreateView, self).form_valid(form)
	def dispatch(self, request, *args, **kwargs):
		obj = get_object_or_404(Alumni, pk=self.kwargs['pk'])
		if obj.user != self.request.user:
			raise PermissionDenied
		return super().dispatch(request, *args, **kwargs)

class CompanyUpdateView(UpdateView):
	model = Company
	template_name = "company_edit.html"
	fields = ('name','address','email','information')
	def get_success_url(self):
		return reverse('AlumniDetail',args=(self.request.user.id,))
	def dispatch(self, request, *args, **kwargs):
		obj = get_object_or_404(Company, pk=self.kwargs['pk'])
		if obj.alumni.user != self.request.user:
			raise PermissionDenied
		return super().dispatch(request, *args, **kwargs)

class CompanyDeleteView(DeleteView):
	model = Company
	template_name = "company_delete.html"
	def get_success_url(self):
		return reverse('AlumniDetail',args=(self.request.user.id,))
	def dispatch(self, request, *args, **kwargs):
		obj = get_object_or_404(Company, pk=self.kwargs['pk'])
		if obj.alumni.user != self.request.user:
			raise PermissionDenied
		return super().dispatch(request, *args, **kwargs)

class JobCreateView(CreateView):
	model = Job
	template_name = "job_new.html"
	fields = ('position', 'startDate', 'endDate')
	def get_success_url(self):
		return reverse('AlumniDetail',args=(self.request.user.id,))
	def form_valid(self, form):
		self.object = form.save(commit=False)
		comp = get_object_or_404(Company, pk=self.kwargs['pk'])
		self.object.company = comp
		self.object.save()
		return super(JobCreateView, self).form_valid(form)
	def dispatch(self, request, *args, **kwargs):
		obj = get_object_or_404(Company, pk=self.kwargs['pk'])
		if obj.alumni.user != self.request.user:
			raise PermissionDenied
		return super().dispatch(request, *args, **kwargs)
class JobUpdateView(UpdateView):
	model = Job
	template_name = "job_edit.html"
	fields = ('position', 'startDate', 'endDate')
	def get_success_url(self):
		return reverse('AlumniDetail',args=(self.request.user.id,))
	def dispatch(self, request, *args, **kwargs):
		obj = get_object_or_404(Job, pk=self.kwargs['pk'])
		if obj.company.alumni.user != self.request.user:
			raise PermissionDenied
		return super().dispatch(request, *args, **kwargs)

class JobDeleteView(DeleteView):
	model = Job
	template_name = "job_delete.html"
	def get_success_url(self):
		return reverse('AlumniDetail',args=(self.request.user.id,))
	def dispatch(self, request, *args, **kwargs):
		obj = get_object_or_404(Job, pk=self.kwargs['pk'])
		if obj.company.alumni.user != self.request.user:
			raise PermissionDenied
		return super().dispatch(request, *args, **kwargs)