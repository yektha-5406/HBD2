from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def home():
    return '''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Birthday Wishes 🎂</title>
        <style>
            body {
                text-align: center;
                font-family: Arial;
                background: linear-gradient(to right, pink, purple);
                color: white;
            }
            .container {
                margin-top: 100px;
            }
            input {
                padding: 10px;
                font-size: 16px;
            }
            button {
                padding: 10px 20px;
                background-color: yellow;
                border: none;
                cursor: pointer;
            }
            h1 {
                font-size: 40px;
            }
        </style>
    </head>
    <body>

    <div class="container">
        <h1>🎉 Birthday Wishes App 🎉</h1>

        <form method="POST" action="/wish">
            <input type="text" name="name" placeholder="Enter your friend's name" required>
            <br><br>
            <button type="submit">Send Wish</button>
        </form>
    </div>

    </body>
    </html>
    '''

@app.route('/wish', methods=['POST'])
def wish():
    name = request.form.get('name')

    return f'''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Wish</title>
        <style>
            body {{
                text-align: center;
                font-family: Arial;
                background: linear-gradient(to right, orange, red);
                color: white;
            }}
            h1 {{
                margin-top: 100px;
                font-size: 40px;
            }}
            a {{
                color: yellow;
                text-decoration: none;
                font-size: 20px;
            }}
        </style>
    </head>
    <body>

        <h1>🎂 Happy Birthday {name}! 🎉</h1>
        <p>Wishing you lots of happiness and success! 💖</p>

        <br><br>
        <a href="/">🔙 Go Back</a>

    </body>
    </html>
    '''

if __name__ == '__main__':
    app.run(debug=True)
