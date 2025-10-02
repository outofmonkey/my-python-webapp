from flask import Flask, render_template_string

app = Flask(__name__)

@app.route('/')
def home():
    html = '''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Welcome to My Web App</title>
        <style>
            body { font-family: Arial, sans-serif; padding: 30px; background-color: #f0f0f0; }
            .container { background: white; padding: 20px; border-radius: 8px; box-shadow: 0 0 10px rgba(0,0,0,0.1); }
            h1 { color: #333; }
            p { font-size: 1.1em; }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Welcome to My Flask Web App!</h1>
            <p>This is a simple Python web application using Flask.</p>
        </div>
    </body>
    </html>
    '''
    return render_template_string(html)

@app.route('/health')
def health():
    return "App is running!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
