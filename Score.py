import Utils

from pathlib import Path


def add_score(difficulty):
    POINTS_OF_WINNING = difficulty*3 + 5

    file_path = Path(Utils.SCORES_FILE_NAME)

    if file_path.exists():
        file = open(file_path,"r+")
        file.seek(0)
        score = int(file.read()) + POINTS_OF_WINNING

        file.seek(0)
        file.write(str(score))



    else:
        file = open(file_path, "w")
        file.write(str(POINTS_OF_WINNING))
    file.close()
