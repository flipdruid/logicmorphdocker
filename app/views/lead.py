from django.forms.models import model_to_dict
from app.models.project import Project
import celery
import email
from django.contrib.sites.models import Site
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, reverse, get_object_or_404
from django.http import JsonResponse
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from accounts.decorators import allowed_users
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView, TemplateView
from django.urls import reverse_lazy
from django.core.exceptions import ObjectDoesNotExist
from accounts.models.user import User
from app.models.profile import Profile
from app.models.lead import Lead
from app.models.reglink import Reglink
from accounts.forms import UserForm, UserUpdateForm, UserFormNoEmail, UserViewForm
from app.models.client import Client
from app.forms.profile import ProfileUpdateForm, ProfileViewForm, ProfileViewClient
from app.forms.client import ClientForm
from accounts.models.user import User
from django.contrib.auth.models import Group

import random

class LeadCreate(CreateView):
    model = Lead
    template_name = "main/contact_us_mail.html"
    fields = ("first_name", "last_name","email","entity_name", "details")
    # success_url = reverse_lazy("main")
    def get_success_url(self):
        if self.request.user.is_superuser or self.request.user.is_staff:
            return reverse('lead_mail_lists')
        else:
            return reverse('main')



# @method_decorator(login_required, name="dispatch")
@method_decorator(allowed_users(allowed_roles=['admin', 'staff']),  name="dispatch")
class LeadMailList(ListView):
    model = Lead
    paginate_by = 9
    template_name = "main/lead_mail_lists.html"
    fields = ("first_name", "last_name","email","entity_name", "details")
    context_object_name = "leads"

    def get_context_data(self, **kwargs):
        context         =    super(LeadMailList, self).get_context_data(**kwargs)
        leads = Lead.objects.all()
        lead_list = {}
        profile_img=""
        for lead in leads:
            try:
                userExist = User.objects.get(email=lead.email)
                profile_img = Profile.objects.get(user=userExist)
                
                lead_list[lead.id] = {
                    'state': lead.state,
                    'ids':lead.id,
                    'first_name':lead.first_name,
                    'last_name':lead.last_name,
                    'email':lead.email,
                    'entity_name':lead.entity_name,
                    'details':lead.details,
                    'created_at': lead.created_at,
                    'updated_at':lead.updated_at,
                    "profile_img": profile_img.avatar,
                }

            except ObjectDoesNotExist:               

                lead_list[lead.id] = {
                    'state': lead.state,
                    'ids':lead.id,
                    'first_name':lead.first_name,
                    'last_name':lead.last_name,
                    'email':lead.email,
                    'entity_name':lead.entity_name,
                    'details':lead.details,
                    'created_at': lead.created_at,
                    'updated_at':lead.updated_at,
                    "profile_img": 'avatar/guesticon2.jpg',
                }

        context['leads']     =    lead_list       
        return context

# @method_decorator(login_required, name="dispatch")
@method_decorator(allowed_users(allowed_roles=['admin', 'staff']),  name="dispatch")
class LeadMailView(DetailView):
    model = Lead
    template_name       =   'main/lead_mail_view.html'
    pk_url_kwarg        =   'pk'
    context_object_name =   'lead'
    
    def get_context_data(self, **kwargs):
        context         =    super(LeadMailView, self).get_context_data(**kwargs)
        currentObject    =    Lead.objects.get(id=self.kwargs['pk'])
        if currentObject.state=="new":
            currentObject.viewed()
            currentObject.save()       
        context['lead']     =  currentObject
        return context


    

# @method_decorator(login_required, name="dispatch")
@method_decorator(allowed_users(allowed_roles=['admin', 'staff']),  name="dispatch")
class LeadMailViewLead(DetailView):
    model = Lead
    template_name       =   'main/lead_mail_view_lead.html'
    pk_url_kwarg        =   'pk'
    context_object_name =   'lead'

    def get_context_data(self, **kwargs):
        context         =    super(LeadMailViewLead, self).get_context_data(**kwargs)
        currentObject    =    Lead.objects.get(id=self.kwargs['pk'])
        if currentObject.state=="new":
            currentObject.viewed()
            currentObject.save()       
        context['lead']     =  currentObject
        return context


    

