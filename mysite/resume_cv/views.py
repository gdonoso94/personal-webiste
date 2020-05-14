from django.shortcuts import render
from django.views import generic
from django.http import HttpResponse
from . import utils
# Create your views here.


class Me(generic.View):
    template_name = 'me.html'

    def get(self, request):
        return render(request, self.template_name)

class GeneratePdf(generic.View):
    def get(self, request):
        pdf = utils.render_to_pdf('me_pdf.html')
        return HttpResponse(pdf, content_type='application/pdf')
