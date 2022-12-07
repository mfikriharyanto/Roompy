from django.shortcuts import render

def top_users(request):
  return render(request, "top_users.html")