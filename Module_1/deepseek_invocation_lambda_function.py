import json
import boto3

def lambda_handler(event, context):
    client = boto3.client("bedrock-runtime")

    prompt = """
    What is Amazon Bedrock?
    """

    body = {
        "messages": [
            {
                "role": "user",
                "content": prompt
            }
        ],
        "max_tokens": 300,
        "temperature": 0.2
    }

    response = client.invoke_model(
        modelId="deepseek.v3.2",
        body=json.dumps(body),
        contentType="application/json",
        accept="application/json"
    )

    response_body = json.loads(response["body"].read())
    generated_text = response_body['choices'][0]["message"]["content"]
    print("Generated response:")
    print(generated_text)

    return {
        "statusCode": 200,
        "body": generated_text
    }
