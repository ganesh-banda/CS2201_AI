from flask import Flask, render_template, request
import random
import string

app = Flask(__name__)

# function to generate captcha
def generate_captcha():
    letters = string.ascii_uppercase + string.digits
    captcha = ''.join(random.choice(letters) for i in range(5))
    return captcha

# store captcha
captcha_text = generate_captcha()

@app.route("/", methods=["GET", "POST"])
def index():
    global captcha_text
    message = ""

    if request.method == "POST":
        user_input = request.form["captcha"]

        if user_input == captcha_text:
            message = "✅ Correct CAPTCHA!"
        else:
            message = "❌ Wrong CAPTCHA!"

        captcha_text = generate_captcha()

    return render_template("index.html", captcha=captcha_text, message=message)

if __name__ == "__main__":
    app.run(debug=True)