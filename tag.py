class Tag:
	def __init__(self):
		self.y = { "tags": [] }

	def add(self, x: list):
		self.y["tags"].append(x)

	def get(self):
		return self.y
