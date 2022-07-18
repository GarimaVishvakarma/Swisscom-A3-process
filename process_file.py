from flask import Flask, jsonify, request
import boto3

app = Flask(__name__)
client = boto3.resource("sqs")


@app.route('/', methods=['POST'])
def home():
    get_file = request.get_json()
    file_name = get_file['file']
    queue = client.get_queue_by_name(QueueName="swisscom-queue")
    response = queue.send_message(MessageBody= file_name)
    return jsonify({"data": response})


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5001, debug=True)

