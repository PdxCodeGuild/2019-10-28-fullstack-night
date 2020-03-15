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


<!DOCTYPE html>
<html>
<head>
  <script src="https://cdn.tiny.cloud/1/65swt83e2hue73atee8ca0za53571esn30vu7s7b1r35anva/tinymce/5/tinymce.min.js" referrerpolicy="origin"></script>
</head>
<body>
  <textarea>
    Welcome to TinyMCE!
  </textarea>
  <script>
    tinymce.init({
      selector: 'textarea',
      plugins: 'a11ychecker advcode casechange formatpainter linkchecker autolink lists checklist media mediaembed pageembed permanentpen powerpaste table advtable tinycomments tinymcespellchecker',
      toolbar: 'a11ycheck addcomment showcomments casechange checklist code formatpainter pageembed permanentpen table',
      toolbar_mode: 'floating',
      tinycomments_mode: 'embedded',
      tinycomments_author: 'Author name'
    });
  </script>
</body>
</html>