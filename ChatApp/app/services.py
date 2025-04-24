from .models import Chats,Messages
from channels.db import database_sync_to_async



def _get_privateChat_obj(user1, user2):
    chat = Chats.objects.filter(is_group=False,members=user1).filter(members=user2)
    return chat


def get_chat_messages(group_id):
    # messages = Messages.objects.filter(chat__group_id = group_id)
    messages = []
    chat = Chats.objects.filter(group_id=group_id).first()
    messages = chat.messages.all()
    return messages


def get_or_create_privateChat(user1, user2):
    chat = _get_privateChat_obj(user1,user2)
    if chat.exists():
        return chat.first(), False
    
    user1_id = user1.id 
    user2_id = user2.id 
    id1,id2 = (user2_id,user1_id) if user1_id > user2_id else (user1_id,user2_id)
    new_chat = Chats.objects.create(group_name=f"PrivateChat_{id1}_{id2}")
    new_chat.members.set([user1,user2])
    new_chat.save()

    return new_chat, True


@database_sync_to_async
def save_message(sender, message, group_id):
    chat = Chats.objects.filter(group_id=group_id).first()
    Messages.objects.create(chat=chat, content=message, sender=sender)
    