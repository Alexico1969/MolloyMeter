from flask import Flask, render_template, request, redirect, url_for, session
import io
import os
import base64
import matplotlib.pyplot as plt
import sqlite3
from database import create_db, print_db, add_question, get_question, update_question

# Initialize the database
create_db()
print("Database initialized")
print("Inserting temp data")
add_question("Best Movie", "Star Wars: A new Hope", "Shrek", "", "", "", "", "", "", "", "") 
print_db()
print("Checkpoint 01")


app = Flask(__name__)
app.secret_key = os.urandom(24)  # For security


question = ""
votes = [0,0,0,0,0,0,0,0,0,0]
choices = ["","","","","","","","","",""]


# storing temp values in list 'votes;' :
votes = [1,2,3,4,5,6,7,8,9,40]


@app.route('/', methods=['GET','POST'])
def home():
    question, choices = get_question()
    
    # Debug print statement
    print(f"&&& Choices: {choices}")
    
    # Sample votes, just as you mentioned
    votes = [1, 2, 3, 4, 5, 6, 7, 8, 9, 40]

    # Filter out empty choices and their corresponding votes
    filtered_choices = [choice for choice, vote in zip(choices, votes) if choice.strip() != ""]
    filtered_votes = [vote for choice, vote in zip(choices, votes) if choice.strip() != ""]

    # Generate the plot as an image
    fig, ax = plt.subplots()
    ax.barh(filtered_choices, filtered_votes, color='#18b8ec')
    ax.set_xlabel("VOTES")
    ax.set_title(question)
    plt.subplots_adjust(left=0.5)

    # Save the plot to a BytesIO object and encode it as base64
    buffer = io.BytesIO()
    fig.savefig(buffer, format='png')
    buffer.seek(0)
    img_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8')

    # Pass the base64 string to the template
    return render_template("home.html", img_base64=img_base64)


@app.route('/vote', methods=['GET','POST'])
def vote():

    if request.method == 'POST':
        pass
        if 'has_voted' in session:
            return "You've already voted!"
        else:
            # Save the vote (e.g., in a database or file)
            session['has_voted'] = True
            return "Thank you for voting!"
    
    


@app.route('/admin', methods=['GET', 'POST'])
def admin():
    data = get_question()
    question = data[0]
    choices = data[1]
    if request.method == 'POST':
        # Get the question and choices from the form
        question = request.form.get('question')
        choices = ["","","","","","","","","",""]
        for i in range(10):
            id = "choice" + str(i+1)
            inp_choice = request.form.get(id)
            if inp_choice != "":
                choices[i] = inp_choice

        update_question(question, choices[0], choices[1],choices[2],choices[3],choices[4],choices[5],choices[6],choices[7],choices[8],choices[9],)

        # printing the entire database:
        print_db()        

        return redirect(url_for('home'))
    
    return render_template('admin.html', question=question)




if __name__ == '__main__':
    app.run(debug=True)
