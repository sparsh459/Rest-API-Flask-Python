from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/armstrong/<int:n>")
def armstrong(n):
    sum = 0
    order = len(str(n))
    copy_n = n
    while(n>0):
        digit = n%10
        sum += digit **order
        n = n//10
    
    if sum == copy_n:
        print(f"{copy_n} is an armstrong number")
        result ={
            "Number":copy_n,
            "Armstrong": True,
            "server_ip": "127:127:143:08/24",
            "Other NUmbers": [23,24,25,25]
        }
    else:
        print(f"{copy_n} is not an armstrong number")
        result ={
            "Number":copy_n,
            "Armstrong": False,
            "server_ip": "127:127:143:09/24",
            "Other numbers": [232, 2,2332,244,35,435,343,3433,3343443,34]
        }
    return jsonify(result)


if __name__ == '__main__':
    app.run(debug=True)