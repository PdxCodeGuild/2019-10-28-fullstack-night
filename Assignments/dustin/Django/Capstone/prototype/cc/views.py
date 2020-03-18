from django.shortcuts import render, reverse
from django.http import HttpResponse, HttpResponseRedirect
from .models import ArtPiece, ArtCollection, CollectionPiece
from users.models import Profile
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from itertools import chain

@login_required
def index(request):
    user = request.user.profile
    banner_image, standard_css, details_css, index_css, submit_css, profile_css = look_select(request)
    css_select = index_css
    banner_image = banner_image

    gallery = ArtPiece.objects.all()
    gallery2 = CollectionPiece.objects.all()
    pictures = sorted(chain(gallery, gallery2), key=lambda x:x.pub_date)
    print(gallery2)

    context = {
        'css_select': css_select,
        'banner_image': banner_image,
        'pictures': pictures,
        }
    return render(request, "cc/index.html", context)

@login_required
def details(request, pk, is_collectionpiece):
    # data = request.GET(pk=pk)
    # print(data)
    user = request.user.profile
    user2 = request.user
    banner_image, standard_css, details_css, index_css, submit_css, profile_css = look_select(request)
    css_select = details_css
    banner_image = banner_image
    associated_works = []
    if is_collectionpiece:
        mainpic = CollectionPiece.objects.get(pk=pk)
        pic_collection = mainpic.collection
        associated_works = CollectionPiece.objects.filter(collection=pic_collection)
        
    else:
        mainpic = ArtPiece.objects.get(pk=pk)

    gallery = user.user.artpiece_set.all() 
    gallery2 = user.user.collectionpiece_set.all()
    # print(gallery, gallery2)
    pictures = sorted(chain(gallery, gallery2), key=lambda x:x.pub_date)
    print(pictures)

    # other_works = 
    context = {
        'css_select': css_select,
        'banner_image': banner_image,
        'mainpic': mainpic,
        'pictures': pictures,
        'associated_works': associated_works,
        }
    return render(request, 'cc/details.html', context)

@login_required
def submitart(request):
    user = request.user.profile
    banner_image, standard_css, details_css, index_css, submit_css, profile_css = look_select(request)
    css_select = submit_css
    banner_image = banner_image
    context = {
        'css_select': css_select,
        'banner_image': banner_image,
        }
    return render(request, 'cc/submitart.html', context)

@login_required
def single_submission(request):
    data = request.POST
    print(data)
    user=request.user.profile
    files=request.FILES
    
    for file in files:
        image=ArtPiece(
            image=request.FILES.get(file),
            name=data['arttitle'],
            user=request.user,
            artist=user,
        )
        image.save()
    text=ArtPiece(
        text=data.get('tinyText1'),
        name=data['arttitle'],
    )
    text.save()
    return HttpResponseRedirect(reverse('users:profile'))

@login_required
def collection_submission(request):
    data = request.POST
    user=request.user.profile
    # print(request.POST)
    new_collection = ArtCollection(
            name=data['collectiontitle'],
            artist=user,
        )
    new_collection.save()

    files=request.FILES
    print(files)
    
    text_adds = [data.get('tinyText2'), data.get('tinyText3'), data.get('tinyText4'), data.get('tinyText5'), data.get('tinyText6'), data.get('tinyText7')]

    for file in files:
        image = CollectionPiece(
            image=request.FILES.get(file),
            collection=new_collection,
            user=request.user
        )
        image.save()

    for i in range(0, 6):
        if text_adds[i] != "":
            text = CollectionPiece(
                text=text_adds[i],
                collection=new_collection
            )
            text.save()

    return HttpResponseRedirect(reverse('users:profile'))


@login_required
def look_select(request):
    user = request.user.profile
    if user.theme.text == 'Light':
        banner_image = "CreativeCrossroadsGIFblue.gif"
        standard_css = "light_standard.css"
        details_css = "light_details.css"
        index_css = "light_index.css"
        submit_css = "light_submit.css"
        if user.layout.text == 'Type 1':
            profile_css = "light_profile1.css"
        if user.layout.text == 'Type 2':
            profile_css = "light_profile2.css"
        if user.layout.text == 'Type 3':
            profile_css = "light_profile3.css"
    else:
        banner_image = "CreativeCrossroadsGIFgreen4.gif"
        standard_css = "dark_standard.css"
        details_css = "dark_details.css"
        index_css = "dark_index.css"
        submit_css = "dark_submit.css"
        if user.layout.text == 'Type 2':
            profile_css = "dark_profile2.css"
        if user.layout.text == 'Type 3':
            profile_css = "dark_profile3.css"
        else:
            profile_css = "dark_profile1.css"
    return banner_image, standard_css, details_css, index_css, submit_css, profile_css

# @login_required
    # return render(request, 'users/profile.html', {})


# Create your views here.