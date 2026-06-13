from flask import Flask, render_template, request
import json

app = Flask(__name__)


# Load JSON files

with open("skills.json") as f:
    skills_data = json.load(f)

with open("courses.json") as f:
    courses_data = json.load(f)

with open("roadmap.json") as f:
    roadmap_data = json.load(f)



@app.route("/", methods=["GET", "POST"])
def home():

    if request.method == "POST":

        career = request.form["career"]

        user_skills = request.form["skills"]

        user_skills = [
            x.strip().lower()
            for x in user_skills.split(",")
        ]


        required_skills = skills_data[career]


        matched = []
        missing = []


        for skill in required_skills:

            if skill.lower() in user_skills:
                matched.append(skill)

            else:
                missing.append(skill)



        score = int(
            (len(matched) / len(required_skills)) * 100
        )


        courses = courses_data[career]


        roadmap = roadmap_data[career]



        return render_template(
            "result.html",
            score=score,
            missing=missing,
            courses=courses,
            roadmap=roadmap
        )



    return render_template(
        "index.html",
        careers=skills_data.keys()
    )



if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)