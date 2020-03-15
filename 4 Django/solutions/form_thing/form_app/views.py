from django.shortcuts import render

def index(request):
    if request.method == "POST":
        if request.POST['hidden-input'] == '1':
            print(f'box one says {request.POST["stuff"]}')
        elif request.POST['hidden-input'] == '2':
            print(f'box two says {request.POST["stuff"]}')
    return  render(request, 'form_app/index.html', {})

# Create your views here.
