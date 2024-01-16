Video Link :https://1drv.ms/v/s!AhwNlhWo4-xGjWZn3ULVCMkoSo9K?e=x9fpP3

The problems I encountered in this project are deploying, using Google Maps, logging in with Google, and using mocky API with Flask.

Design Overview:
Project Structure:

The project seems to be a Flask web application for a hotel booking platform. Below is an overview of the key components:

app.py: The main application file containing Flask routes, database initialization, and functions to interact with the database.
templates Folder: Contains HTML templates for different pages like home, detail, search, signin, and signup.
static Folder: Contains static assets like CSS files (style.css, style2.css) and images.
database.db: SQLite database file storing tables for hotels and users.
Data Model:

Hotels Table:
id: Primary key
name: Hotel name
country: Country where the hotel is located
city: City where the hotel is located
price: Price per night
rate: Hotel rating
comments: Number of comments
discount: Discount percentage
amenities: Hotel amenities
image_path: Path to the hotel image
latitude: Latitude for the map
longitude: Longitude for the map
Users Table:
id: Primary key
name: User's name
surname: User's surname
email: User's email
password: User's password
country: User's country
city: User's city
Assumptions:

User Authentication: The application assumes a basic user authentication system using email and password.
Session Management: Flask session is used for managing user sessions.
Database: SQLite is used as the database management system.
Map Integration: Google Maps JavaScript API is integrated for showing the hotel location on the map.
Detailed Analysis:
1. Database Initialization (initDB function):

Two tables are created: hotels and users.
hotels table stores information about hotels.
users table stores information about users.
2. Data Retrieval Functions:

get_hotels(): Retrieves all hotels from the database.
get_hotels_by_id(id): Retrieves a specific hotel by ID.
get_users(email): Retrieves user information by email.
get_search_results(city): Retrieves hotels based on the city.
3. Routes and Views:

/initialize: Initializes the database and redirects to the home page.
/home: Displays a list of hotels on the home page.
/signin: Handles user authentication and renders the home page if successful.
/signup: Handles user registration.
/logout: Logs out the user and redirects to the home page.
/detail/<int:id>: Displays detailed information about a specific hotel.
/search: Displays search results based on the city.
4. Templates:

base.html: The base template for other HTML pages. It includes common elements like navigation and Bootstrap styles.
home.html: Displays a list of hotels with details and a search form.
detail.html: Shows detailed information about a specific hotel, including a map.
search.html: Displays search results.
signin.html: Provides a form for user login.
signup.html: Provides a form for user registration.
5. CSS Styles (style.css, style2.css):

Contains styles for various elements on the web pages.
Suggestions:
Security:
Implement secure password handling (hashing and salting).
Use Flask's built-in features or extensions for secure session management.
Input Validation:
Implement proper input validation to prevent SQL injection and other vulnerabilities.
Error Handling:
Add error handling mechanisms to handle unexpected situations and provide meaningful error messages to users.
User Experience:
Enhance the user interface for better user experience.
Code Structure:
Consider organizing code into separate files for better maintainability, especially if the application grows.
Testing:
Implement unit tests to ensure the functionality of critical components.
Deployment:
Consider using environment variables for sensitive information like secret keys and API keys.
Choose an appropriate deployment strategy for production.
