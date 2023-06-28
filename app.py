from flask import Flask, request, render_template

app = Flask(__name__)

# Define a route for the root URL ("/") with GET method
@app.route("/", methods=["GET"])
def first_route():
    return render_template("index.html",message="Hello Earthling")

# Run the Flask application if executed directly
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5001)