from django.shortcuts import render

def trending_rooms(request):
  return render(request, "trending_rooms.html")