from flask import Flask, request, jsonify
import sqlite3
from model import score_idea

app = Flask(__name__)

# Initialize DB
def init_db():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS ideas
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  title TEXT,
                  description TEXT,
                  score INTEGER)''')
    conn.commit()
    conn.close()

init_db()

# Submit Idea
@app.route('/submit', methods=['POST'])
def submit_idea():
    data = request.json
    title = data['title']
    description = data['description']

    score = score_idea(description)

    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("INSERT INTO ideas (title, description, score) VALUES (?, ?, ?)",
              (title, description, score))
    conn.commit()
    conn.close()

    return jsonify({"message": "Idea submitted!", "score": score})

# Get Ideas
@app.route('/ideas', methods=['GET'])
def get_ideas():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("SELECT * FROM ideas ORDER BY score DESC")
    rows = c.fetchall()
    conn.close()

    ideas = []
    for row in rows:
        ideas.append({
            "id": row[0],
            "title": row[1],
            "description": row[2],
            "score": row[3]
        })

    return jsonify(ideas)

if __name__ == '__main__':
    app.run(debug=True)
