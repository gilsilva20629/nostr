from time import time
import json

class Filter:
	
	def __init__(
		self,
		ids: list,
		authors: list,
		kinds: list,
		letter: str,
		letter_list: list,
		since: int,
		until: int,
		limit: int
		):

		self.ids = ids
		self.authors = authors
		self.kinds = kinds
		self.letter = letter
		self.letter_list = letter_list
		self.since = since
		self.until = until
		self.limit = limit

	def __init__(
		self,
		authors: list,
		kinds: list,
		limit: int
		):

		self.ids = None
		self.authors = authors
		self.kinds = kinds
		self.letter = None
		self.letter_list = None
		self.since = None
		self.until = None
		self.limit = limit

	def build(self):
		if self.ids == None:

			ready_filter = {
				"authors": self.authors,
				"kinds": self.kinds,
				"limit": self.limit
			}
			#return json.dumps(ready_filter)
			return ready_filter

		else:

			ready_filter = {
				"ids": self.ids,
				"authors": self.authors,
				"kinds": self.kinds,
				f"#{self.letter}": self.letter_list,
				"since": self.since,
				"until": self.until,
				"limit": self.limit
			}
			#return json.dumps(ready_filter)
			return ready_filter

		
		

		