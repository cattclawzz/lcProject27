from flask import Flask, render_template

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"]) 

def index():
    return render_template(
        "index.html",
        foo = "Hello World!"
    )

#!!flask server!!
if __name__ == "__main__":
    app.run(debug=True)
