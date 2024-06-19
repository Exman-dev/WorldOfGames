from flask import Flask, render_template_string
import Utils

app = Flask(__name__)

SCORE_FILE_PATH = Utils.SCORES_FILE_NAME

@app.route('/Score')
def score_server():
    try:
        with open(SCORE_FILE_PATH, 'r') as file:
            score = file.read().strip()
            html_content = f"""
            <html>
            <head>
            <title>Scores Game</title>
            </head>
            <body>
            <h1>The score is <div id="score">{score}</div></h1>
            </body>
            </html>
            """
    except Exception as e:
        error_message = str(e)
        html_content = f"""
        <html>
        <head>
        <title>Scores Game</title>
        </head>
        <body>
        <h1><div id="score" style="color:red">{error_message}</div></h1>
        </body>
        </html>
        """
    return render_template_string(html_content)

if __name__ == '__main__':
    app.run(debug=True)
