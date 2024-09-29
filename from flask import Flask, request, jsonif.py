from flask import Flask, request, jsonify

app = Flask(__name__)

commands = []

@app.route('/send-command', methods=['POST'])
def receive_command():
    data = request.json
    command = data.get("command")
    if command:
        # exec command fix
        if command not in commands:
            commands.append(command)
            return jsonify({"message": "Command received", "command": command}), 200
        else:
            return jsonify({"message": "Command already received"}), 200
    return jsonify({"message": "No command provided"}), 400

@app.route('/get-commands', methods=['GET'])
def get_commands():
    if commands:
        command = commands.pop(0)  #getv
        return jsonify({"commands": [command]}), 200
    return jsonify({"commands": []}), 200

@app.route('/delete-command', methods=['DELETE'])
def delete_command():
    command = request.json.get("command")
    if command in commands:
        commands.remove(command)
        return jsonify({"message": "Command deleted"}), 200
    return jsonify({"message": "Command not found"}), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)
