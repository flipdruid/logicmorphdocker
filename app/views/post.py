from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from accounts.decorators import allowed_users
from django.views.generic import  DetailView, UpdateView, CreateView, DeleteView
from app.models.post import Post


# @method_decorator(login_required, name="dispatch")
@method_decorator(allowed_users(allowed_roles=['admin', 'staff', 'client']),  name="dispatch")
class PostCreate(CreateView):
    model = Post
    template_name = "main/post_add.html"
    fields = ("title", "description")
    success_url = reverse_lazy("main")

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)


# @method_decorator(login_required, name="dispatch")
@method_decorator(allowed_users(allowed_roles=['admin', 'staff', 'client']),  name="dispatch")
class PostView(DetailView):
    model = Post
    template_name = "main/post_view.html"
    pk_url_kwarg = "pk"
    context_object_name = "posts"

# @method_decorator(login_required, name="dispatch")
@method_decorator(allowed_users(allowed_roles=['admin', 'staff', 'client']),  name="dispatch")
class PostUpdate(UpdateView):
    model = Post
    template_name = "main/post_edit.html"
    fields = ("title", "description")
    pk_url_kwarg = "pk"
    success_url = reverse_lazy("main")


# @method_decorator(login_required, name="dispatch")
@method_decorator(allowed_users(allowed_roles=['admin', 'staff', 'client']),  name="dispatch")
class PostDelete(DeleteView):
    model = Post
    success_url = reverse_lazy("main")
    # direct delete by pass confirmation page
    def get(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)
