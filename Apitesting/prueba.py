import requests

url = "http://localhost/test1/wp-json/wp/v2/pages/11"

payload={}
headers = {
  'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOjEsIm5hbWUiOiJhYmFycmllbnRvIiwiaWF0IjoxNjU4MjU0MTg1LCJleHAiOjE4MTU5MzQxODV9.Kobp4Mmkelzn9f_cUHURAP9d8Lp1F1XdfVWYVu9vSSM'
}

response = requests.request("DELETE", url, headers=headers, data=payload)

print(response.text)
