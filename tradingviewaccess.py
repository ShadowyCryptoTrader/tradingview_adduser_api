import json
import time

import math
import os

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.proxy import Proxy, ProxyType

from time import sleep


from flask import Flask, request, jsonify
app = Flask(__name__)


@app.route('/addusertotv/', methods=['POST'])
def addusertotv():

    param = request.data.decode('UTF-8')
    
    paramArray = param.split(",")
    
    usertoAdd = paramArray[0]
    cred_user = 'your_tradinvg_view_user'
    cred_pass = 'your_trading_view_password'
    indicator_path = "https://www.tradingview.com/script/" + paramArray[1]

    try:
        chrome_options = webdriver.ChromeOptions()
        chrome_options.binary_location = "/app/.apt/usr/bin/google-chrome"
        
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--no-sandbox")
        driver = webdriver.Chrome(executable_path="/app/.chromedriver/bin/chromedriver", chrome_options=chrome_options)
        
        driver.get("https://www.tradingview.com")
        sleep(1)
        #user icon
        driver.find_element(By.XPATH,"//div[@class='tv-header__area tv-header__area--user']/button").click()
        sleep(1)
        #sign-in button
        driver.find_element(By.XPATH,"//button[@data-name='header-user-menu-sign-in']").click()
        sleep(1)
        #email login button
        driver.find_element(By.XPATH,"//span[@class='tv-signin-dialog__social tv-signin-dialog__toggle-email js-show-email']").click()
        sleep(1)
        driver.find_element(By.XPATH,"//input[@autocomplete='username']").send_keys(cred_user)
        driver.find_element(By.XPATH,"//input[@autocomplete='current-password']").send_keys(cred_pass)
        #actual login
        driver.find_element(By.XPATH,"//button[@class='tv-button tv-button--size_large tv-button--primary tv-button--loader']").click()
        sleep(1)
        driver.get(indicator_path)
        sleep(2)
        try:
            #Hide watchlist (sidebar) since sometimes can cause issues
            driver.find_element(By.XPATH,"//div[@data-name='base']").click()
            sleep(0.5)
            driver.find_element(By.XPATH,"//div[@data-name='base' and contains(@class,'isActive')]").click()
        except Exception as a:
            print(a)
            print('Didnt find the element. Not an issue.') 
        sleep(0.5)
        #Section for adding users to the script
        driver.find_element(By.XPATH,"//button[@data-name='manage-access']").click()
        sleep(0.5)
        driver.find_element(By.XPATH,"//button[text()='Add new users']").click()
        sleep(1)
        text_input = driver.find_element(By.XPATH,"//input[@placeholder='Search for a user to grant them access']")
        ActionChains(driver).send_keys_to_element(text_input, usertoAdd + Keys.RETURN).perform()
        sleep(0.5)
        ActionChains(driver).send_keys_to_element(text_input, '-' + Keys.RETURN).perform()
        sleep(2.5)
        driver.find_element(By.XPATH,"//span[text()='Add access']").click()
        sleep(0.5)
        driver.find_element(By.XPATH,"//button[@data-name='submit-button' and @name='submit']").click()  
        sleep(1)
        #Logout to avoid leaving open sessions
        driver.find_element(By.XPATH,"//button[@class='tv-header__user-menu-button tv-header__user-menu-button--logged js-header-user-menu-button']").click()
        sleep(0.5)
        try:
            driver.find_element(By.XPATH,"//button[@data-name='header-user-menu-sign-out']").click()
        except Exception as a:
            print(a)
            print('Error doing logout. not too bad...') 
        sleep(0.5)
    except Exception as g:
        driver.quit()
        print('Exception jodiendo con chrome')
        print(g)    
    
    driver.quit()     
    
    return jsonify({
            "Message": "User added: " + usertoAdd + "!!",
            "METHOD" : "POST"
    })
    
    
    print("end...")


# A welcome message to test the server
@app.route('/')
def index():
    return "<h1>Server started !!</h1>"


if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run(threaded=True, port=5000)

