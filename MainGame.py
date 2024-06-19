import threading
import MainScore
from Live import welcome, load_game

def run_flask_app():
    MainScore.app.run(debug=True, use_reloader=False)

if __name__ == "__main__":

    flask_thread = threading.Thread(target=run_flask_app)
    flask_thread.start()


    print(welcome("Guy"))
    load_game()
