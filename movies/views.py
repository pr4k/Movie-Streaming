from django.shortcuts import render
from django.views.generic import FormView, ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView
from movies.models import Movie, Comment
from movies.forms import CommentForm

# Create your views here.
class MovieDetailsForm(CreateView):
    model = Movie
    fields = '__all__'
    success_url = '/movies'
class MovieDetailsUpdate(UpdateView):
    model = Movie
    fields = '__all__'
    template_name_suffix = '_update_form'
    success_url = '/movies'
    def get_object(self):
        return Movie.objects.get(id = self.kwargs['id'])

class MovieDetails(DetailView):
    def get_object(self):
        post = Movie.objects.get(id = self.kwargs['id'])
        return {'detail':post,'form':CommentForm,'comment':Comment.objects.filter(post = post)}
    template_name = 'movies/movie_details.html'
    query_set = Movie.objects.all()

class AllMovies(ListView):
    print("YEs")
    model = Movie

class CommentFormView(FormView):
    form_class = CommentForm
    success_url = '/movies'
    def form_valid(self,form):
        id = self.kwargs['id']
        print(self.request.user)
        form.instance.user = self.request.user
        form.instance.post = Movie.objects.get(id=id)
        form.save()
        return super().form_valid(form)
