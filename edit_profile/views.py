from django.shortcuts import render
from user.models import UserManager
from edit_profile.forms import ProfileForm
from django.http import JsonResponse, HttpResponseRedirect
import json

# Create your views here.

def edit_user(request, user_id, details):
    if request.method == 'POST':
        form = ProfileForm(request.POST)
        if form.is_valid():
            try:
                name, about = parse_details(details)
                UserManager.edit_user(user_id, name, about)
            except:
                return show_failure_notif("Gagal menyimpan perubahan. Mohon dicoba kembali beberapa saat lagi.")
            return HttpResponseRedirect(request.path_info)
        return
    else:
        form = ProfileForm()
    return render(request, 'edit_profile.html', {'form':form})

def show_failure_notif(args):
    return JsonResponse({'status':'false', 'message':args}, status=400)

def parse_details(details):
    res = json.loads(details)
    return res['name'], res['about']