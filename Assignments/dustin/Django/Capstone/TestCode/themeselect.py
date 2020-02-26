def theme_select(request, user_choice):
    if user_choice == "Theme Dark":
        user = request.user
        data = request.POST
        theme = theme.object.get(data['theme'])
        theme = "Dark theme css file"
        theme.save
        return render(reverse('cc:accountsettings'))



    if user_choice == "Theme Light":
        user = request.user
        data = request.POST
        theme = theme.object.get(data['theme'])
        theme = "Light theme css file"
        theme.save
        return render(reverse('cc:accountsettings'))


    if user_choice == "Theme Monochrome":
        user = request.user
        data = request.POST
        theme = theme.object.get(data['theme'])
        theme = "Monochrome theme css file"
        theme.save
        return render(reverse('cc:accountsettings'))


    if user_choice == "Theme Hi-Contrast"
    user = request.user
        data = request.POST
        theme = theme.object.get(data['theme'])
        theme = "Hi-Contrast theme css file"
        theme.save
        return render(reverse('cc:accountsettings'))