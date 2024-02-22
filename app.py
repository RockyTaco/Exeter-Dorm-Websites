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
main
        {'name': 'Lincoln', 'day': 'Monday', 'rotates': True},
        {'name': 'Drescher', 'day': 'Tuesday', 'rotates': False},
        {'name': 'Camilus', 'day': 'Wednesday', 'rotates': False},
        {'name': 'Mills', 'day': 'Thursday', 'rotates': False},
        {'name': 'Mit', 'day': 'Friday', 'rotates': True},
        {'name': 'Lembo', 'day': 'Monday', 'rotates': False}     
    ]
}

# maybe get rid of this
@app.route('/')
def home():
    return render_template('index.html', dorm_data=dorm_data)
@app.route('/events')
def events():
    return render_template('events.html', dorm_data=dorm_data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)


