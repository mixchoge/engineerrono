from django.contrib import admin
from .models import Respond, Message, Chat, Private

admin.site.register(Respond)
admin.site.register(Message)
admin.site.register(Chat)
admin.site.register(Private)
