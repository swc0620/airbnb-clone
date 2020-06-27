from django.views import View
from django.views.generic import FormView
from django.shortcuts import render, redirect, reverse
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login, logout
from . import forms

# Create your views here.

# Django Class Based View
class LoginView(View):
    def get(self, request):
        form = forms.LoginForm()
        return render(request, "users/login.html", context={
            "form": form,
        })

    def post(self, request):
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            # django returns data that passed validation as "cleaned_data"
            # print(form.cleaned_data)
            email = form.cleaned_data.get("email")
            password = form.cleaned_data.get("password")
            user = authenticate(request, username=email, password=password)
            if user is not None:
                login(request, user)
                return redirect(reverse("core:home"))
        return render(request, "users/login.html", context={
            "form": form,
        })

def log_out(request):
    logout(request)
    return redirect(reverse("core:home"))

# class LoginView(FormView):
#     template_name = "users/login.html"
#     form_class = forms.LoginForm

#     # reverse() goes to the url and returns the actual url.
#     # The problem is when the LoginView form loads, the url is not loaded yet. Therefore the code below raises error.
#     # success_url = reverse("core:home")

#     # reverse_lazay() is not immediately executed, but is executed only when the view is loaded
#     success_url = reverse_lazy("core:home")

#     def form_valid(self, form):
#         email = form.cleaned_data.get("email")
#         password = form.cleaned_data.get("password")
#         user = authenticate(self.request, username=email, password=password)
#         if user is not None:
#             login(self.request, user)
#         return super().form_valid(form)