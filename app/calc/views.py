from django.shortcuts import render

# Create your views here.
def home(request):
  return render(request, 'home.html', { 'name': 'Sai Krishna Reddy', 'title': 'Sai'})
