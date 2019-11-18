import json

from django.http.response import JsonResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import CreateView

from . import forms
from . import models


# Create your views here.
class SignUp(CreateView):
    http_method_names = ('get', 'post')
    form_class = forms.SignUpForm
    success_url = '/'
    template_name = 'core/signUp.html'

    def form_valid(self, form):
        """If the form is valid, save the associated model."""
        self.object = form.save()
        username = form.cleaned_data['username']
        password = form.cleaned_data['password1']
        user = authenticate(username=username, password=password)
        login(self.request, user) # After registration the user is signedin
        data = {'success': True}
        status = 201 # HTTP STATUS CREATED
        return JsonResponse(
            data,
            safe=False,
            status=status
        )

    def form_invalid(self, form):
        """If the form is invalid, render the invalid form."""
        data = dict(form.errors.items())
        data = json.dumps(data, ensure_ascii=False)
        status = 400 # HTTP STATUS BAD REQUEST
        return JsonResponse(
            data,
            safe=False,
            status=status
        )


class SignIn(LoginView):
    http_method_names = ('get', 'post')
    template_name = 'core/signIn.html'
    form_class = forms.SignInForm

    def form_valid(self, form):
        """Security check complete. Log the user in."""
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(username=username, password=password)
        if user is not None and user.is_active:
            login(self.request, user)
            data = {'success': True}
            status = 200 # HTTP STATUS OK
        else:
            data = {'detail': 'User is not active'}
            status = 401 # HTTP STATUS NOT AUTHORIZED
        return JsonResponse(data, safe=False, status=status)

    def form_invalid(self, form):
        data = dict(form.errors.items())
        data = json.dumps(data, ensure_ascii=False)
        status = 401 # HTTP STATUS NOT AUTHORIZED
        return JsonResponse(data, safe=False, status=status)


class SignOut(LogoutView):
    http_method_names = ('get')

    def get(self, request, *args, **kwargs):
        logout(request)
        return HttpResponseRedirect('/')
