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
    # hedge load time 
    sleep( 2 )

    # id username input box
    login_field = driver.find_element( By.XPATH , x_login_field )
    # send username
    login_field.send_keys( user )
    # hedge type time
    sleep( 1 )

    # id password input box
    password_field = driver.find_element( By.XPATH , x_password_field )
    # send password
    password_field.send_keys( pwrd ) 
    # hedge type time
    sleep( 1 )

    # tag login button
    lets_log_into_twitter = driver.find_element( By.XPATH , x_login_button )
    # interact (click) with login button
    lets_log_into_twitter.click()
    # hedge request processing & site load times
    sleep( 2 )


def re_tweet( tweet ):
    '''
    uses Selenium ChromeDriver to retweet a tweet

    input) tweet you want to retweet
    '''
    # load the tweet 
    driver.get( tweet )
    # hedge load time
    sleep( 2 )

    # locate the retweet button
    re_tweet_ing = driver.find_element( By.XPATH , re_tweet_button )
    # and click it
    re_tweet_ing.click()
    # hedge load time
    sleep( 2 )

    # locate button to confirm the retweet 
    confirm_re_tweet_ing = driver.find_element( By.XPATH , confirm_re_tweet_button )
    # and confirm the retweet (a.k.a. click to retweet the tweet)
    confirm_re_tweet_ing.click()
    # then sleep so user can see load (if desired)
    sleep( 5 )


def re_tweet_this_tweet():
    '''
    times and executes login_to_twitter and re_tweet
    '''
    # function start time
    now = time.time()

    # get it poppin
    login_to_twitter()
    # and drop a rt
    re_tweet()
    
    # function end time
    then = time.time()  
    # close out with display of runtime to nearest sec
    return 'execution:', int( then - now ), 'seconds'


# let's do it
if __name__ == '__main__':
    # check that username and password are logical
    if len( user ) or len( pwrd ) < 1:
        # cause a ruckus if they're not
        raise Exception( 'illogical username or password'
                        '\nplease check you have correctly entered your login information - login_info.py'
                        f'\ncurrent user = { user } , current password = { pwrd }' ) 

    # input the link to your tweet of interest
    status_to_retweet = input( 'link to tweet: ' )

    # retweet the tweet of interest
    re_tweet_this_tweet( status_to_retweet )
