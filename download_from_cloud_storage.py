import os, re, sys, time, errno, configparser
# from bs4 import BeautifulSoup
from selenium.webdriver import Chrome, ChromeOptions
# from selenium.webdriver.common.action_chains import ActionChains
# from selenium.common.exceptions import NoSuchElementException


def login(driver, root_url, user_id, password):
    print("Log in to ", root_url, "with the account of", user_id, ".")
    driver.get(root_url + "login")
    time.sleep(3)

    login_inputs = driver.find_elements_by_class_name("gp-input-lg")
    login_inputs[0].send_keys(user_id)
    time.sleep(2)
    login_inputs[1].send_keys(password)
    time.sleep(2)

    driver.find_element_by_id("gptest-login-btn").click()
    time.sleep(3)


def select_timelapse(driver):
    print("Select a latest timelapse.")
    driver.find_element_by_class_name("grid-item-thumbnail").click()
    time.sleep(5)


def download(driver):
    print("Download a latest timelapse.")
    timelapse_id = "o61ERB8329Jq2"
    driver.find_element_by_id("gp-media-detail-kebab-menu-" + timelapse_id).click()
    time.sleep(5)
    download_options = driver.find_elements_by_class_name("download-option")
    download_options[1].click()


def main():
    config_ini = configparser.ConfigParser()
    config_filepath = 'config.ini'
    if not os.path.exists(config_filepath):
        raise FileNotFoundError(errno.ENOENT, os.strerror(errno.ENOENT), config_filepath)
    config_ini.read(config_filepath, encoding='utf-8')
    config_default = config_ini['DEFAULT']

    root_url = config_default.get('ROOT_URL')
    user_id = config_default.get('USER_ID')
    password = config_default.get('PASSWORD')
    executable_path = config_default.get('EXECUTABLE_PATH')

    options = ChromeOptions()
    options.add_argument('--headless')
    driver = Chrome(executable_path=executable_path, options=options)

    login(driver, root_url, user_id, password)
    select_timelapse(driver)
    download(driver)

    driver.quit()


if __name__ == '__main__':
    main()
