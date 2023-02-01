import random
import time
import string
from django.http import JsonResponse
from agora_token_builder import RtcTokenBuilder

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
    userName = request.GET.get('userName')
    appId = '1f3c5f4a522a49f6aa8e7b2b3b3c21a8'
    appCertificate='4a227d13fe624dfc9dfe3b473e6948e7'
    channelName=createRoomID()
    uid=random.randint(1,230)
    role=1
    expirationTimeInSec=3600*6
    currentTime=time.time()
    privilegeExpiredTs=currentTime+expirationTimeInSec
    token = RtcTokenBuilder.buildTokenWithUid(appId, appCertificate, channelName, uid, role, privilegeExpiredTs)
    return JsonResponse({'token':token,'uid':uid,'channel':channelName ,'username':userName},safe=False)
