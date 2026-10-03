from flask import Flask, render_template, request, send_from_directory

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    image_name = None
    if request.method == 'POST':
        image_name = request.form.get('image_name', '')
    return render_template('index.html', image_name=image_name)

@app.route('/img/<path:filename>')
def serve_image(filename):
    return send_from_directory('static/img', filename)

if __name__ == '__main__':
    app.run(debug=True)