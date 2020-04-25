from django.shortcuts import render
from show.models import Data
def index(request):
    # first = First.objects.values('subject').distinct()
    # second = Second.objects.values('subject').distinct()
    # third = Third.objects.values('subject').distinct()
    # fourth = Fourth.objects.values('subject').distinct()
    # fifth = Fifth.objects.values('subject').distinct()
    # sixth = Sixth.objects.values('subject').distinct()
    # param = {'1st':first,'2nd':second,'3rd':third,'4th':fourth,'5th':fifth,'6th':sixth}

    data = Data.objects.values('subject').distinct()
    param = {'data':data}
    return render(request,'notes/index.html',param)

def search(request):
    s = request.GET.get('search')
    search = Data.objects.filter(subject__istartswith=s).values('subject').distinct()
    param = {'data':search}
    return render(request,'notes/index.html',param)

    
    