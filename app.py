import sqlite3 as sql
from flask import Flask, render_template, request, redirect, url_for, flash, session


from flask import session


app = Flask(__name__)
app.secret_key = 'e7e5017844a0d8ffbb40ec346072c2198581a7418134892a'



def initDB():
    conn = sql.connect('database.db')
    print("Opened database successfully")   
    
    conn.execute('CREATE TABLE IF NOT EXISTS hotels (id INTEGER PRIMARY KEY, name Text,country Text,city Text, price float, rate float,comments integer, discount float,amenities Text, image_path TEXT, latitude float, longitude float)')
    print("Table created successfully")

    conn.execute('CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT, surname TEXT, email TEXT ,password TEXT, country TEXT, city TEXT)')
    print("Users table created successfully")
    
    conn.commit()
    conn.close()

def get_hotels():
    conn = sql.connect('database.db')
    cursor = conn.execute("SELECT id, name,country,city , price, rate,comments , discount ,amenities, image_path, latitude, longitude FROM hotels")
    hotels = cursor.fetchall()
    conn.close()
    return hotels

def get_hotels_by_id(id):
    conn = sql.connect('database.db')
    cursor = conn.execute("SELECT id, name,country,city , price, rate,comments , discount ,amenities, image_path, latitude, longitude FROM hotels WHERE id = ?", (id,))
    hotel = cursor.fetchone()
    conn.close()
    
    if hotel:
        # Convert the result to a dictionary for easier access in the template
        hotel_dict = {
            'id': hotel[0],
            'name': hotel[1],
            'country': hotel[2],
            'city': hotel[3],
            'price': hotel[4],
            'rate': hotel[5],
            'comments': hotel[6],
            'discount': hotel[7],
            'amenities': hotel[8],
            'image_path': hotel[9],
            'latitude' : hotel[10],
            'longitude' : hotel[11],

        }
        return hotel_dict
    else:
        # Return None if the hotel is not found
        return None

def add_user(name, surname, email, password, country, city):
    conn = sql.connect('database.db')
    conn.execute("INSERT INTO users (name, surname, email, password, country, city) VALUES (?, ?, ?, ?, ?, ?)",
                 (name, surname, email, password, country, city))
    conn.commit()
    conn.close()

def get_users(email):
    conn = sql.connect('database.db')
    cursor = conn.execute("SELECT id, name, surname, email, password, country, city FROM users WHERE email=?", (email,))
    user = cursor.fetchone()
    conn.close()

    if user:
        user_dict = {
            'id': user[0],
            'name': user[1],
            'surname': user[2],
            'email': user[3],
            'password': user[4],
            'country': user[5],
            'city': user[6]
        }
        return user_dict
    else:
        return None
    
def get_search_results(city):
    conn = sql.connect('database.db')
    cursor = conn.execute("SELECT id, name,country,city , price, rate,comments , discount ,amenities, image_path, latitude, longitude FROM hotels WHERE city = ?", (city,))
    search = cursor.fetchone()
    conn.close()
    if search:
        # Convert the result to a dictionary for easier access in the template
        search_dict = {
            'id': search[0],
            'name': search[1],
            'country': search[2],
            'city': search[3],
            'price': search[4],
            'rate': search[5],
            'comments': search[6],
            'discount': search[7],
            'amenities': search[8],
            'image_path': search[9],
            'latitude' : search[10],
            'longitude' : search[11],

        }
        return search_dict
    else:
        # Return None if the hotel is not found
        return None

@app.route('/initialize')
def initialize():
    # Call the initDB function to initialize the database and insert the first element
    initDB()
    return redirect(url_for('home_page'))

@app.route('/home')
def home_page():
    hotels = get_hotels()

    return render_template('home.html', hotels=hotels)

@app.route('/signin', methods=['GET', 'POST'])
def signin_page():
    user = None
    

    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        user = get_users(email)

        if user and user['password'] == password:
            flash('Logged in successfully!')
            return render_template('home.html', user=user, hotels=get_hotels())

        flash('Invalid credentials. Please try again.')

    return render_template('signin.html', user=user)
    



@app.route('/signup', methods=['GET', 'POST'])
def signup_page():
    if request.method == 'POST':
        name = request.form['name']
        surname = request.form['surname']
        email = request.form['email']
        password = request.form['password']
        country = request.form.get('country')
        city = request.form.get('city')

        # Add the new user to the database
        add_user(name, surname, email, password, country, city)
        flash('Account created successfully!')
        return redirect(url_for('signin_page'))

    return render_template('signup.html')

@app.route('/logout')
def logout():
    # Clear user-related data from the session
    session.pop('user', None)  # Assuming you store user information under the 'user' key in the session

    # Redirect to the home page or any other desired page
    return redirect(url_for('home_page'))

@app.route('/detail/<int:id>', methods = ['GET'])
def detail(id):
    if request.method == 'GET':
        try:

         with sql.connect("database.db") as con:
            cur = con.cursor()
            cur.execute("SELECT FROM hotels WHERE Id = ?",(id) )
            
            con.commit()
            con.close() 
        finally:
            hotel = get_hotels_by_id(id)
            

            
            return render_template('detail.html', hotel=hotel)

@app.route('/search', methods=['GET'])
def search_results():
    query = request.args.get('q', '')

    conn = sql.connect('database.db')
    cursor = conn.cursor()

    
    cursor.execute("SELECT * FROM hotels WHERE city LIKE ? ", ('%' + query + '%'))

    results = cursor.fetchall()

    conn.close()

    return render_template('search.html', results=results)

if __name__ == '__main__':
    app.run(debug=True)