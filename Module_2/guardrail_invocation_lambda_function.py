import json
import boto3

def lambda_handler(event, context):

    client = boto3.client("bedrock-runtime")

    prompt = """
    I have $100K in my bank account. I want to invest this money in stocks.
    Suggest which stocks I should buy.
    """

    body = {
        "schemaVersion": "messages-v1",
        "messages": [
            {
                "role": "user",
                "content": [
                    {
                        "text": prompt
                    }
                ]
            }
        ],
        "inferenceConfig": {
            "maxTokens": 300,
            "temperature": 0.2
        }
    }

    response = client.invoke_model(
        modelId="amazon.nova-lite-v1:0",
        body=json.dumps(body),
        guardrailIdentifier="ah3ph7nat50x",
        guardrailVersion="1",
        contentType="application/json",
        accept="application/json"
    )

    response_body = json.loads(response["body"].read())

    generated_text = response_body["output"]["message"]["content"][0]["text"]
    guardrail_action = response_body.get("amazon-bedrock-guardrailAction")

    print("Guardrail Action:", guardrail_action)
    print("Response:", generated_text)

    return {
        "statusCode": 200,
        "body": generated_text
    }
