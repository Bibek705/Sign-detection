import random
import time
import string
from django.http import JsonResponse
from agora_token_builder import RtcTokenBuilder
from .models import usersModel

def createRoomID():
    letters = string.ascii_lowercase
    roomID = ''.join(random.choice(letters) for i in range(6))
    return roomID

'''def saveRoom(id,name):
    roomIDModel.objects.create(roomid=id, createdBy=name)

def checkForRoom(id):
    return roomIDModel.objects.filter(roomid=id).count()
'''

def createRoomToken(request):
    channel = request.GET.get('userName')
    member = request.GET.get('room')
    appId = '1f3c5f4a522a49f6aa8e7b2b3b3c21a8'
    appCertificate='4a227d13fe624dfc9dfe3b473e6948e7'
    if channel=='':
        while True:
            channelName=createRoomID()
            if usersModel.objects.filter(channel=channelName).count()==0:
                break
    else:
        channelName=channel
    uid=random.randint(1,230)
    role=1
    expirationTimeInSec=3600*6
    currentTime=time.time()
    privilegeExpiredTs=currentTime+expirationTimeInSec
    token = RtcTokenBuilder.buildTokenWithUid(appId, appCertificate, channelName, uid, role, privilegeExpiredTs)
    usersModel.objects.create(channel=channelName, uid=uid, name=member, role=role)
    return JsonResponse({'token':token,'uid':uid,'channel':channelName, 'user':member},safe=False)


def getmember(request):
    uid = request.GET.get('UID')
    room_name = request.GET.get('room_name')

    member = usersModel.objects.get(
        uid=uid,
        channel=room_name,
    )
    name = member.name
    return JsonResponse({'name': member.name}, safe=False)
