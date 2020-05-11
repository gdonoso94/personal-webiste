from django.shortcuts import render
from django.views import generic
from django.http import HttpResponse

# Create your views here.
class Me(generic.View):
    template_name = 'me.html'

    def get(self, request):
          return render(request, self.template_name)