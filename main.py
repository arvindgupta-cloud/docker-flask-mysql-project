from flask import Flask, request, render_template_string
import mysql.connector

app = Flask(__name__)

# MySQL connection details
DB_CONFIG = {
    "host": "mysql",       # change to your container name if different
    "user": "root",
    "password": "admin",
    "port": 3306,
    "database": "flask_db"
}

# HTML template with comment form on left, comments list on right
HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>Comment App</title>
    <style>
        .container { display: flex; }
        .left { width: 40%; padding: 10px; }
        .right { width: 60%; padding: 10px; border-left: 1px solid #ccc; }
        textarea { width: 100%; height: 100px; }
        input[type=submit] { padding: 8px 12px; margin-top: 5px; }
        h2 { margin-top: 0; }
        .comment { border-bottom: 1px solid #eee; padding: 5px 0; }
    </style>
</head>
<body>
    <div class="container">
        <div class="left">
            <h2>Write a Comment</h2>
            <form method="POST">
                <textarea name="comment" required></textarea><br>
                <input type="submit" value="Submit">
            </form>
        </div>
        <div class="right">
            <h2>All Comments</h2>
            {% for comment in comments %}
                <div class="comment">{{ comment[0] }}</div>
            {% endfor %}
        </div>
    </div>
</body>
</html>
"""

@app.route('/', methods=['GET', 'POST'])
def home():
    comments = []
    try:
        # Connect to MySQL
        conn = mysql.connector.connect(**DB_CONFIG)
        cursor = conn.cursor()

        # Handle form submission
        if request.method == 'POST':
            comment_text = request.form['comment']
            cursor.execute("INSERT INTO messages (text) VALUES (%s)", (comment_text,))
            conn.commit()

        # Fetch all comments
        cursor.execute("SELECT text FROM messages ORDER BY id DESC")
        comments = cursor.fetchall()

        cursor.close()
        conn.close()
    except Exception as e:
        return f"❌ Database Connection Failed: {e}"

    # Render HTML with comments
    return render_template_string(HTML_TEMPLATE, comments=comments)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
