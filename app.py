from flask import Flask, render_template, request, redirect
from connect_postgres import *

app = Flask(__name__)


@app.route("/")
def hello_route():
    return render_template("add_url.html")


# Not needed, table will be initialized when running docker compose via db/init.sql
# @app.route('/create_table')
# def create_database_table_route():
#     create_table()
#     return "Table created!"


@app.route("/add_url", methods=["POST"])
def add_url_route():

    # Retrieve form data from add_url.html with the following names
    original_url = request.form["original_url"]
    short_code = request.form["short_code"]

    add_url(original_url, short_code)
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
