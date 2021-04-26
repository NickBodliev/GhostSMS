import requests

RECIEVER = input("ENTER THE MOBILE NUMBER")
MESSAGE = input("ENTER THE MESSAGE -----> ")
resp = requests.post('https://textbelt.com/text', {
  'phone': RECIEVER,
  'message': MESSAGE,
  'key': 'textbelt',
})
print(resp.json())