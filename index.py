from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

def get_roblox_user_id(username):
    url = f"https://users.roblox.com/v1/usernames/users"
    
    headers = {
        'Content-Type': 'application/json',
    }
    
    payload = {
        "usernames": [username],
    }

    try:
        response = requests.post(url, headers=headers, json=payload)
        
        if response.status_code == 200:
            data = response.json()
            if data["data"]:
                user_id = data["data"][0]["id"]
                return user_id
            else:
                return "User not found."
        else:
            return f"Error: Unable to fetch data (Status Code: {response.status_code})"
    except Exception as e:
        return f"An error occurred: {e}"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_user_id', methods=['POST'])
def get_user_id():
    username = request.form['username']
    user_id = get_roblox_user_id(username)
    return jsonify({'user_id': user_id})

if __name__ == "__main__":
    app.run(debug=True)
