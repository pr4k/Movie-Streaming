from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from django.shortcuts import render
from django.views.generic import FormView, ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView
from movies.models import Movie, Comment
from movies.forms import CommentForm
from django import template

register = template.Library()

# Create your views here.
class MovieDetailsForm(UserPassesTestMixin,CreateView):
    model = Movie
    fields = '__all__'
    success_url = '/movies'
    def test_func(self):
        return self.request.user.is_superuser
class MovieDetailsUpdate(UserPassesTestMixin,UpdateView):
    model = Movie
    fields = '__all__'
    template_name_suffix = '_update_form'
    success_url = '/movies'
    def get_object(self):
        return Movie.objects.get(id = self.kwargs['id'])

    def test_func(self):
        return self.request.user.is_superuser
class MovieDetails(LoginRequiredMixin,DetailView):
    def get_object(self):
        post = Movie.objects.get(id = self.kwargs['id'])
        return {'detail':post,'form':CommentForm,'comment':Comment.objects.filter(post = post)}
    template_name = 'movies/movie_details.html'
    query_set = Movie.objects.all()

class AllMovies(LoginRequiredMixin,ListView):
    print("YEs")
    model = Movie

class CommentFormView(LoginRequiredMixin,FormView):
    form_class = CommentForm
    success_url = '/movies'
    def form_valid(self,form):
        id = self.kwargs['id']
        print(self.request.user)
        form.instance.user = self.request.user
        form.instance.post = Movie.objects.get(id=id)
        form.save()
        return super().form_valid(form)
