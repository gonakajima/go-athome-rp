from django.shortcuts import render

def signup(request):
    return render(request, '../hello/templates/signup.html')
