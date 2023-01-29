from django.views.generic import ListView
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from accounts.decorators import allowed_users
from django.core.exceptions import ObjectDoesNotExist
from app.models import Post
from app.models.profile import Profile


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

    def get_context_data(self, **kwargs):
        context     =    super(Landing, self).get_context_data(**kwargs)
        posts       =    Post.objects.all()
        post_lists  ={}
        profile_img=""

        for post in posts:
            try:
                profile_img = Profile.objects.get(user=post.created_by)
                post_lists[post.id] = {
                    "title" : post.title,
                    "description": post.description,
                    "created_by":post.created_by,
                    "created_at":post.created_at,
                    "updated_at":post.updated_at,
                    "profile_img": profile_img.avatar
                }

            except ObjectDoesNotExist:  
                pass
            context['posts']     =    post_lists      
        # context['show_convert']     =  User.objects.filter(email=currentObject.email)
        return context

class Carousel(ListView):
    model = Post
    template_name = "main/carousel.html"
    paginate_by = 9
    context_object_name = "posts"

    def get_context_data(self, **kwargs):
        context     =    super(Carousel, self).get_context_data(**kwargs)
        posts       =    Post.objects.all()
        post_lists  ={}
        profile_img=""

        for post in posts:
            try:
                profile_img = Profile.objects.get(user=post.created_by)
                post_lists[post.id] = {
                    "title" : post.title,
                    "description": post.description,
                    "created_by":post.created_by,
                    "created_at":post.created_at,
                    "updated_at":post.updated_at,
                    "profile_img": profile_img.avatar
                }

            except ObjectDoesNotExist:  
                pass
            context['posts']     =    post_lists      
        # context['show_convert']     =  User.objects.filter(email=currentObject.email)
        return context
    
class EmailRegTemplate(TemplateView):
    template_name = "main/email_reg_template.html"