from django.shortcuts import render
from . import models
#from django.contrib import messages


def index(request):
    model1 = models.Uploadmyfiles.objects.all()
    #file1 = model1[(len(model1)-1)].upload_file
    #print(file1)
    print('hi')
    #print(file1.url)
    print('hello')
    return render(request, 'index.html')

'''def manage_file_upload(f):
    with open('media/uploadedfolder/' + f.name, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
        #destination.write('hey aprajita')'''
# Create your views here.
def uploadfile(request):
    print('hey i am working')
    print(request.FILES)
    file1 = request.FILES['myfile1']
    file2 = request.FILES['myfile2']

    print(file1.name)
    print(file2.name)
    model = models.Uploadmyfiles(upload_file = file1)
    model.save()
    model = models.Uploadmyfiles(upload_file = file2)
    model.save()
    var = request.POST['actionrequired']
    print(var)
    #manage_file_upload(request.FILES['myfile'])
    #messages.info(request, 'Your password has been changed successfully!')
    return render(request, 'index.html',{'model':models.Uploadmyfiles.objects.all()})
    #return render(request, 'index.html',{'model':'file1'})
