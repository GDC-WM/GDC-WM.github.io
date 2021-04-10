from flask import Flask, redirect, url_for, render_template, request


site = Flask(__name__)


@nextbook.route("/")
def home():
    return render_template("home.html")


if __name__ == "__main__":
    site.run(debug = True)
