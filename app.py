from flask import Flask, request, jsonify

app = Flask(__name__)

# Function to process the POST request data
def process_data(data):
    numbers = []
    alphabets = []
    highest_lowercase = []

    for item in data:
        if item.isdigit():
            numbers.append(item)
        elif item.isalpha():
            alphabets.append(item)
            if item.islower():
                highest_lowercase.append(item)

    highest_lowercase.sort(reverse=True)
    return numbers, alphabets, highest_lowercase[:1]

# POST method route
@app.route('/bfhl', methods=['POST'])
def handle_post():
    try:
        req_data = request.get_json()

        if not req_data or 'data' not in req_data:
            return jsonify({"is_success": False, "message": "Invalid input"}), 400

        numbers, alphabets, highest_lowercase = process_data(req_data['data'])

        response = {
            "is_success": True,
            "user_id": "john_doe_17091999",  # Replace with your own logic for user_id
            "email": "john@xyz.com",
            "roll_number": "ABCD123",
            "numbers": numbers,
            "alphabets": alphabets,
            "highest_lowercase_alphabet": highest_lowercase
        }
        return jsonify(response), 200

    except Exception as e:
        return jsonify({"is_success": False, "message": str(e)}), 500

# GET method route
@app.route('/bfhl', methods=['GET'])
def handle_get():
    response = {
        "operation_code": 1
    }
    return jsonify(response), 200

if __name__ == '__main__':
    app.run(debug=True)
