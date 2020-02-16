from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import NumGroup

def group(request, pk):
    numgroup = NumGroup.objects.get(pk=pk)
    if request.user != numgroup.user:
        return HttpResponseRedirect('http://google.com')
    nums = numgroup.nums.all()
    return HttpResponse(numgroup.name + ' ' +str([num.val for num in nums]))

@login_required
def index(request):
    if request.method == 'POST':
        new_group = NumGroup(name=request.POST['name'], user=request.user)
        new_group.save()
    user_groups = request.user.numgroups.all()
    return render(request, 'nums/index.html', {'groups': user_groups})
# Create your views here.
