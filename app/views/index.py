from logging import exception

from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.template import loader
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView
from django.views.generic import DeleteView
from django.views.generic import DetailView
from django.views.generic import ListView
from django.views.generic import TemplateView
from django.views.generic import UpdateView

from app.models import Lead
from app.models import Post


class Error400(TemplateView):
    template_name = "400.html"


class Error403(TemplateView):
    template_name = "403.html"


class Error404(TemplateView):
    template_name = "404.html"


class Error500(TemplateView):
    template_name = "500.html"


class Landing(ListView):
    model = Post
    template_name = "main/landing.html"
    paginate_by = 10
    context_object_name = "posts"