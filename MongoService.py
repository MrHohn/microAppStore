from pymongo import MongoClient
import random

class DataService(object):

	def init(cls, client):
		cls.client = client
		cls.db = client.appstore
		cls.user_download_history = cls.db.user_download_history
		cls.app_info = cls.db.app_info

	def retrieve_user_download_history(cls, filter_dict = {}):
		# return a dict {user_id: downlad_history} containing user download history data
		# return all data in the collection if no filter is specified
		result = {}
		cursor = cls.user_download_history.find(filter_dict)
		for user_download_history in cursor:
			result[user_download_history['user_id']] = user_download_history['downlad_history']
		return result

	def update_app_info(cls, filter_dict, update):
		cls.app_info.update_one(filter_dict, update, True)