from django.shortcuts import render
from django.views import generic
from django.http import HttpResponseRedirect


class LandingPage(generic.View):
    template_name = 'index.html'

    def get(self, request):
        return render(request, self.template_name)

class PersonalBlog(generic.View):
    personal_blog = "https://unamotoyunbambu.wordpress.com"

    def get(self, request):
        return HttpResponseRedirect(self.personal_blog)
