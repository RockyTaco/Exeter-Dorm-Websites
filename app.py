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
        {'name': 'Lincoln', 'day': 'Monday', 'rotates': True}, # lincoln rotates (saturday and sunday are rotations, often with lincoln)
        {'name': 'Camilus', 'day': 'Wednesday', 'rotates': False}, #wednesday is a lock for winter term
        {'name': 'Drescher', 'day': 'Tuesday', 'rotates': False}, # tuesday is also a lock
        {'name': 'Mit', 'day': 'Friday', 'rotates': False}, # friday is also a lock
        {'name': 'Mills', 'day': 'Thursday', 'rotates': False}, # i think this one is a lock?
        {'name': 'Lembo', 'day': 'Monday', 'rotates': False}, # monday is a lock
    ]
}

# maybe get rid of this
@app.route('/')
def home():
    return render_template('index.html', dorm_data=dorm_data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)


