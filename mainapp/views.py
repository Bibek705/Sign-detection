from django.shortcuts import render, redirect
from .functions import createRoomToken, getmember

# Create your views here.
def create_token(request):
    return createRoomToken(request)


def getMember(request):
    return getmember(request)

def createOrJoinRoom(request):
    context={}
    return render(request, 'createRoom.html', context)

def getintoRoom(request):
    return render(request,'room.html',{})
