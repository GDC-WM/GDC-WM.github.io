from urllib.parse import quote_plus
from flask import Flask, redirect, url_for, render_template, request


nextbook = Flask(__name__)


@nextbook.route("/")
def home():
    return render_template("home.html")


if __name__ == "__main__":
    nextbook.run(debug = True)
