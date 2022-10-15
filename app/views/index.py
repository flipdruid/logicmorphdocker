from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from app.models import Post, Lead
from django.urls import reverse_lazy


class Landing(ListView):
    model               =   Post
    template_name       =   'main/landing.html'
    paginate_by         =   10
    context_object_name =   'post_list'

@method_decorator(login_required, name='dispatch')
class PostCreate(CreateView):
    model               =   Post
    template_name       =   'main/post_add.html'
    fields              =   ('title', 'description')
    success_url         =   reverse_lazy('main')  


    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)

@method_decorator(login_required, name='dispatch')
class PostView(DetailView):
    model               =   Post
    template_name       =   'main/post_view.html'
    pk_url_kwarg        =   'pk'
    context_object_name =   'poll'

class LeadCreate(CreateView):
    model           =   Lead
    template_name   =   'main/contact_us.html' 
    fields          =   '__all__'
    success_url     =   reverse_lazy("main") 

@method_decorator(login_required, name='dispatch')
class PostEdit(UpdateView):
    model               =   Post
    template_name       =   'main/post_edit.html'
    fields              =   ('title', 'description')
    pk_url_kwarg        =   'pk'
    success_url         =   reverse_lazy('main')

@method_decorator(login_required, name='dispatch')
class PostDelete(DeleteView):
    model               =   Post    
    pk_url_kwarg        =   'pk'
    success_url         =   reverse_lazy('main')
    template_name       =   'main/post_confirm_delete.html'
    context_object_name =   'post'