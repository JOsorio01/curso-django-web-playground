from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.shortcuts import get_object_or_404
from registration.models import Profile

# Create your views here.
class ProfilesList(ListView):
    model = Profile
    template_name = 'profiles/profile_list.html'
    paginate_by = 3

class ProfileDetail(DetailView):
    model = Profile
    template_name = 'profiles/profile_detail.html'

    def get_object(self, queryset=None, **kwargs):
        return get_object_or_404(Profile, user__username=self.kwargs['username'])