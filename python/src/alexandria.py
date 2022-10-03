import plyvel
import os

class Alexandria():
	class Document():
		def __init__(self, location):
			os.makedirs(location + "/alexandria")

			self.location = location
			self.current_collection_object = None
			self.collections = []

		class Collection():
			def __init__(self, name):
				self.name = name

				self.kvstore = plyvel.DB("", create_if_missing=True)

			def retrieve_document(self, ):

			def create_document(self, obj):
				self.kvstore.put(key, obj)

			def delete_document(self, key):
				self.kvstore.delete(key)

			def update_document(self, key, obj):
				self.kvstore.update(key, obj)


	class Graph():
		def __init__(self, location, name):
			os.makedirs(location + "/alexandria/" + name)

			self.location = location
			self.current_collection_object = None
			self.graphs = []

		class Node():
			def __init__(self, ):	
