from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.core.exceptions import PermissionDenied
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from .models import Photo
from django.http import HttpResponseForbidden

# Create your views here.

class PhotoListView(ListView):
    model = Photo
    template_name = 'gallery/list.html'
    context_object_name = 'photos'

class PhotoDetailView(DetailView):
    model = Photo
    template_name = 'gallery/detail.html'
    context_object_name = 'photo'
    

class UploadView(LoginRequiredMixin, CreateView):
    model = Photo
    fields = ['title','description', 'image']
    template_name = 'gallery/upload.html'
    success_url = reverse_lazy('gallery:list')
    
    def form_valid(self,form):
        form.instance.uploader = self.request.user
        
        return super().form_valid(form)
    
class IsUploader(UserPassesTestMixin):
    
    def get_photo(self):
        return get_object_or_404(Photo, pk = self.kwargs.get('pk'))
    def test_func(self):
        if self.request.user.is_authenticated:
            return self.request.user == self.get_photo().uploader
        else:
            raise PermissionDenied("Dont Have Permissions")
            # return HttpResponseForbidden()
        
class PhotoDeleteView(IsUploader, DeleteView):
    template_name = 'gallery/delete.html'
    model = Photo
    success_url = reverse_lazy('gallery:list')