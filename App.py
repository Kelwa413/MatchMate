from flask import Flask, render_template, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('homepage.html')
@app.route('/date_time_selection')
def book():
    return render_template('/date_time_selection.html')


if __name__ == '__main__':
    app.run(debug=True)
# for server go to: http://127.0.0.1:5000/
# test test 123