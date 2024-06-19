import sys
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

CHROME_DRIVER_PATH = "C:\\Users\\David\\Desktop\\DevOps\\Chrome\\chromedriver-win64\\chromedriver.exe"


def test_scores_service(url):
    driver = None
    try:

        s = Service(CHROME_DRIVER_PATH)
        driver = webdriver.Chrome(service=s)
        driver.get(url)


        score_element = driver.find_element(By.ID, "score")
        score = int(score_element.text)


        result = 1 <= score <= 1000
    except Exception as e:
        print(f"An error occurred: {e}")
        result = False
    finally:
        if driver:
            driver.quit()

    return result


def main_function():
    url = "http://127.0.0.1:8777/Score"
    if test_scores_service(url):
        print("Test passed.")
        sys.exit(0)
    else:
        print("Test failed.")
        sys.exit(-1)


if __name__ == "__main__":
    main_function()