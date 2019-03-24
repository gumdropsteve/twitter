import time
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from login_info import user, pwrd

# ChromeDiver set up (for no notifications)
chrome_options = webdriver.ChromeOptions()   
prefs = { 'profile.default_content_setting_values.notifications': 2 }
chrome_options.add_experimental_option( 'prefs' , prefs )


def login_to_twitter():
    from paths import login_page, x_login_field, x_password_field, x_login_button
    '''
    uses Selenium ChromeDriver to log in to Twitter
    '''
    # make driver
    driver = webdriver.Chrome( options=chrome_options )  # disables notifications (thanks @najbot)

    # get login page
    driver.get( twitter_login_page )
    sleep( 2 )

    # send username
    login_field = driver.find_element( By.XPATH , x_login_field )
    login_field.send_keys( user )
    sleep( 1 )

    # send password
    password_field = driver.find_element( By.XPATH , x_password_field )
    password_field.send_keys( pwrd ) 
    sleep( 1 )

    # login
    lets_log_into_twitter = driver.find_element( By.XPATH , x_login_button )
    lets_log_into_twitter.click()
    sleep( 2 )


def re_tweet( tweet ):
    '''
    uses Selenium ChromeDriver to retweet a tweet

    input) tweet you want to retweet
    '''
    # load the tweet 
    driver.get( tweet )
    sleep( 2 )

    # locate and click the retweet button
    re_tweet_ing = driver.find_element( By.XPATH , re_tweet_button )
    re_tweet_ing.click()
    sleep( 2 )

    # confirm the retweet and retweet
    confirm_re_tweet_ing = driver.find_element( By.XPATH , confirm_re_tweet_button )
    confirm_re_tweet_ing.click()
    # sleep so user can see load (if desired)
    sleep( 5 )


def re_tweet_this_tweet():
    '''
    times and executes login_to_twitter and re_tweet
    '''
    # function start time
    now = time.time()

    # function
    login_to_twitter()
    re_tweet()
    
    # function end time
    then = time.time()  

    return 'execution:', then - now, 'seconds'


# check that username and password are logical
if len( user ) or len( pwrd ) < 1:
    raise Exception('illogical username or password'
                    '\nplease check you have correctly entered your login information - login_info.py'
                    f'\ncurrent user = {user} , current password = {pwrd}') 

# input the link to your tweet of interest
status_to_retweet = input( 'link to tweet: ' )

# retweet the tweet of interest
re_tweet_this_tweet( status_to_retweet )
