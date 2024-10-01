from websockets.sync.client import connect
import json

class MessageEvent:

	def sendMessage(self,  relay: str, msg: str):
		self.relay = relay
		self.msg = msg
		self.ready_message = f'["EVENT", {msg}]'		#["EVENT", <event JSON as defined above>], usado para publicar eventos.

		with connect(self.relay) as websocket:
			websocket.send(self.ready_message)
			response = websocket.recv()
			return response


class MessageReq:

	def sendMessage(self, relay: str, subscription: str, filters: list):
		self.relay = relay
		self.subscription =	subscription
		self.filters = filters
		self.intermadiary_message = ["REQ", self.subscription]
		for f in self.filters:
			self.intermadiary_message.append(f)

		#["REQ", <subscription_id>, <filters1>, <filters2>, ...], usado para solicitar eventos e assinar novas atualizações.	
		self.ready_message = json.dumps(self.intermadiary_message)
		#print(self.ready_message, end="\n\n")
		#print(type(self.ready_message), end="\n\n")

		with connect(self.relay) as websocket:
			websocket.send(self.ready_message)
			response = websocket.recv()
			return response


class MessageClose:

	def sendMessage(self, relay: str, subscription: str):
		self.relay = relay
		self.subscription =	subscription
		#["CLOSE", <subscription_id>], usado para interromper assinaturas anteriores.
		#self.ready_message = f'["CLOSE", {self.subscription}]'	
		self.ready_message = json.dumps(["CLOSE", self.subscription])
		print(self.ready_message)
		
		with connect(self.relay) as websocket:
			websocket.send(self.ready_message)
			response = websocket.recv()
			return response
