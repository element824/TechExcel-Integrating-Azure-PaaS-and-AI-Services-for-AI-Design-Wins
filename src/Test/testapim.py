import os
import json
import datetime
import requests
import time
from openai import AzureOpenAI

apim_resource_gateway_url = "https://apim-jz6pum3fmpm5g.azure-api.net/azure-openai-api2"
apim_subscription_key = ""
openai_deployment_name  = "gpt-4o"
openai_api_version = "2024-06-01"
 
runs = 1
sleep_time_ms = 1000

for i in range(runs):
    print("▶️ Run: ", i+1)
    messages=[
        {"role": "system", "content": "You are a sarcastic unhelpful assistant."},
        {"role": "user", "content": "Can you tell me the time, please?"}
    ]
    client = AzureOpenAI(
        azure_endpoint=apim_resource_gateway_url,
        api_key=apim_subscription_key,
        api_version=openai_api_version
    )
    response = client.chat.completions.create(model=openai_deployment_name, messages=messages)
    print("💬 ", response.choices[0].message.content)
    time.sleep(sleep_time_ms/1000)