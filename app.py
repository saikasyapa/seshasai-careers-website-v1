from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [{
    'Id': 1,
    'Title': 'Python Developer',
    'Location': 'Hyderabad',
    'Salary': 'Rs.5,00,000'
}, {
    'Id': 2,
    'Title': 'Java Developer',
    'Location': 'Hyderabad',
    'Salary': 'Rs.6,00,000'
}, {
    'Id': 4,
    'Title': 'Frontend Developer',
    'Location': 'New Delhi',
    'Salary': 'Rs.5,00,000'
}, {
    'Id': 4,
    'Title': 'Backend Developer',
    'Location': 'banglore',
    'Salary': '7,00,000'
}, {
    'Id': 5,
    'Title': 'Data Analyst',
    'Location': 'Lucknow',
    'Salary': 'Rs.6,00,000'
}]


@app.route("/")
def hello_world():
  return render_template("home.html",
                         jobs=JOBS,
                         company_name='Aurora Consulting')


@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)


if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
