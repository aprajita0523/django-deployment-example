from django.shortcuts import render
#from django.views.generic import View
#from django.http import HttpResponse
#from django.views.generic import View,TemplateView
from django.views.generic import View,TemplateView,ListView,DetailView
from basic_app import models

# Create your views here.
'''def index(request):
    return render(request,'index.html')'''


'''class CBView(View):
    def get(self,request):
        return HttpResponse("class based views are cool")'''

'''class IndexView(TemplateView):
     template_name = 'index.html'''

class IndexView(TemplateView):
     template_name = 'index.html'

     def get_context_data(self,**kwargs):
         context = super().get_context_data(**kwargs)
         context['injectme'] = 'hi this is Basic Injection!'
         return context

class SchoolListView(ListView):
    context_object_name ='schools'
    model = models.School

class SchoolDetailView(DetailView):
    model = models.School
    context_object_name ='school_detail'
    template_name = 'basic_app/school_details.html'
