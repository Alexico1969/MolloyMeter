from flask import Flask, render_template, request, redirect, url_for, session
import io
import os
import base64
import matplotlib.pyplot as plt
import sqlite3
from database import create_db, add_question, get_question, update_question, update_choice, delete_question, delete_choice

# Initialize the database
create_db()

app = Flask(__name__)
app.secret_key = os.urandom(24)  # For security

questions = {}
votes = []
choices = ["","","","","","","","","",""]

# storing temp values in list 'votes;' :

try:
    questions = session.get('questions')
except:
    print("No questions stored in sessions, keeping default values")

try:
    stored_choices = session.get('choices')
except:
    print("No choices stored in sessions, keeping default values")

votes = [10,3,3,2,1,8,-1,-1,-1,-1]



@app.route('/')
def home():
    # Filter out invalid choices (empty strings) and corresponding votes (-1)
    filtered_choices = [choice for choice, vote in zip(choices, votes) if choice.strip() != "" and vote != -1]
    filtered_votes = [vote for choice, vote in zip(choices, votes) if choice.strip() != "" and vote != -1]

    print("Filtered Choices:", filtered_choices)  # Debugging statement
    print("Filtered Votes:", filtered_votes)      # Debugging statement

    # Generate the plot as an image
    fig, ax = plt.subplots()
    ax.barh(filtered_choices, filtered_votes, color='#18b8ec')
    ax.set_xlabel('Votes')
    ax.set_title('Voting Results')

    # Save the plot to a BytesIO object and encode it as base64
    buffer = io.BytesIO()
    fig.savefig(buffer, format='png')
    buffer.seek(0)
    img_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8')

    # Pass the base64 string to the template
    return render_template("home.html", img_base64=img_base64)


@app.route('/vote', methods=['POST'])
def vote():
    if 'has_voted' in session:
        return "You've already voted!"
    else:
        # Save the vote (e.g., in a database or file)
        session['has_voted'] = True
        return "Thank you for voting!"

@app.route('/admin', methods=['GET', 'POST'])
def admin():
    question, choices = get_question(1)
    if request.method == 'POST':
        # Get the question and choices from the form
        question_text = request.form.get('question')

        for i in range(10):
            id = "choice" + str(i+1)
            inp_choice = request.form.get(id)
            if inp_choice != "":
                choices[i] = inp_choice
        
        # Store the question and choices (could also add unique ID for multiple questions)
        questions['current_question'] = {
            'question_text': question_text,
            'choices': choices,
        }

        session['questions'] = questions
        session['choices'] = choices
        add_question("What's your favorite programming language?", ["Python", "JavaScript", "Java", "C++"])



        print("Question and choices have been set successfully!")
        return redirect(url_for('home'))
    
    return render_template('admin.html', question=question)


if __name__ == '__main__':
    app.run(debug=True)