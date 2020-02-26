def custom_set(request, user_choice):
    if user_choice == "Layout 1":
        user = request.user;
        layout = user.get.object(data['layout'])
        layout = "css layout 1 url path"
        layout.save()
        return render(reverse("cc:accountsettings"))

    if user_choice == "Layout 2":
        user = request.user;
        layout = user.get.object(data['layout'])
        layout = "css layout 2 url path"
        layout.save()
        return render(reverse("cc:accountsettings"))

    if user_choice == "Layout 3":
        user = request.user;
        layout = user.get.object(data['layout'])
        layout = "css layout 3 url path"
        layout.save()
        return render(reverse("cc:accountsettings"))
