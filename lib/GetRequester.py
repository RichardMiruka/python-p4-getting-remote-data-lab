import requests
import json

class GetRequester: #GetRequester class has been defined with an __init__ method to initialize the url attribute

    def __init__(self, url):     #get_response_body method sends a GET request to the provided URL using the requests library and returns the response body as a string.
        self.url = url

    def get_response_body(self):
        response = requests.get(self.url)
        return response.text

    def load_json(self):
        response_body = self.get_response_body()
        data = json.loads(response_body)
        return data
    
    #The load_json method utilizes the get_response_body method to retrieve the response body
    #Then, it uses the json.loads function to convert the response body into a Python list or dictionary, depending on the structure of the JSON data.
    
    #Getting Remote Data(GET requests using python)