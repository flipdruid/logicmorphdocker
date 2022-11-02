from app.models.profile import Profile

def currentuserprofile(request):
    # currentuser = request.user
    userprofile=""
    if request.user.is_authenticated:
        try:
            userprofile = Profile.objects.get(user=request.user)   
        except Profile.DoesNotExist:
            pass
    else:
        pass
    return {"userprofile": userprofile}