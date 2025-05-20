import math
import time
from selenium import webdriver
from selenium.webdriver.common.by import By


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


def main():
    driver = webdriver.Chrome()
    driver.get("http://suninjuly.github.io/alert_accept.html")

    driver.find_element(By.TAG_NAME, "button").click()
    time.sleep(1)
    driver.switch_to.alert.accept()

    time.sleep(1)

    x = driver.find_element(By.ID, "input_value").text
    answer = calc(x)

    driver.find_element(By.ID, "answer").send_keys(answer)
    driver.find_element(By.TAG_NAME, "button").click()

    time.sleep(5)
    print(driver.switch_to.alert.text)

    driver.quit()


if __name__ == "__main__":
    main()
