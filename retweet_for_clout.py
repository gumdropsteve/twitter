def re_tweet_this_tweet(tweet):
    import time
    from time import sleep
    from selenium import webdriver
    from selenium.webdriver.common.by import By

    now = time.time()  # function start time

    # diver set up
    chrome_options = webdriver.ChromeOptions()  # set up driver for no notifications
    prefs = {"profile.default_content_setting_values.notifications": 2}
    chrome_options.add_experimental_option("prefs", prefs)
    driver = webdriver.Chrome(options=chrome_options)  # disables notifications (thanks @najbot)

    # twitter xpath(s)
    twitter_login_page = 'https://twitter.com/login'
    twitter_login_field = '/html/body/div[1]/div[2]/div/div/div[1]/form/fieldset/div[1]/input'
    twitter_password_field = '/html/body/div[1]/div[2]/div/div/div[1]/form/fieldset/div[2]/input'
    twitter_login_button = '/html/body/div[1]/div[2]/div/div/div[1]/form/div[2]/button'
    re_tweet_button = '/html/body/div[45]/div[2]/div[3]/div/div/div[1]/div[1]/div/div[4]/div[2]/div[2]/button[1]'
    confirm_re_tweet_button = '//*[@id="retweet-tweet-dialog-dialog"]/div[2]/form/div[2]/div[3]/button/span[1]'

    # account info
    account_email = 'YOUR EMAIL HERE'  # email or handle
    account_password = 'YOUR PASSWORD HERE'  # password

    def login_to_twitter():
        driver.get(twitter_login_page)
        driver.maximize_window()
        sleep(2)
        login_field = driver.find_element(By.XPATH, twitter_login_field)
        login_field.send_keys(account_email)
        sleep(2)
        password_field = driver.find_element(By.XPATH, twitter_password_field)
        password_field.send_keys(account_password)
        sleep(2)
        lets_log_into_twitter = driver.find_element(By.XPATH, twitter_login_button)
        lets_log_into_twitter.click()
        sleep(2)

    def re_tweet():
        driver.get(tweet)
        sleep(2)
        re_tweet_ing = driver.find_element(By.XPATH, re_tweet_button)
        re_tweet_ing.click()
        sleep(2)
        confirm_re_tweet_ing = driver.find_element(By.XPATH, confirm_re_tweet_button)
        confirm_re_tweet_ing.click()
        sleep(2)

    # function
    login_to_twitter()
    re_tweet()
    
    print('task completed..')
    then = time.time()  # function end time
    print('execution:', then - now, 'seconds')
    return


# status_to_retweet = ''
# re_tweet_this_tweet(status_to_retweet)
