from settings import API_KEY
from serpapi import GoogleSearch

def get_results(query):    
    params = {
      "q": query,
      "location": "Lagos, Lagos, Nigeria",
      "hl": "en",
      "gl": "ng",
      "google_domain": "google.com",
      "api_key": API_KEY
    }

    search = GoogleSearch(params)
    response = search.get_dict()
    return response
