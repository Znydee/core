from django.forms import ModelForm
from django.contrib.auth.models import User
from .models import Room,Message
class RoomForm(ModelForm):
    class Meta:
        model = Room
        fields= ["name"]
       
#class MessageForm(forms.Form):
#    class Meta:
#        model = Message
#        fields=["content"]