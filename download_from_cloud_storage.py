import os, re, sys, time, errno, configparser
# from bs4 import BeautifulSoup
from selenium.webdriver import Chrome, ChromeOptions, Remote
# from selenium.webdriver.common.action_chains import ActionChains
# from selenium.common.exceptions import NoSuchElementException


def login(driver, root_url, user_id, password):
    print("Log in to ", root_url, "with the account of", user_id, ".")
    # driver.get(root_url + "login")
    driver.get('https://gopro.com/login')
    time.sleep(4)

    login_inputs = driver.find_elements_by_class_name('gp-input-lg')
    login_inputs[0].send_keys(user_id)
    time.sleep(2)
    login_inputs[1].send_keys(password)
    time.sleep(2)

    target = driver.find_element_by_xpath("//*[@id='gptest-login-btn']")
    driver.execute_script("arguments[0].click();", target)
    time.sleep(4)


def select_timelapse(driver):
    print("Select a latest timelapse.")
    driver.get('https://plus.gopro.com/media-library/')
    time.sleep(3)
    target = driver.find_element_by_xpath("//*[@class='grid-item-thumbnail']")
    driver.execute_script("arguments[0].click();", target)
    time.sleep(2)


def download(driver):
    print("Download a latest timelapse.")
    driver.get('https://plus.gopro.com/media-library/o61ERB8329Jq2')
    time.sleep(3)
    print(driver.current_url)

    # timelapse_id = 'o61ERB8329Jq2'
    # driver.find_element_by_id('gp-media-detail-kebab-menu-' + timelapse_id).click()
    target = driver.find_element_by_xpath("//*[@id='gp-media-detail-kebab-menu-o61ERB8329Jq2']")
    driver.execute_script("arguments[0].click();", target)
    time.sleep(2)
    target = driver.find_elements_by_xpath("//*[@class='download-option']")
    driver.execute_script("arguments[1].click();", target)


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
    # executable_path = config_default.get('EXECUTABLE_PATH')

    options = ChromeOptions()
    options.add_argument('--headless')
    # driver = Chrome(executable_path=executable_path, options=options)
    driver = Remote(command_executor='http://localhost:4444/wd/hub',
                    desired_capabilities=options.to_capabilities(),
                    options=options)

    login(driver, root_url, user_id, password)
    # select_timelapse(driver)
    download(driver)

    driver.quit()


if __name__ == '__main__':
    main()
