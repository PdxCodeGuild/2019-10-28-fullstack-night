if ArtPieceUserFave == True:
    add URL to FaveList
    



def profile(request):
    user = request.user
    if user['theme'] == 'Dark':
        profile_css = "dark_style.css"

        if user['layout'] == "Type 1":
            profile_layout = "layoutstyle1.css"
        if user['layout'] == "Type 2":
            profile_layout = "layoutstyle2.css"
        if user['layout'] == "Type 3":
            profile_layout = "layoutstyle3.css"
    if user['theme'] == 'Light':
        profile_css = "light_style.css"

        if user['layout'] == "Type 1":
            profile_layout = "layoutstyle1.css"
        if user['layout'] == "Type 2":
            profile_layout = "layoutstyle2.css"
        if user['layout'] == "Type 3":
            profile_layout = "layoutstyle3.css"
    context = {'profile_css': profile_css, 'profile_layout': profile_layout, **kwargs}
    return HttpResponse(request, 'users/{username}/profile.html', context)
    

def profile(request):
    user = request.user
    username = user['username']
    if user['theme'] == 'Dark' && user['layout'] == "Type 1":
        profile_css = "dark_style1.css"
    if user['theme'] == 'Light' && user['layout'] == "Type 1":
        profile_css = "light_style1.css"
    if user['theme'] == 'Dark' && user['layout'] == "Type 2":
        profile_css = "dark_style2.css"
    if user['theme'] == 'Light' && user['layout'] == "Type 2":
        profile_css = "light_style2.css"
    if user['theme'] == 'Dark' && user['layout'] == "Type 3":
        profile_css = "dark_style3.css"
    if user['theme'] == 'Light' && user['layout'] == "Type 3":
        profile_css = "light_style3.css"

    context = {'profile_css': profile_css, **kwargs}
    return HttpResponse(request, 'users/{username}/profile.html', context)

'''
<link rel="stylesheet" href={% static 'cc/css/{{profile_css}}' %}">
'''

