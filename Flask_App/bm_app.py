# import necessary libraries
from flask import (
    Flask,
    render_template,
    jsonify,
    request)


app = Flask(__name__)


@app.route("/")
def index():
    return render_template('index.html')


# Create a list to hold our data
my_data = []


@app.route("/api/data")
def data():
    print(my_data)
    return jsonify(my_data)


@app.route("/send", methods=["GET", "POST"])
def send():
    if request.method == "POST":
        bib_number = request.form["bib number"]
        age = request.form["age"]
        gender = request.form["gender"]
        ideal_finish = request.form["ideal finish"]
        form_data = {
            "bib number": int(bib_number),
            "age": int(age),
            "gender": gender,
            "ideal finish": ideal_finish
        }

        my_data.append(form_data)

        return "Thanks for your information!"

        
    if request.method == "GET":
        if request.args.get("GETinput", None):
            result = request.args["GETinput"]
            return render_template("form.html", result=result)
    return render_template("form.html")


if __name__ == "__main__":
    app.run(debug=True) 
