# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from forms import LoginForm
from models import SignUpModel, SessionModel
from datetime import datetime, timedelta
from django.contrib.auth.hashers import make_password, check_password
import ctypes

# Create your views here.
# password = make_password('@rocket')
# user = SignUpModel(username='rocket', email='hunt97@rocketmail.com', password=password)
# user.save()


# login view to display at the time of login or sign in
def login_view(request):
    date = datetime.now()
    # password = make_password('@rocket')
    # user = SignUpModel(username='rocket', email='hunt97@rocketmail.com', password=password)
    # user.save()
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = SignUpModel.objects.filter(username=username).first()
            if user:
                # check for the password
                if check_password(password, user.password):
                    token = SessionModel(user=user)
                    token.create_token()
                    token.save()
                    response = redirect('/room/')
                    response.set_cookie(key='session_token', value=token.session_token)
                    return response
                else:
                    print("Incorrect Username or Password")
                    ctypes.windll.user32.MessageBoxW(0, u"Incorrect Username or Password", u"Error", 0)
                    return render(request, 'index.html', {'invalid': True})
            else:
                print ("User does not exist")
                ctypes.windll.user32.MessageBoxW(0, u"User does not exist.Please sign up", u"Error", 0)
                return render(request, 'index.html', {'invalid': True})
        else:
            print ("Error: Invalid form")
            ctypes.windll.user32.MessageBoxW(0, u"Invalid form entries.Enter again", u"Error", 0)
    else:
        form = LoginForm()
    return render(request, 'index.html', {'form': form}, {'Date': date})


# def create_room(request):
#     if request.method == "POST":
#         form = RoomForm(request.POST)
#         if form.is_valid():
#             room = form.cleaned_data['room']
#             if len(room) > 0:
#                 room_info = RoomModel(room=room)
#                 room_info.save()
#             else:
#                 print 'Too short name for a room'
#                 ctypes.windll.user32.MessageBoxW(0, u"Too short name for a room. please try again", u"Error", 0)
#                 form = RoomForm()
#         else:
#             print 'form seems to be invalid'
#             ctypes.windll.user32.MessageBoxW(0, u"form seems to be invalid. please try again", u"Error", 0)
#             form = RoomForm()
#     else:
#         form = RoomForm()
#     return render(request, 'index.html', {'form': form})
#
#
# def create_devices(request):
#     if request.method == "POST":
#         form = ToggleForm(request.POST)
#         if form.is_valid():
#             device = form.cleaned_data['device']
#             if len(device) > 0:
#                 device_info = ToggleForm(device=device)
#                 device_info.save()
#             else:
#                 print 'Too short name for a room'
#                 ctypes.windll.user32.MessageBoxW(0, u"Too short name for a room. please try again", u"Error", 0)
#                 form = ToggleForm()
#         else:
#             print 'form seems to be invalid'
#             ctypes.windll.user32.MessageBoxW(0, u"form seems to be invalid. please try again", u"Error", 0)
#             form = ToggleForm()
#     else:
#         form = ToggleForm()
#     return render(request, 'index.html', {'form': form})
