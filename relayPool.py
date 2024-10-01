# "relayPool" obsoleto substituido por "message"

import json
from websockets.sync.client import connect

class RelayPool:

	def __init__(self, subscription="asdfsadfasdf"):
		self.subscription = subscription

	def fetchEvents(self, author: str, kind: int, limit: int):
		filter = {
			"authors": [author],
			"kinds": [kind],
			"limit": limit
		}

		with connect("wss://relay.damus.io") as websocket:
			#websocket.send(f"[\"REQ\",\"{self.subscription}\", {json.dumps(filter)}]")
			websocket.send(	json.dumps(["REQ", self.subscription, filter]))
			print( json.dumps(["REQ", self.subscription, filter]))
			#websocket.send(	f'["REQ", {json.dumps(self.subscription)}, {json.dumps(filter)}]')
			#print(f'["REQ", {json.dumps(self.subscription)}, {json.dumps(filter)}]')	
			event = websocket.recv()
			print(f'\nResponse:\n{event}')
