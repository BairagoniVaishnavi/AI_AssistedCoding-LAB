from flask import Flask, render_template, request
import re
import html

app = Flask(__name__)

feedback_data = []

def is_valid_email(email):
    pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
    return re.match(pattern, email)

def sanitize_input(text):
    return html.escape(text.strip())

@app.route("/", methods=["GET"])
def home():
    return render_template("index.html", message=None, error=None)

@app.route("/submit", methods=["POST"])
def submit():
    try:
        name = request.form.get("name", "").strip()
        email = request.form.get("email", "").strip()
        feedback = request.form.get("feedback", "").strip()

        if not name or not email or not feedback:
            return render_template("index.html", error="All fields are required!", message=None)

        if len(name) > 100 or len(email) > 100 or len(feedback) > 500:
            return render_template("index.html", error="Input too long!", message=None)

        if not is_valid_email(email):
            return render_template("index.html", error="Invalid email format!", message=None)

        name = sanitize_input(name)
        email = sanitize_input(email)
        feedback = sanitize_input(feedback)

        feedback_data.append({
            "name": name,
            "email": email,
            "feedback": feedback
        })

        return render_template("index.html", message="Feedback submitted successfully!", error=None)

    except Exception:
        return render_template("index.html", error="Something went wrong.", message=None)

if __name__ == "__main__":
    app.run(debug=True)