@method_decorator(login_required, name="dispatch")
class LeadMailDelete(DeleteView):
    model = Lead        
    # template_name       =   'main/lead_mail_confirm_delete.html'        
    # pk_url_kwarg        =   'pk'
    success_url = reverse_lazy("lead_mail_lists")
    # context_object_name =   'lead'

    def get(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)


# @method_decorator(login_required, name="dispatch")
@method_decorator(allowed_users(allowed_roles=['admin', 'staff']),  name="dispatch")
class LeadToClient(DetailView):
    model = Lead
    template_name       =   'main/lead_client.html'
    pk_url_kwarg        =   'pk'
    context_object_name =   'lead'

    # def get_context_data(self, **kwargs):
    #     context         =    super(LeadToClient, self).get_context_data(**kwargs)
    #     currentObject    =    Lead.objects.get(id=self.kwargs['pk'])
        
    #     context['lead_mails']     =    Lead.objects.all().filter(email=currentObject.email)        
    #     context['show_convert']     =  User.objects.filter(email=currentObject.email)
    #     return context
    def get_context_data(self, **kwargs):
        context         =    super(LeadToClient, self).get_context_data(**kwargs)
        currentObject    =    Lead.objects.get(id=self.kwargs['pk'])
        leadInfo = {}
        if User.objects.filter(email=currentObject.email).count()>0:
            userInfo = User.objects.get(email=currentObject.email)
            profileInfo = Profile.objects.get(user=userInfo)
            leadInfo = {
                'show_convert': True,
                'profile_img' : profileInfo.avatar,
                'fname':userInfo.first_name,
                'lname':userInfo.last_name,
                'email':userInfo.email
            }

        else:

            leadInfo = {
                'show_convert': False,
                'profile_img' : "avatar/default-lead-avatar.png",
                'fname':currentObject.first_name,
                'lname':currentObject.last_name,
                'email':currentObject.email
            }

        context['lead_mails']   =    Lead.objects.all().filter(email=currentObject.email)        
        context['leadInfo']     =  leadInfo
        return context



# @login_required()
@allowed_users(allowed_roles=['admin', 'staff'])
def createreglink(request,lead_id):
    try:
        currentLead =  Lead.objects.get(pk=lead_id)
        emailExist = Reglink.objects.get(lead_mail=currentLead.email)

        if emailExist.lead_mail==currentLead.email:
            celery.current_app.send_task(
            "app.tasks.leadtoclient_sendreglink.sendreglink", args=(str(emailExist.id),))    
    
    except ObjectDoesNotExist:
        chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
        randomstr = "".join((random.choice(chars)) for x in range(30))
        if Reglink.objects.filter(lead_reglink=randomstr).count()>0:
                    randomstr = ""
                    chars = "9876543210zyxwvutsrqponmlkjihgfedcbaZYXWVUTSRQPONMLKJIHGFEDCBA"
                    randomstr = "".join((random.choice(chars)) for x in range(30))

        reglink =   Reglink.objects.create(
                    lead_id=currentLead.id,
                    lead_firstname=currentLead.first_name,
                    lead_lastname=currentLead.last_name,
                    lead_mail=currentLead.email,
                    lead_reglink=randomstr,
                    )
        reglink.save()
        getNewRegLink = Reglink.objects.get(lead_mail=currentLead.email)
        celery.current_app.send_task(
            "app.tasks.leadtoclient_sendreglink.sendreglink", args=(str(getNewRegLink.id),))  

    return HttpResponseRedirect(reverse('lead_client', args=(str(lead_id),)))

# @login_required(login_url= '/accounts/login')
def leadactivation(request, reglink):
    regForm = UserFormNoEmail()
    currentReglink =   Reglink.objects.get(lead_reglink=reglink)
    regForm=UserFormNoEmail(initial={'email': str(currentReglink.lead_mail),
                                'first_name': str(currentReglink.lead_firstname), 
                                'last_name': str(currentReglink.lead_lastname)}, auto_id=False)
    # regForm.fields['email'].disabled = True
                                
    if request.method == 'POST':
        regForm=UserFormNoEmail(request.POST)
        regFormEmail = regForm['email'].value()
        if regForm.is_valid():
            user = regForm.save()
            group = Group.objects.get(name='client')
            user.groups.add(group)           

            profileUser=User.objects.get(email=regFormEmail)
            userProfile = Profile.objects.create(user = profileUser )
            userProfile.save()

            clientProfile = Profile.objects.get(user=profileUser)
            clientProfileCreate = Client.objects.create(profile=clientProfile)
            clientProfileCreate.save()
            return HttpResponseRedirect(reverse('accounts:login'))

    context ={"regForm":regForm, 'leadmail':str(currentReglink.lead_mail)}    
    return render(request, 'main/lead_regform.html', context)

