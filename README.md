# tradingview_adduser_api
Python selenium API to automate user access to your Trading View invite-only indicator.

1. This is a simple project that starts a Flask server containing only one endpoint.
2. The endpoint uses Selenium webdriver to automatically login to your trading view account and add a user to any of your invite-only indicators.
3. Set your own TradingView user and password AND keep it safe!

To test, simply send a post request to the endpoint and include in the message body the user to be added and the tradingview script name:



![image](https://user-images.githubusercontent.com/122331832/211453282-64442f90-24c0-4bfb-9142-3329245fa340.png)



Things to improve:

- Add the expiration date of the access.
- Add security so that only you can access the API endpoint. (API key, etc..)
- Add a delete user operation.
- Move the password to a SECURE properties file.
- Error handling, asynchronous messaging, retries, etc...


