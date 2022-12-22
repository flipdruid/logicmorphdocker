from django.views.generic import ListView
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from accounts.decorators import allowed_users

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
    paginate_by = 9
    context_object_name = "posts"

class Carousel(ListView):
    model = Post
    template_name = "main/carousel.html"
    paginate_by = 9
    context_object_name = "posts"
    

@method_decorator(allowed_users(allowed_roles=['admin', 'staff', 'client']),  name="dispatch")
class Dashboard(TemplateView):
    template_name = "main/dashboard.html"