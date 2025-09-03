from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# In-memory storage (later replace with DB)
workouts = []

@app.route('/')
def home():
    return render_template("index.html", workouts=workouts)

@app.route('/add', methods=['POST'])
def add_workout():
    workout = request.form.get("workout")
    duration = request.form.get("duration")

    if workout and duration.isdigit():
        workouts.append({"workout": workout, "duration": int(duration)})
    return redirect(url_for("home"))

if __name__ == '__main__':
    app.run(debug=True)


from flask import Flask

def create_gymtrainer():
    app = Flask(__name__)

    @app.route('/')
    def index():
        return "Welcome to GymTrainer!"

    return app

