from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [{
    'id': 1,
    'title': 'python developer',
    'location': 'Hyderabad',
    'salary': 'Rs.5,00,000'
}, {
    'id': 2,
    'title': 'java developer',
    'location': 'Hyderabad',
    'salary': 'Rs.5,50,000'
}, {
    'id': 3,
    'title': '.net developer',
    'location': 'Chennai',
}, {
    'id': 4,
    'title': 'frontend developer',
    'location': 'New delhi',
    'salary': 'Rs.5,00,000'
}]


@app.route("/")
def hello_world():
  return render_template("home.html", jobs=JOBS, company_name='magnasoft')


@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)


if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
