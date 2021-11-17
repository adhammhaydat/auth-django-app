from django.shortcuts import render
from .models import Snack
from django.urls import reverse_lazy
from django.views.generic import (ListView,
                                    DeleteView,
                                    DetailView,
                                    UpdateView,
                                    CreateView)
# Create your views here.

class SnackListView(ListView):
    model = Snack
    template_name = "pages/list_view.html"
    


class SnackDetailView(DetailView):
    model = Snack
    template_name = "pages/snack_detail.html"
    context_object_name = "snack_object"

class SnackCreateView(CreateView):
    model = Snack
    template_name = "pages/snack_create.html"
    fields =["title", "description",'purshers']


class SnackUpdateView(UpdateView):
    model = Snack
    template_name = "pages/snack_update.html" 
    fields =["title", "description"]

class SnackDeleteView(DeleteView):
    model = Snack
    template_name = "pages/snack_delete.html"
    success_url = reverse_lazy("snack_view")

               