from flask import Flask, redirect, url_for, render_template, request


site = Flask(__name__)


@site.route("/")
def home():
    return render_template("home.html")

@site.route("/parryt")
def parryt():
	return render_template("parryt.html")

if __name__ == "__main__":
    site.run(debug = True)
