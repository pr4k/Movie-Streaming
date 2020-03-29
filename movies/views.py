from django.shortcuts import render
from django.views.generic import FormView, ListView, DetailView
from movies.models import Movie, Comment
from movies.forms import CommentForm

# Create your views here.
class MovieDetails(DetailView):
    def get_object(self):
        print(self.kwargs)
        print(self.request)
        print("yes")
        print(Movie.objects.all())

        return {'checl':Movie.objects.get(id=2),'form':CommentForm}
    template_name = 'movies/movie_list.html'
    query_set = Movie.objects.all()

class AllMovies(ListView):
    print("YEs")
    model = Movie

class CommentFormView(FormView):
    form_class = CommentForm
    success_url = '/hello'
