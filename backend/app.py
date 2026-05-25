from flask import Flask, request, jsonify
from flask_cors import CORS
import pymysql
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
CORS(app)

def get_db_connection():
    return pymysql.connect(
        host=os.getenv("DB_HOST"),
        port=int(os.getenv("DB_PORT", 3306)),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_NAME"),
        cursorclass=pymysql.cursors.DictCursor
    )

@app.route("/", methods=["GET"])
def home():
    return jsonify({"message": "FixBoard API is running"})

@app.route("/issues", methods=["GET"])
def get_issues():
    try:
        connection = get_db_connection()
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM issues ORDER BY created_at DESC")
            issues = cursor.fetchall()
        connection.close()
        return jsonify(issues), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/issues", methods=["POST"])
def create_issue():
    try:
        data = request.get_json()

        title = data.get("title")
        description = data.get("description")
        category = data.get("category")

        if not title or not description or not category:
            return jsonify({"error": "Title, description, and category are required"}), 400

        connection = get_db_connection()
        with connection.cursor() as cursor:
            sql = """
            INSERT INTO issues (title, description, category)
            VALUES (%s, %s, %s)
            """
            cursor.execute(sql, (title, description, category))
            connection.commit()

        connection.close()
        return jsonify({"message": "Issue created successfully"}), 201

    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/issues/<int:issue_id>", methods=["PUT"])
def update_issue_status(issue_id):
    try:
        data = request.get_json()
        status = data.get("status")

        if not status:
            return jsonify({"error": "Status is required"}), 400

        connection = get_db_connection()
        with connection.cursor() as cursor:
            sql = "UPDATE issues SET status = %s WHERE id = %s"
            cursor.execute(sql, (status, issue_id))
            connection.commit()

        connection.close()
        return jsonify({"message": "Issue status updated successfully"}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/issues/<int:issue_id>", methods=["DELETE"])
def delete_issue(issue_id):
    try:
        connection = get_db_connection()
        with connection.cursor() as cursor:
            sql = "DELETE FROM issues WHERE id = %s"
            cursor.execute(sql, (issue_id,))
            connection.commit()

        connection.close()
        return jsonify({"message": "Issue deleted successfully"}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)