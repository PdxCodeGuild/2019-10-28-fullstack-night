from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render, reverse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import PostGroup, ProfileMusicChoice
from signup_part2.models import UserDetails
from signup_part3.models import UserCredit
from signup_part4.models import UserNetflix
from signup_part5.models import UserSecrets
from signup_part6.models import UserDob
import json
import random

@login_required
def index(request):
    if request.method == 'POST':
        new_post = PostGroup(body=request.POST['body'], user=request.user)
        new_post.save()
        return HttpResponseRedirect(reverse('myspace:index'))
    user_posts = request.user.postgroup_set.all()
    context = {"user_posts": user_posts}
    return render(request, 'myspace_pages/myspace_pages.html', context)

def myspace_pages_vue(request):
    outlist = []
    for postgroup in PostGroup.objects.filter(user=request.user):
        one_user = {
            "user": postgroup.user.username,
            "body": postgroup.body,
            "id": postgroup.id,
            }
        outlist.append(one_user)
    users_names = [user for user in User.objects.all()]
    your_friend = random.choice(users_names)
    friend_pic = your_friend.userprofile.profile_pic.image
    print(your_friend.userprofile.profile_pic.image)
    # return render(request, 'myspace_pages/myspace_pages_vue.html', {"your_friend":your_friend})
    context = {
        'postgroup_send': outlist,
        # Does this need to be user_posts ?? 
        # Does .text need to be .body ??
        'submit_to': reverse('myspace:vue_submit'),
        # 'user': request.user,
        'profile_pic': request.user.userprofile.profile_pic.image.url,
        'user_details': UserDetails.objects.get(user=request.user),
        'user_credit': UserCredit.objects.get(user=request.user),
        'user_netflix': UserNetflix.objects.get(user=request.user),
        'user_secrets': UserSecrets.objects.get(user=request.user),
        'user_dob': UserDob.objects.get(user=request.user),
        "your_friend": your_friend,
        "friend_pic": friend_pic,
        "profile_music": ProfileMusicChoice.objects.all(),
    }
    print(context)
    return render(request, 'myspace_pages/myspace_pages_vue.html', context)

def vue_submit(request):
    data = json.loads(request.body)
    PostGroup(
        body=data['text'],
        user=request.user,
        ).save()
    outlist = []
    for postgroup in PostGroup.objects.filter(user=request.user):
        one_user = {
            "user": postgroup.user.username,
            "body": postgroup.body,
            "id": postgroup.id,
            }
        outlist.append(one_user)
    context = {
        # 'postgroup_send': [postgroup.body for postgroup in PostGroup.objects.all()],
        'postgroup_send': outlist
    }
    return JsonResponse(context)
    

# Create your views here.
