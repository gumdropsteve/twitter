from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from paths import login_page, user_box, pass_box, login_button, tweet_box, tweet_button
from login_info import user, pwrd

# GeckoDriver setup
options = webdriver.FirefoxOptions()  
options.set_preference( 'dom.push.enabled' , False )  # blocks popups 


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
        self.driver.get( login_page ) 
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


# check that username and password are logical
if len( user ) < 1 or len( pwrd ) < 1:
    raise Exception('illogical username or password\nplease check you have correctly entered your login information \n@ login_info.py\n'
                    f'current user = {user} (len={len(user)})\ncurrent password = {pwrd} (len={len(pwrd)})') 

# call for status
my_tweet = input( "what's your status? " )

# check length for compliance
if len( my_tweet ) > 280:
    raise Exception( f'tweet too long \n{ len( my_tweet ) } > 280' )

# option to enter username upon call
if user == '__OPT-OUT__':
    pwrd = user('username: ')

# option to enter password upon call
if pwrd == '__OPT-OUT__':
    pwrd = input('password: ')

# let's do it
print( Tweet( user , pwrd , my_tweet ).run_all() )
