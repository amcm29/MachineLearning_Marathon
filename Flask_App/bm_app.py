# import necessary libraries
from flask import (
    Flask,
    render_template,
    jsonify,
    request)


app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route("/send", methods=["GET", "POST"])
def send():
    if request.method == "POST":
        bib_number = int(request.form["bib"])
        age = int(request.form["age"])
        group = int(request.form["1"])
        group = int(request.form["2"])
        temperature = float(request.form["temp"])
        hours = int(request.form["timeHours"])
        minutes = float(request.form["timeMinutes"])
        form_data = {
            "bib": int(bib_number),
            "age": int(age),
            "1": group,
            "2": group,
            "temp": temperature,
            "timeHours": hours,
            "timeMinutes": minutes
        }

        my_data.append(form_data)

        return render_template('form.html', age=age, group=1, group=2, temperature = temperature, hours = hours, minutes = minutes) "Thanks for your information!"

        
    if request.method == "GET":
        return render_template("form.html")


if __name__ == "__main__":
    app.run(debug=True) 
