from django.shortcuts import render

# create views here

def home_page(request):
    return render(request,'index.html',{"title: Home"})