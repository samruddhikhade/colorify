from flask import Flask, request, render_template
import os

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/colorize", methods=["POST"])
def colorize():
    file = request.files["image"]

    try:
        # save uploaded image
        input_path = "test_images/input.jpg"
        file.save(input_path)

        # run DeOldify script
        os.system("python deoldify/colorize_image.py")

        return render_template("index.html", image=False)

    except Exception as e:
        return f"Error: {str(e)} ❌"


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)