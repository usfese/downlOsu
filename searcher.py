import requests
import json

class Searcher:
    def __init__(self, num):
        request_dict = None

    def search(self):
        count = num
        offset = 0
        while count > 0:
            batch_size: int = min(30,count)
            count -= batch_size
            request_dict = {"limit" : batch_size, "offset" : offset}