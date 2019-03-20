from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

'''
set up setup and define constants (paths)
'''
# driver setup
options = webdriver.FirefoxOptions()  
options.set_preference( 'dom.push.enabled' , False )  # blocks popups 
# site
twitter_login_page = 'https://twitter.com/login'
# paths
user_box = '.js-username-field'
pass_box = '.js-password-field'
login_button = 'button.submit'
tweet_box = '#tweet-box-home-timeline'  
tweet_button = 'form.tweet-form:nth-child(2) > div:nth-child(3) > div:nth-child(2) > button:nth-child(2)'
# user
user = ''  # your account here
pwrd = ''  # your password here


class Tweet:
    def __init__( self , username , password , status ):
        self.username = username
        self.password = password
        self.status = status
    '''
    1) log in to twitter
    2) locate and engage tweet box
    3) send tweet (keys) to tweet box
    4) tweet
    '''

    def set_browser( self ):
        # set driver
        self.driver = webdriver.Firefox( options=options ) 
    
    def login( self ):
        # get login page
        self.driver.get( twitter_login_page ) 
        sleep( 1 )
        # send username
        self.driver.find_element_by_css_selector( user_box ).send_keys( self.username )
        sleep( 1 )
        # send password
        self.driver.find_element_by_css_selector( pass_box ).send_keys( self.password )
        sleep( 1 )
        # login
        self.driver.find_element_by_css_selector( login_button ).click()
        sleep( 2 )
    
    def send_status( self ):
        # send status
        self.driver.find_element_by_css_selector( tweet_box ).send_keys( self.status )
        sleep( 1 )
        # tweet
        self.driver.find_element_by_css_selector( tweet_button ).click()
        sleep( 5 )
    
    def close_browser( self ):
        # close browser
        self.driver.close()
    
    def run_all( self ):
        self.set_browser()
        self.login()
        self.send_status()
        self.close_browser()
        # report
        return f'sent tweet: { self.status } \nto account: { self.username }'


my_tweet = input( 'status? ' )
if len( my_tweet ) > 280:
    raise Exception( f'tweet too long { len( my_tweet ) }' )
print( Tweet( user , pwrd , my_tweet ).run_all() )
