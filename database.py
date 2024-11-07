import sqlite3

def create_db(db_name="quiz.db"):
    """Create the database and set up the tables."""
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

    # Create 'questions' table
    cursor.execute('''CREATE TABLE IF NOT EXISTS questions (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        question_text TEXT NOT NULL)''')

    # Create 'choices' table
    cursor.execute('''CREATE TABLE IF NOT EXISTS choices (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        question_id INTEGER,
                        choice_text TEXT NOT NULL,
                        votes INTEGER DEFAULT 0,
                        FOREIGN KEY (question_id) REFERENCES questions (id))''')

    conn.commit()
    conn.close()
    print(f"Database '{db_name}' created with tables 'questions' and 'choices'.")

def add_question(question_text, choices, db_name="quiz.db"):
    """Insert a question and its choices into the database."""
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

    # Insert the question
    cursor.execute("INSERT INTO questions (question_text) VALUES (?)", (question_text,))
    question_id = cursor.lastrowid

    # Insert each choice for the question
    for choice in choices:
        cursor.execute("INSERT INTO choices (question_id, choice_text) VALUES (?, ?)", (question_id, choice))

    conn.commit()
    conn.close()
    print(f"Question '{question_text}' and choices added.")

def get_question(q_id, db_name="quiz.db"):
    """Retrieve a question and its choices by question ID."""
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

    # Get the question
    cursor.execute("SELECT * FROM questions WHERE id = ?", (q_id,))
    question = cursor.fetchone()

    # Get the choices for the question
    cursor.execute("SELECT * FROM choices WHERE question_id = ?", (q_id,))
    choices = cursor.fetchall()

    conn.close()
    return question, choices

def update_question(q_id, new_text, db_name="quiz.db"):
    """Update a question's text by ID."""
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

    cursor.execute("UPDATE questions SET question_text = ? WHERE id = ?", (new_text, q_id))

    conn.commit()
    conn.close()
    print(f"Question ID {q_id} updated.")

def update_choice(c_id, new_text, db_name="quiz.db"):
    """Update a choice's text by ID."""
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

    cursor.execute("UPDATE choices SET choice_text = ? WHERE id = ?", (new_text, c_id))

    conn.commit()
    conn.close()
    print(f"Choice ID {c_id} updated.")

def delete_question(q_id, db_name="quiz.db"):
    """Delete a question and its choices by question ID."""
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

    # Delete related choices first
    cursor.execute("DELETE FROM choices WHERE question_id = ?", (q_id,))

    # Delete the question
    cursor.execute("DELETE FROM questions WHERE id = ?", (q_id,))

    conn.commit()
    conn.close()
    print(f"Question ID {q_id} and its choices deleted.")

def delete_choice(c_id, db_name="quiz.db"):
    """Delete a choice by choice ID."""
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

    cursor.execute("DELETE FROM choices WHERE id = ?", (c_id,))

    conn.commit()
    conn.close()
    print(f"Choice ID {c_id} deleted.")
