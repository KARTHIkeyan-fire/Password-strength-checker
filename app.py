from flask import Flask, render_template, request
import string

app = Flask(__name__)

def check_pwd(password):
    strength = 0
    remarks = ""
    lower_count = upper_count = num_count = wspace_count = special_count = 0

    for char in list(password):
        if char in string.ascii_lowercase:
            lower_count += 1
        elif char in string.ascii_uppercase:
            upper_count += 1
        elif char in string.digits:
            num_count += 1
        elif char == ' ':
            wspace_count += 1
        else:
            special_count += 1

    if lower_count >= 1: strength += 1
    if upper_count >= 1: strength += 1
    if num_count >= 1: strength += 1
    if wspace_count >= 1: strength += 1
    if special_count >= 1: strength += 1

    if strength == 1:
        remarks = "⚠️ Very Bad Password!!! Change ASAP"
    elif strength == 2:
        remarks = "⚠️ Not A Good Password!!! Change ASAP"
    elif strength == 3:
        remarks = "❗ It's a weak password, consider changing"
    elif strength == 4:
        remarks = "👍 It's a hard password, but can be better"
    elif strength == 5:
        remarks = "✅ A very strong password"

    return {
        "lower": lower_count,
        "upper": upper_count,
        "num": num_count,
        "space": wspace_count,
        "special": special_count,
        "strength": strength,
        "remarks": remarks
    }

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    if request.method == "POST":
        password = request.form["password"]
        result = check_pwd(password)
    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
