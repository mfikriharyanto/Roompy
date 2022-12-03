from django.shortcuts import render
from user.models import UserManager
from django.http import JsonResponse
import json

# Create your views here.

def edit_user(request, user_id, details):
    try:
        name, about = parse_details(details)
        UserManager.edit_user(user_id, name, about)
    except:
        show_failure_notif("Gagal menyimpan perubahan. Mohon dicoba kembali beberapa saat lagi.")

def show_failure_notif(args):
    return JsonResponse({'status':'false', 'message':args}, status=400)

def parse_details(details):
    res = json.loads(details)
    return res['name'], res['about']