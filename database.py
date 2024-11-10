import sqlite3


def create_db(db_name="quiz.db"):
    """Create the database and set up the tables."""
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()


    # Create 'question_and_choices' table
    cursor.execute('''CREATE TABLE IF NOT EXISTS question_and_choices (
                        id INTEGER,      
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


def add_question(db_name="quiz.db", question="", O1="", O2="", O3="", O4="", O5="", O6="", O7="", O8="", O9="", O10=""):
    """Insert a new entry into the question_and_choices table with id set to 1."""
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    cursor.execute(f"DROP TABLE IF EXISTS question_and_choices")
    cursor.execute('''CREATE TABLE IF NOT EXISTS question_and_choices (
                            id INTEGER,      
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
    # Insert a new row with id = 1
    cursor.execute('''INSERT INTO question_and_choices 
                      (id, question, choice01, choice02, choice03, choice04, choice05, 
                       choice06, choice07, choice08, choice09, choice10)
                      VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''', 
                   (1, question, O1, O2, O3, O4, O5, O6, O7, O8, O9, O10))

    conn.commit()
    conn.close()
    print(f"Entry added with id = 1 for question '{question}' and choices.")


def get_question():
    """Retrieve a question and its choices by the question text."""
    conn = sqlite3.connect("quiz.db")
    cursor = conn.cursor()


    # Retrieve the question and its choices
    cursor.execute("SELECT * FROM question_and_choices ")
    question_row = cursor.fetchone()


    conn.close()
    
    if question_row:
        id = question_row[0]
        question = question_row[1]
        choices = question_row[2:]  # All choices
        return question, choices
    else:
        print(f"Question '{question_text}' not found.")
        return None, None


def update_question(question, O1, O2, O3, O4, O5, O6, O7, O8, O9, O10):
    """Update the question text."""
    conn = sqlite3.connect("quiz.db")
    cursor = conn.cursor()
    cursor.execute("UPDATE question_and_choices SET question = ? WHERE id = ?", (question, 1))
    cursor.execute("UPDATE question_and_choices SET choice01 = ? WHERE id = ?", (O1, 1))
    cursor.execute("UPDATE question_and_choices SET choice02 = ? WHERE id = ?", (O2, 1))
    cursor.execute("UPDATE question_and_choices SET choice03 = ? WHERE id = ?", (O3, 1))
    cursor.execute("UPDATE question_and_choices SET choice04 = ? WHERE id = ?", (O4, 1))
    cursor.execute("UPDATE question_and_choices SET choice05 = ? WHERE id = ?", (O5, 1))
    cursor.execute("UPDATE question_and_choices SET choice06 = ? WHERE id = ?", (O6, 1))
    cursor.execute("UPDATE question_and_choices SET choice07 = ? WHERE id = ?", (O7, 1))
    cursor.execute("UPDATE question_and_choices SET choice08 = ? WHERE id = ?", (O8, 1))
    cursor.execute("UPDATE question_and_choices SET choice09 = ? WHERE id = ?", (O9, 1))
    cursor.execute("UPDATE question_and_choices SET choice10 = ? WHERE id = ?", (O10, 1))
    conn.commit()
    conn.close()
    print(f"New question: {question}")


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



