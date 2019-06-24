from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator
from django.utils.text import slugify
from .models import Page
from .forms import PageForm


class PageListView(ListView):
	model = Page


class PageDetailView(DetailView):
	model = Page


@method_decorator(staff_member_required, name='dispatch')
class PageCreate(CreateView):
	model = Page
	form_class = PageForm
	success_url =  reverse_lazy('pages:pages')


@method_decorator(staff_member_required, name='dispatch')
class PageUpdate(UpdateView):
	model = Page
	form_class = PageForm
	template_name_suffix = '_update_form'

	def get_success_url(self):
		return reverse_lazy('pages:page', args=[self.object.id, slugify(self.object.title)])


@method_decorator(staff_member_required, name='dispatch')
class PageDelete(DeleteView):
	model = Page
	
	def get_success_url(self):
		return reverse_lazy('pages:pages')
