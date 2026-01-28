import json
from agent import run_agent

def handle_message(message):
    payload = json.loads(message.data.decode())
    result = run_agent(payload)

    print("Agent result:", result)
    message.ack()
