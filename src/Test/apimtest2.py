import os
import json
import datetime
import requests
import time
runs = 1
sleep_time_ms = 1000

apim_resource_gateway_url = "https://apim-jz6pum3fmpm5g.azure-api.net/azure-openai-api2/openai"
openai_deployment_name  = "gpt-4o"
apim_subscription_key = ""
openai_api_version = "2024-06-01"
url = apim_resource_gateway_url + "/deployments/" + openai_deployment_name + "/chat/completions?api-version=" + openai_api_version

for i in range(runs):
    print("▶️ Run: ", i+1)
    messages={"messages":[
        {"role": "system", "content": "You are a sarcastic unhelpful assistant."},
        {"role": "user", "content": "Can you tell me the time, please?"}
    ]}
    response = requests.post(url, headers = {'api-key':apim_subscription_key}, json = messages)
    print("status code: ", response.status_code)
    print("headers ", response.headers)
    print("x-ms-region: ", response.headers.get("x-ms-region")) # this header is useful to determine the region of the backend that served the request
    if (response.status_code == 200):
        data = json.loads(response.text)
        print("response: ", data.get("choices")[0].get("message").get("content"))
    else:
        print(response.text)
    time.sleep(sleep_time_ms/1000)