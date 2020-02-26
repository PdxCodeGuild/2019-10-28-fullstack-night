def vote_up(request):
    data = request.POST
    votes = data['votes']
    votes += 1
    votes.save()
    #look for active refresh in JS after function runs and updates that field
    return render(request, artdetail.html, {'votes' = votes})

def vote_down(request):
    data = request.POST
    votes = data['votes']
    votes -= 1
    votes.save()
    #look for active refresh in JS after function runs and updates that field
    return render(request, artdetail.html, {'votes' = votes})