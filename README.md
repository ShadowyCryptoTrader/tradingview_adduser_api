# tradingview_adduser_api
Python selenium API to automate user access to your Trading View invite-only indicator.

1. This is a simple project that starts a Flask server containing only one endpoint.
2. The endpoint uses Selenium webdriver to automatically login to your trading view account and add a user to any of your invite-only indicators.
3. Set your own TradingView user and password AND keep it safe!

To test, simply send a post request to the endpoint and include in the message body the user to be added and the tradingview script name:

Postman example:

![image](https://user-images.githubusercontent.com/122331832/211453282-64442f90-24c0-4bfb-9142-3329245fa340.png)


Pending functionalities:

- Add the expiration date of the access.
- Add a delete user operation.

Other things to improve the code:

- Replace those ugly sleep() with Explicit waits: https://selenium-python.readthedocs.io/waits.html. Will improve performance and avoid issues when HTML elements are not fully loaded.
- Add security so that only you can access the API endpoint. (API key, etc..)
- Move the password to a SECURE properties file.
- Error handling, asynchronous messaging, retries, etc...


