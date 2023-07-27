import requests
import json

slack_webhook_url = "https://hooks.slack.com/services/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"

def sendSlackWebhook(strText):
    headers = {
    "Content-type": "application/json"
    }

    data = {
        "text" : strText
    }

    res = requests.post(slack_webhook_url, headers=headers, data=json.dumps(data))
    
    if res.status_code == 200:
        return "ok"
    else:
        return "error"

print(sendSlackWebhook("안녕하세요 파이썬에서 보내는 메시지 입니다."))