# @login_required()
@allowed_users(allowed_roles=['admin', 'staff', 'client'])
def userprofile(request):

    currentUser = request.user    
    currentProfile = Profile.objects.get(user=currentUser)

    if request.user.is_superuser:
        profileform = ProfileUpdateForm(initial={
            "avatar" : currentProfile.avatar,
            # "is_logicmorph_staff":currentProfile.is_logicmorph_staff,
            # "is_dark_theme":currentProfile.is_dark_theme
        },  auto_id=False)

    else:
        profileform = ProfileViewClient
    # Update user form (username, fname, lname) -- START
    userform = UserUpdateForm(initial ={
        'username': currentUser.username,
        'first_name': currentUser.first_name,
        'last_name':currentUser.last_name
    })    
    if request.method == 'POST': 
        userform=UserUpdateForm(request.POST, instance=request.user)
        if userform.is_valid():
            userform.save(commit=False)
            currentU = User.objects.get(id=currentUser.id)
            currentU.first_name=userform.cleaned_data['first_name']
            currentU.last_name=userform.cleaned_data['last_name']
            currentU.save()

        profileform=ProfileUpdateForm(request.POST,  request.FILES, instance=currentProfile)
        if profileform.is_valid():
            profileform.save()
            return HttpResponseRedirect(reverse('user_profile'))
        
    # Update user form (username, fname, lname) -- END

    context ={"userform":userform, 'currentProf':currentProfile, 'currentUser':currentUser, 'profileform': profileform}

    return render(request, 'main/userprofile.html', context)


@allowed_users(allowed_roles=['admin'])
def userprofileadminupdate(request,pk):

    getUser = User.objects.get(id=pk)
    getProfile = Profile.objects.get(user=getUser)

    userform = UserViewForm(initial ={
        'username': getUser.username,
        'first_name': getUser.first_name,
        'last_name':getUser.last_name
    })    

    profileform = ProfileViewForm(initial={
        "avatar" : getProfile.avatar,
        "is_logicmorph_staff":getProfile.is_logicmorph_staff,
        "is_dark_theme":getProfile.is_dark_theme
    },  auto_id=False)

    if request.method=='POST':
        profileform=ProfileViewForm(request.POST, request.FILES, instance=getProfile)
        if profileform.is_valid():
            profileform.save()
            return HttpResponseRedirect(reverse('user_profile_adminupdate', args=(getUser.id,)))

    context = {
        'userform':userform,
        'profileform': profileform,
        'profileinfo':getProfile,
        'userinfo': {
                "first_name" : getUser.first_name,
                "last_name" : getUser.last_name
                }
    }

    return render(request, 'main/userprofile_adminupdate.html', context)
    


@allowed_users(allowed_roles=['admin'])
def currentusers(request):
    currentGroups = Group.objects.values('name')
    currentUsers= User.objects.all()
    context ={
        'currentGroups':currentGroups,
        'currentUsers': currentUsers
    }

    return render(request, 'main/users_list.html', context)

@allowed_users(allowed_roles=['admin'])
def usergroupchange(request):
    changeStatus =""
    if request.method == 'POST':
        userID = request.POST['currentid']
        userGroup = request.POST['getselectvalue']
        requestedgroup = Group.objects.get(name=userGroup)
        currentuser = User.objects.get(id=userID)
        currentUserGroup = currentuser.groups.all()[0].name
        

        if userGroup != currentUserGroup:
            currentuser.groups.clear()
            currentuser.groups.add(requestedgroup)            
            print("Successfully save changes " + currentUserGroup + " to " + userGroup)
            changeStatus = "successfully save changes"
        else:
            print("save changes Failed " + currentUserGroup + " to " + userGroup)   
            changeStatus = "save changes failed"        
        
    return JsonResponse({'changeStatus':changeStatus})
    
    
