# import requests
#
# # API URL
# url = "<your_lambda_function_url>/predict"
#
# # Data to be sent in the POST request
# data = {
#     "state": "Delhi",
#     "city": "khanshar",
#     "aqi_values": [145,130,200,175,89]
# }
#
# # Make the POST request
# response = requests.post(url, json=data)
#
# # Print the response from the server
# if response.status_code == 200:
#     print("Prediction:", response.json())
# else:
#     print(f"Failed to get response, status code: {response.status_code}")


import requests

# API Gateway URL for your Lambda function
url = "https://n2y4uv6qpx6j73xgjf5wkfzmze0hpsdu.lambda-url.ap-south-1.on.aws/predict_batch"

# Request headers
headers = {"Content-Type": "application/json"}

# Data to be sent in the POST request
data = {
    "state": "Delhi",
    "city": "Khanshar",
    "aqi_values": [145, 130, 200, 175, 89]
}

# Make the POST request
response = requests.post(url, json=data, headers=headers)

# Print the response from the server
if response.status_code == 200:
    print("Prediction:", response.json())
else:
    print(f"Failed to get response, status code: {response.status_code}, Response: {response.text}")
