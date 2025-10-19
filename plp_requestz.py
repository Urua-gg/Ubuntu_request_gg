import requests
#send a message to a specified website and get response
response = requests.get("https://www.usedcars.co.ke/cars-for-sale")

#send a message if the response is successful
if response.status_code == 200:
    print("Request was successful!")
    print("Response Content:", response.text)
else:
    print("Request failed with status code:", response.status_code)

    print("Response Content:", response.text)