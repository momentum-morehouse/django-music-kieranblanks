from django.shortcuts import render
from .models import Album
from .forms import CommentForm

# Create your views here.
def list_albums(request):
    albums = Album.objects.all()
    if request.method == 'GET':
        form = CommentForm()
    else:
        form = CommentForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect(to='list_albums')

    return render(request, "albums/list_albums.html", {"form": form})
    return render(request, "albums/list_albums.html",
                  {"albums": albums})


    