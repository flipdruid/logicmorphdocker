from django.views.generic import ListView
from django.views.generic import TemplateView


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
    paginate_by = 3
    context_object_name = "posts"