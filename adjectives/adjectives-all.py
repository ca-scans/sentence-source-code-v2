from flask import Flask, json

adjectives = [{"id": 1,"name": "kind","credit-card": "4554 1111 1111 1111"},{"id": 2,"name": "proud", "credit-card": "4554 1111 1111 1111"},{"id": 3,"name": "calm", "credit-card": "4554 1111 1111 1111"}]

api = Flask(__name__)

@api.route('/api/adjectives', methods=['GET'])
def get_adjectives():
  return json.dumps(adjectives)

@api.route('/api/adjectives', methods=['POST'])
def post_adjectives():
  return json.dumps({"success": True}), 201

@api.route('/api/adjectives', methods=['DELETE'])
def delete_adjectives():
  return json.dumps({"success": True}), 202

if __name__ == '__main__':
    api.run()
