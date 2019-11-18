from django.http.response import HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from django.urls import reverse_lazy

from ..api.models import LastQueryApi


class Index(TemplateView):
    http_method_names = ('get',)
    template_name = 'app/index.html'

    # Redirect if user is authenticated
    def get(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return HttpResponseRedirect(reverse_lazy('app:home'))
        return super().get(request, *args, **kwargs)


class Home(LoginRequiredMixin, TemplateView):
    http_method_names = ('get',)
    login_url = reverse_lazy('core:signin')
    template_name = 'app/home.html'

    def get(self, request, *args, **kwargs):
        githubUser = request.GET.get('githubUser')
        if githubUser is '':
            return HttpResponseRedirect(reverse_lazy('app:home'))
        return super().get(request, *args, **kwargs)
