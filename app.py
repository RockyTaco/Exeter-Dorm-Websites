from flask import Flask, render_template
import functions

app = Flask(__name__)

# Sample data
dorm_data = { #made data all stored in this dictionary for ease of change
    'image_url': 'url_to_image',
    'motto': 'Home to the ox',
    'birthdays': [ #We'll scrape this from Connect
        {'name': 'Ryan Manley', 'date': 'January 15'},
        {'name': 'Mitchell Carson', 'date': 'February 20'},
    ],
    'faculty': [
        {'name': 'Lincoln', 'day': 'Monday'},
        {'name': 'Drescher', 'day': 'Tuesday'},
        {'name': 'Camilus', 'day': 'Wednesday'},
        {'name': 'Mills', 'day': 'Thursday'},
        {'name': 'Mit', 'day': 'Friday'},
        {'name': 'Lembo', 'day': 'Monday'}
    ]
}


@app.route('/')
def home():
    return render_template('index.html', dorm_data=dorm_data)
@app.route('/events')
def events():
    return render_template('events.html', dorm_data=dorm_data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)


