from flask import Flask, request, jsonify, render_template
from pymongo import MongoClient
from flask import session

app = Flask(__name__)
app.secret_key = 'your_secret_key'

client = MongoClient("mongodb+srv://Ayurpharma:medrecom34@cluster0.j0lio.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
db = client.doctor_db
doctor_collection = db.doctors

@app.route('/')
def hello_world():  # put application's code here
    return render_template('index.html')


@app.route('/register')
def about():
    return render_template('register.html')


@app.route('/register', methods=['POST'])
def register():
    if request.method == 'POST':
        data = {
            "name": request.form['name'],
            "email": request.form['email'],
            "password": request.form['password'],
            "phone": request.form['phone'],
            "experience": int(request.form['experience']),
            "certification_id": request.form['certification_id']
        }

        # Insert data into the database
        doctor_collection.insert_one(data)

        return jsonify({"message": "Registration successful!"})

@app.route('/login')
def about1():
    return render_template('login.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        user = doctor_collection.find_one({'email': email, 'password': password})

        return render_template('bot.html')





@app.route('/show_data')
def show_data():
    # Fetch all registered doctor data
    all_data = list(doctor_collection.find())
    return render_template('show_data.html', data=all_data)


if __name__ == '__main__':
    app.run(debug=True)
