from django.shortcuts import render, redirect
from .forms import RoomForm
from django.http import HttpResponse, JsonResponse
from .models import Room, Message
# Create your views here.
def home(request):
    #return render(request,"chatapp/home.html")
    #form = RoomForm()
    #print(request.POST)
    if request.method == "POST":
        print(request.POST)
        if Room.objects.filter(name=request.POST["room_name"]).exists():
            return redirect("chatroom",room=request.POST["room_name"],username=request.POST["username"] )
        else:
            Room.objects.create(name=request.POST["room_name"])
            return redirect("chatroom",room=request.POST["room_name"] ,username=request.POST["username"] )
    return render(request,"chatapp/home.html")
    
#def join_room_or_create(request):    
#    print("heyy")
#    if Room.objects.filter(name=request.POST["groupname"]).exists():
#        return redirect("chatroom",room=request.POST["groupname"] )
#    else:
#        Room.objects.create(name=request.POST["groupname"])
#        return redirect("chatroom",room=request.POST["groupname"] )
    
def room(request,room, username):
    room=Room.objects.filter(name= room).first()
    messages=Message.objects.filter(room=room)
    return render(request,"chatapp/room.html",{"username":username,"room":room,"messages":messages})
   
def get_message(request,room):
    print(room)
    room=Room.objects.filter(name=room).first()
    messages = Message.objects.filter(room=room)
    return JsonResponse({"messages":list(messages.values())})
    
def  send_message(request):
    room=Room.objects.filter(name=request.POST["room"]).first()
    Message.objects.create(user=request.POST["username"],room=room, content=request.POST["message"])
    return HttpResponse("done")