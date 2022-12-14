from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Room(models.Model):
    name = models.CharField(max_length=128)
    #online = models.ManyToManyField(User, blank=True)
    #participant = models.CharField(max_length=128,default="anon")
    #def get_online_count(self):
#        return self.online.count()

#    def join(self, user):
#        self.online.add(user)
#        self.save()

#    def leave(self, user):
#        self.online.remove(user)
#        self.save()
        
    def __str__(self):
        return f"{self.name} chatroom"
        
class Message(models.Model):
    #user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    user = models.CharField(max_length=128,default="anon")
    room = models.ForeignKey(to=Room, on_delete=models.CASCADE)
    content = models.CharField(max_length=512)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"sent from {self.user} to {self.room}"