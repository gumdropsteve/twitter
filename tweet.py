from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from user_info import u , p  # delete this line , or make a user_info file

'''
set up setup and define constants (paths)
  - done here for easy editing 
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
user = u  # your account here
pwrd = p  # your password here


class Tweet:
    '''
    simple overview:
        1) open browser
        2) log in to twitter
        3) locate and engage tweet box
        4) send tweet (keys) to tweet box
        5) tweet
    note: 
        sleep included for loadtimes
    '''

    def __init__( self , username , password , status ):
        self.username = username
        self.password = password
        self.status = status

    def set_browser( self ):
        # set driver (GeckoDriver) using previously defined options
        # done here to avoid browser popping up before status is set
        self.driver = webdriver.Firefox( options=options ) 
    
    def login( self ):
        # load login page
        self.driver.get( twitter_login_page ) 
        sleep( 1 )
        # send username to username input box
        self.driver.find_element_by_css_selector( user_box ).send_keys( self.username )
        sleep( 1 )
        # send password to password input box
        self.driver.find_element_by_css_selector( pass_box ).send_keys( self.password )
        sleep( 1 )
        # click button to login
        self.driver.find_element_by_css_selector( login_button ).click()
        sleep( 2 )
    
    def send_status( self ):
        # send status to status input box 
        self.driver.find_element_by_css_selector( tweet_box ).send_keys( self.status )
        sleep( 1 )
        # click button to tweet
        self.driver.find_element_by_css_selector( tweet_button ).click()
        sleep( 5 )
    
    def close_browser( self ):
        # close browser
        self.driver.close()
    
    def run_all( self ):
        # do it all 
        self.set_browser()
        self.login()
        self.send_status()
        self.close_browser()
        # report
        return f'sent tweet: { self.status } \nto account: { self.username }'


# call for status
my_tweet = input( "what's your status? " )

# check length for compliance
if len( my_tweet ) > 280:
    raise Exception( f'tweet too long \n{ len( my_tweet ) } > 280' )

# let's do it
print( Tweet( user , pwrd , my_tweet ).run_all() )
