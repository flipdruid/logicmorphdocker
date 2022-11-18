from app.models.profile import Profile
from app.models.client import Client
from django.core.exceptions import ObjectDoesNotExist

def currentuserprofileclient(request):
    userprofile=""
    profileclient=""
    if request.user.is_authenticated:
        try:
            
            userprofile = Profile.objects.get(user=request.user)
            profileclient = Client.objects.get(profile=userprofile)
        # except Profile.DoesNotExist:
        #     pass
        except ObjectDoesNotExist:
            pass
    else:
        pass
    return {"userprofile": userprofile, "profileclient": profileclient}