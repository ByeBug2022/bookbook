from django.shortcuts import render

# Create your views here.
from hello.models import Person
# Create your views here.
def index(request):
    person = Person.objects.get(name='test')
    params = {'name':person.name}
    return render(request,'index.html',params)