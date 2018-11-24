import requests
api_address="http://api.forismatic.com/api/1.0/?method=getQuote&lang=en&format=jsonp&jsonp=?"
api_address1=requests.get(api_address).content
print(api_address1)
