from websockets.sync.client import connect
import json

from keyPair import KeyPair
from event import Event
import message
from filter import Filter
#from relayPool import RelayPool

keyPair = KeyPair("b2776165d40acc349ad1f7f11105b037a3403971ee1be87787b47b407b6eb77f")
user_data = json.dumps({"name": "test_dev_nostr", "displayName": "GSO"})
event = Event(kind=0, author=keyPair.getPubkey(), content=user_data)

event.sign(keyPair)	

msg_event = message.MessageEvent()
print(msg_event.sendMessage("wss://relay.damus.io", event.serialize()))

authors = ["04c915daefee38317fa734444acee390a8269fe5810b2241e5e6dd343dfbecc9"]
filter01 = Filter(authors,[1],3)

authors = ["82341f882b6eabcd2ba7f1ef90aad961cf074af15b9ef44a09f9d2a8fbfbe6a2"]	
filter02 = Filter(authors,[1],3)

authors = ["6e468422dfb74a5738702a8823b9b28168abab8655faacb6853cd0ee15deee93"]
filter03 = Filter(authors,[1],3)

msg_req = message.MessageReq()
#print(msg_req.sendMessage("wss://relay.damus.io", "asdfasdasd", [filter01.build(), filter02.build(), filter03.build()]))
#print(msg_req.sendMessage("wss://relay.damus.io", "asdfasdasd", [filter02.build(), filter03.build()]))
print(msg_req.sendMessage("wss://relay.damus.io", "asdfasdasd", [filter03.build()]))

msg_close = message.MessageClose()
print(msg_close.sendMessage(relay="wss://relay.damus.io", subscription="asdfasdasd"))

