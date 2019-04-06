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
        '''
        initialized)
            1) self
                >> self
            2) username
                >> email, handle, phone number, etc... of account tweet will be sent from
            3) password
                >> password of account tweet will be sent from 
            4) statua
                >> the tweet being sent 
        '''
        self.username = username
        self.password = password
        self.status = status

    # done here to avoid browser popping up before status is set
    def set_browser( self ):
        '''
        set driver (Firefox GeckoDriver) using previously defined options
        '''
        self.driver = webdriver.Firefox( options=options ) 
    
    def login( self ):
        '''
        load Twitter login page and log in to Twitter
        '''
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
        '''
        find tweet box on Twitter home page and send it the status input
        '''
        # send status to status input box 
        self.driver.find_element_by_css_selector( tweet_box ).send_keys( self.status )
        sleep( 1 )
        # click button to tweet
        self.driver.find_element_by_css_selector( tweet_button ).click()
        sleep( 5 )
    
    def close_browser( self ):
        '''
        closes browser being used  
        '''
        self.driver.close()
    
    # do it all 
    def run_all( self ):
        '''
        combination of all functions with output confirmation 
        '''
        # set GeckoDriver
        self.set_browser()
        # log in to Twitter
        self.login()
        # tweet out status input
        self.send_status()
        # close browser
        self.close_browser()
        # report back the tweet that was sent and account it was sent to
        return f'sent tweet: { self.status } \nto account: { self.username }'


# let's do it
if __name__ == '__main__':
    # check that username and password are logical
    if len( user ) < 1 or len( pwrd ) < 1:
        # username or password deemed invalid
        raise Exception('illogical username or password\nplease check you have correctly entered your login information \n@ login_info.py\n'
                        f'current user = {user} (len={len(user)})\ncurrent password = {pwrd} (len={len(pwrd)})') 

    # call for status
    my_tweet = input( "what's your status? " )

    # check that username and password are logical length
    if len( user ) < 1 or len( pwrd ) < 1:
        # username or password deemed invalid due to lenght of less than 1 character
        raise Exception('illogical username or password\nplease check you have correctly entered your login information \n@ login_info.py\n'
                        f'current user = {user} (len={len(user)})\ncurrent password = {pwrd} (len={len(pwrd)})') 

    # check max length for compliance
    if len( my_tweet ) > 280:
        # tweet deemed too long
        raise Exception( f'tweet too long \n{ len( my_tweet ) } > 280' )
    # check min length for compliance
    if len( my_tweet ) < 1:
        # tweet deemed too short 
        raise Exception( f'tweet too short \n{ len( my_tweet ) } < 1' )

    # option to enter username upon call
    if user == '__OPT-OUT__':
        user = input('username: ')

    # check that username length is logical 
    if len( user ) < 1:
        # username deemed invalid due to lenght of less than 1 character
        raise Exception(f'illogical username or password\ncurrent user = {user} (len={len(user)})\ncurrent password = {pwrd} (len={len(pwrd)})') 

    # option to enter password upon call
    if pwrd == '__OPT-OUT__':
        pwrd = input('password: ')

    # check that password is logical length
    if len( pwrd ) < 1:
        # password deemed invalid due to lenght of less than 1 character
        raise Exception(f'illogical username or password\ncurrent user = {user} (len={len(user)})\ncurrent password = {pwrd} (len={len(pwrd)})') 

    # display out in terminal 
    print( Tweet( user , pwrd , my_tweet ).run_all() )
