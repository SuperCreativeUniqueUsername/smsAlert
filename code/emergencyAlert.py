import requests
from bs4 import BeautifulSoup

url = "https://511.alberta.ca/api/v2/get/alerts" 
response = requests.get(url)

if response.status_code == 200:  # check if the response is successful
    data = response.json()  # extract JSON data from the response
    message = data[0]['Message']  # extract the string from the "Notes" key
    message = BeautifulSoup(message, 'html.parser').get_text()  # convert any HTML entities to their corresponding characters
    notes = data[0]['Notes']  # extract the string from the "Notes" key
    notes = BeautifulSoup(notes, 'html.parser').get_text()  # convert any HTML entities to their corresponding characters
    print(message + '\n' + notes)  # display the string
else:
    print("Error:", response.status_code)
