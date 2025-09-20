from flask import Flask, send_from_directory, redirect, url_for

app = Flask(__name__, static_folder='.', static_url_path='')

@app.route('/')
def home():
    return send_from_directory('.', 'index.html')

@app.route('/about')
def about():
    return send_from_directory('.', 'about.html')

@app.route('/products')
def products():
    return send_from_directory('.', 'products.html')

@app.route('/contact')
def contact():
    return send_from_directory('.', 'contact.html')

@app.route('/login')
def login():
    return send_from_directory('.', 'login.html')

@app.route('/<path:filename>.html')
def serve_html(filename):
    return send_from_directory('.', f'{filename}.html')

@app.errorhandler(404)
def page_not_found(e):
    return redirect(url_for('home'))

# Use PORT env variable for Render
import os
port = int(os.environ.get("PORT", 5000))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port)
