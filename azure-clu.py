import requests
import json
import pprint

url = "https://language123.cognitiveservices.azure.com/language/:analyze-conversations?api-version=2022-10-01-preview"

headers = {
    'Ocp-Apim-Subscription-Key':'4d499847b86c48ca9ca21f298e3047b6'

    
}


data = {
    "kind": "Conversation",
    "analysisInput": {
        "conversationItem": {
            "id": "id__3019",
            "text": "I would",
            "modality": "text",
            "language": "en",
            "participantId": "id__3019"
        }
    },
    "parameters": {
        "projectName": "chat-demo",
        "verbose": True,
        "deploymentName": "myDeployment",
        "stringIndexType": "TextElement_V8"
    }
}

enter= input("Enter your order: ")
data["analysisInput"]["conversationItem"]["text"] = enter

response = requests.post(url, headers=headers, json=data)

if response.status_code ==200:
    data = json.loads(response.text)
    #print(data)
else:
    print(f"Error: {response.status_code}")
    #print(response.text)    
try:
    resultDic = data['result']

    predictionDic = resultDic['prediction']

    order = predictionDic['topIntent']

    
    orders = {'order a drink': 'Notificación Bartender', 
            'order hambuger' : 'Notificaión Chef',
            'order pizza' : 'Notificaión Chef',
            'pay the bill' : 'Notificacío Cajero'
            }

    #notification = orders.get(order)
    print(orders)
except:
    print("You made a mistake")

