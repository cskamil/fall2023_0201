from flask import Flask, render_template

app = Flask(__name__)

@app.route("/hello_for_loops")
def hello_world_template():

    student_1 = {'name': 'Student-1', 'score': 90}
    student_2 = {'name': 'Student-2', 'score': 80}
    
    student_list = [student_1, student_2]

    return render_template('for_loop.html', 
                           students = student_list,
                           max_score = 100)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)

