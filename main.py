from telethon.sync import TelegramClient, events
from telethon.tl.types import PeerUser, User, PeerChat, PeerChannel
from pip._vendor import tomli

def read_file(path):
   with open(path, 'r') as f:
      return f.read()

config = tomli.loads(read_file('config.toml'))

# TODO: replace with our grouip
dest_chats = [
   'OutputDlock'
]

with TelegramClient('AlphaAggregator', config["auth"]["api_id"], config["auth"]["api_hash"]) as client:
   # Log starting
   client.send_message(dest_chats[0], "AlphaAggregator started")
   client.iter_dialogs()
   src_ids  = []
   dst_id = None
   for dialog in client.iter_dialogs():
      if dialog.title in config["config"]["groups"]:
         print(dialog.title)
         src_ids.append(dialog.id)
      elif dialog.title in dest_chats:
         dst_id = dialog.id
   
   if dst_id is None:
      print("Destination chat not found")
      exit(1)

   @client.on(events.NewMessage(chats=src_ids, from_users=config["config"]["users"]))
   async def handler(event):
      channel_id=event.message.peer_id
      sender = await event.get_sender()
      sender_identifier = sender.username if sender.username else sender.first_name if sender.first_name else sender.id
      channel = await client.get_input_entity(channel_id)
      chat_from = event.chat if event.chat else (await event.get_chat()) # telegram MAY not send the chat enity
      chat_title = chat_from.title
      print(sender)
      print(channel)
      message_text = event.raw_text
      # print(event.message)

      # print(event);
      await client.send_message(dest_chats[0], "<b>{}</b> - @{} <blockquote>{}</blockquote>".format(chat_title,sender_identifier , message_text), parse_mode='html')
      print("Message sent")
   client.run_until_disconnected()