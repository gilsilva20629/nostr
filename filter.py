from time import time
import json

class Filter:
	DAY=86400
	WEEK=DAY*7
	MONTH=DAY*30
	YEAR=MONTH*12
	
	def __init__(
		self,
		authors: list,
		kinds: list,
		limit: int,
		ids=None,
		letter=None,
		letter_list=None,
		since=None,
		until=None
		):

		self.authors = authors
		self.kinds = kinds
		self.limit = limit
		self.ids = ids
		self.letter = letter
		self.letter_list = letter_list
		self.since = since
		self.until = until
		
		self.args_list = [
			self.authors,
			self.kinds,
			self.limit,
			self.ids,
			self.letter,
			self.letter_list,
			self.since,
			self.until
		]

		self.local = locals()

	def build(self):
		ready_filter = {}
		for arg in self.args_list:
			#print("arg:", arg)
			if arg != None:
				for x, y in self.local.items():
					#print("x, y:", x,"_", y)
					if arg == y :
						if isinstance(arg, str) and len(arg) == 1 and arg in "pe" :
							'''
							try:
								print(len(arg), type(arg))
							except Exception as E:
								print("ocoreu um erro!", E)
							'''
							ready_filter.update({"#" + arg: self.letter_list })

						else:
							'''
							try:
								print(len(arg), type(arg))
								#ready_filter[x] = arg
							except Exception as E:
								print("ocoreu um erro!", E)
							'''
							ready_filter.update({x: arg})

		if "letter_list" in ready_filter :
			ready_filter.pop("letter_list")

		#print("Teste de build:", ready_filter, end="\n\n")
		return ready_filter
		
		
				
