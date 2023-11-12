from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/counter", methods=["GET", "POST"])
def counter():
    counter = int(request.args.get("counter", "-1"))
    counter += 1
    url = request.base_url
    return render_template("counter.html", counter=counter, url=url)


if __name__ == "__main__":
    app.run()
