from django.shortcuts import render

# Create your views here.
def home(request):
  return render(request, 'home.html', { 'name': 'Sai Krishna Reddy', 'title': 'Sai'})

def add(request):
  val1 = int(request.GET['num1'])
  val2 = int(request.GET['num2'])
  res = val1 + val2
  return render(request, 'result.html', { 'res': res})
