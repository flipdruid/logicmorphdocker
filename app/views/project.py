from django.views.generic import CreateView, ListView, UpdateView, DeleteView, TemplateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from accounts.decorators import allowed_users
from django.urls import reverse_lazy
from app.models.project import Project
from app.models.profile import Profile
from app.models.client import Client
from django.shortcuts import reverse
from app.context.context_processors import currentuserprofileclient as pc
from django.core.paginator import Paginator
from django.db.models import Q


@method_decorator(login_required, name="dispatch")
class CreateProjectClient(CreateView):
    model = Project
    template_name = "main/project_create.html"
    fields = ("name",)
    success_url = reverse_lazy("list_client_project")
    
    def form_valid(self, form):
        cprof = Profile.objects.get(user=self.request.user)
        ccli = Client.objects.get(profile=cprof)
        form.instance.client = ccli
        return super(CreateProjectClient, self).form_valid(form)

@method_decorator(login_required, name="dispatch")
@method_decorator(allowed_users(allowed_roles=['admin', 'staff']),  name="dispatch")
class CreateProject(CreateView):
    model = Project
    template_name = "main/project_create.html"
    fields = ("name","client",)
    success_url = reverse_lazy("list_project")
    

@method_decorator(login_required, name="dispatch")
@method_decorator(allowed_users(allowed_roles=['admin', 'staff']),  name="dispatch")
class ListProject(ListView):
    model = Project
    paginate_by = 9
    template_name = "main/project_lists.html"
    fields = ("name", "state","client","created_at", "updated_at")
    context_object_name = "projects"

@method_decorator(login_required, name="dispatch")
class ListClientProject(ListView):
    queryset = Project.objects.all()
    paginate_by = 9
    template_name = "main/project_lists.html"
    context_object_name = "projects"

    def get_queryset(self):
        queryset = super(ListClientProject, self).get_queryset()
        client = Client.objects.get(profile=self.request.user.profile_user.all()[0])
        return queryset.filter(client=client)
    
@method_decorator(login_required, name="dispatch")
class ClientProjectUpdate(UpdateView):
    model               =   Project
    template_name       =   'main/project_update.html'
    fields              =   ("name",)
    pk_url_kwarg        =   'pk'
    context_object_name =   "projects"
    success_url         =   reverse_lazy('list_client_project')


class ClientProjectDelete(DeleteView):    
    model               =   Project        

    # direct delete by pass confirmation page
    def get(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)


    def get_success_url(self):
        if self.request.user.is_superuser or self.request.user.is_staff:
            return reverse('list_project')
        else:
            return reverse('list_client_project')