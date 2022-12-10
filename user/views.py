from django.shortcuts import render
from user.forms import ProfileForm
from django.http import JsonResponse, HttpResponseRedirect
from user.models import UserManager
import json

def top_users(request):
    return render(request, "top_users.html")

def get_user(request, pk):
    if request.method == 'GET':
        user = UserManager.get_user(pk)
        if user == None:
            return HttpResponseRedirect(request.path_info)
        context = {
            'user': user
        }
        
    return render(request, 'profile.html', context)

def edit_user(request, pk):
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            try:
                form.save()
            except:
                return show_failure_notif("Gagal menyimpan perubahan. Mohon dicoba kembali beberapa saat lagi.")
            return HttpResponseRedirect(request.path_info)
    else:
        form = ProfileForm()
        user = UserManager.get_user(pk)
        if user == None:
            return HttpResponseRedirect(request.path_info)
        context = {
            'user': user,
            'form':form
        }
    return render(request, 'profile_form.html', context)

def show_failure_notif(args):
    return JsonResponse({'status':'false', 'message':args}, status=400)