import plyvel
import os

class Alexandria():
	def __init__(self, location):
		os.makedirs(location + "/alexandria")

		self.location = location
		self.current_collection_object = None
		self.collections = []

	class Collection():
		def __init__(self, name):
			self.name = name

			self.kvstore = plyvel.DB("", create_if_missing=True)

		def create_document(self, obj):
			self.kvstore.put(key, obj)

		def delete_document(self, key):
			self.kvstore.delete(key)

		def update_document(self, key, obj):
			self.kvstore.update(key, obj)

		class Document():
			def __init__(self, ):		
