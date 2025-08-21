from flask import Flask, request
import os
import docker

app = Flask(__name__)
client = docker.from_env()

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    print("Alert Received:", data)
    # Restart NGINX if alert is fired
    try:
        container = client.containers.get("nginx")
        container.restart()
        print("NGINX restarted successfully!")
    except Exception as e:
        print("Error:", e)
    return "OK", 200

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
