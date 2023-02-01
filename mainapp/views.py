from django.shortcuts import render, redirect
from .functions import createRoomToken


# Create your views here.
def get_token(request):
    return createRoomToken(request)

def createOrJoinRoom(request):
    context={}
    return render(request, 'createRoom.html', context)

def getintoRoom(request):
    return render(request,'room.html',{})
