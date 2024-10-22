import httpx

url = "https://scaling-fortnight-x5qjx44jw9ghvx94-5000.app.github.dev/"

response = httpx.get(url)
print(response.status_code)
print(response)



response = httpx.get(url)
print(response.status_code)
print(response.text)

mydata = {
    "text": "Hello Casey!",
    "param2": "Making a POST request"
}

# A POST request to the API
response = httpx.post(url + "echo", data=mydata)

# Print the response
print(response.status_code)
print(response.text)

success1 = {
"id": "Casey",
"token": "school"
}

# A POST request to the API
response = httpx.post(url + "login", data=success1)

# Print the response
print(response.status_code)
print(response.text)


success2 = {
"id": "Phil",
"token": "school1"
}

# A POST request to the API
response = httpx.post(url + "login", data=success2)

# Print the response
print(response.status_code)
print(response.text)

fail1 = {
"id": "Casey",
"token": "schoolio"
}

# A POST request to the API
response = httpx.post(url + "login", data=fail1)

# Print the response
print(response.status_code)
print(response.text)
