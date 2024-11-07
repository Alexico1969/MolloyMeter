import sqlite3


def create_db(db_name="quiz.db"):
    """Create the database and set up the tables."""
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()


    # Create 'question_and_choices' table
    cursor.execute('''CREATE TABLE IF NOT EXISTS question_and_choices (
                        question TEXT NOT NULL,
                        choice01 TEXT NOT NULL,
                        choice02 TEXT NOT NULL,
                        choice03 TEXT NOT NULL,
                        choice04 TEXT NOT NULL,
                        choice05 TEXT NOT NULL,
                        choice06 TEXT NOT NULL,
                        choice07 TEXT NOT NULL,
                        choice08 TEXT NOT NULL,
                        choice09 TEXT NOT NULL,
                        choice10 TEXT NOT NULL
                   )''')




    conn.commit()
    conn.close()
    print(f"Database '{db_name}' created with table 'question_and_choices'.")


def add_question(question, choices, db_name="quiz.db"):
    """Insert a question and 10 associated choices into the database."""
    if len(choices) != 10:
        raise ValueError("Exactly 10 choices are required.")


    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()


    # Insert the question and choices
    cursor.execute('''INSERT INTO question_and_choices 
                      (question, choice01, choice02, choice03, choice04, choice05, choice06, choice07, choice08, choice09, choice10)
                      VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''', 
                   (question, *choices))


    conn.commit()
    conn.close()
    print(f"Question '{question}' and its choices added.")


def get_question():
    """Retrieve a question and its choices by the question text."""
    conn = sqlite3.connect("quiz.db")
    cursor = conn.cursor()


    # Retrieve the question and its choices
    cursor.execute("SELECT * FROM question_and_choices WHERE question = ?", (question_text,))
    question_row = cursor.fetchone()


    conn.close()
    
    if question_row:
        question = question_row[0]
        choices = question_row[1:]  # All choices
        return question, choices
    else:
        print(f"Question '{question_text}' not found.")
        return None, None


def update_question(old_question, new_question, db_name="quiz.db"):
    """Update the question text."""
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()


    cursor.execute("UPDATE question_and_choices SET question = ? WHERE question = ?", (new_question, old_question))


    conn.commit()
    conn.close()
    print(f"Question '{old_question}' updated to '{new_question}'.")


def delete_question(question_text, db_name="quiz.db"):
    """Delete a question and its choices by the question text."""
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()


    # Delete the question and its associated choices
    cursor.execute("DELETE FROM question_and_choices WHERE question = ?", (question_text,))


    conn.commit()
    conn.close()
    print(f"Question '{question_text}' and its choices deleted.")

def print_db(db_name="quiz.db"):
    """Print all the questions and their associated choices from the database."""
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    # Retrieve all info
    cursor.execute("SELECT * FROM question_and_choices")
    questions = cursor.fetchall()
    print()
    print("*** Database data: ***")
    print()
    for el in questions:
        print(">", el)
    
    conn.close()



