from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from paths import login_page, user_box, pass_box, login_button, tweet_box, tweet_button
from login_info import user, pwrd


class TwitterBot:    

    def __init__(self, username):
        '''
        inputs:
            > username
                >> email, handle, phone number, etc... of account tweet will be sent from
        '''
        # who are we working with? (store user)
        self.username = username

    def set_browser(self, block_popups=True):
        '''
        function: set driver (Firefox GeckoDriver) using previously defined options
        inputs:
            > block_popups
                >> do you want pop ups blocked? (defaults to True)
        '''
        # are we blocking popups? (default answer is 'yes')
        if block_popups == True:
            # GeckoDriver setup
            options = webdriver.FirefoxOptions()
            # block popups 
            options.set_preference('dom.push.enabled', False)  
            # set webdriver with options
            self.driver = webdriver.Firefox(options=options) 
        # we are not blocking popups 
        else:
            # set default webdriver
            self.driver = webdriver.Firefox() 
    
    def login(self, password):
        '''
        function: load Twitter login page and log in to Twitter
        inputs:
            > password
                >> password of account tweet will be sent from 
        '''
        # load login page
        self.driver.get(login_page) 
        sleep(1)
        # send username to username input box
        self.driver.find_element_by_css_selector(user_box).send_keys(self.username)
        sleep(1)
        # send password to password input box
        self.driver.find_element_by_css_selector(pass_box).send_keys(password)
        sleep(1)
        # click button to login
        self.driver.find_element_by_css_selector(login_button).click()
        sleep(5)
    
    def send_status(self, status):
        '''
        function: find tweet box on Twitter home page and send it the status input
        inputs:
            > status
                >> the tweet being sent 
        '''
        # store status
        self.status = status
        # send status to status input box 
        sleep(3)
        tweet_space = '/html/body/div/div/div/div/main/div/div/div/div[1]/div/div[2]/div[2]/div[1]/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div[1]/div/div/div/div[2]/div/div/div/div'
        try:
            self.driver.find_elements_by_xpath(tweet_space)[0].send_keys(self.status)
            print('SUCCESS')
            sleep(2)
        except:
            print('EXCEPT')
            sleep(2)
            self.driver.find_element_by_css_selector(tweet_box).click()
            sleep(2)
            self.driver.find_elements_by_xpath(tweet_space)[0].send_keys(self.status)
        sleep(2)
        # click button to tweet
        self.driver.find_element_by_css_selector(tweet_button).click()
        sleep(5)
    
    def close_browser(self):
        '''
        quits browser being used  
        '''
        self.driver.quit()


# default funcitonality = log in and tweet
if __name__ == '__main__':

    # is username blank?
    if user.strip() == '':
        # option to enter username (eliminate error spaces w/ strip)
        user = input('username: ').strip()
    else:
        # eliminate error spaces just in case
        user = user.strip() 

    # is password blank?
    if pwrd.strip() == '':
        # option to enter password (eliminate error spaces w/ strip)
        pwrd = input('password: ').strip()
    else:
        # eliminate error spaces just in case
        pwrd = pwrd.strip() 

    # usernames must be less than 15 characters and passwords must be at least 6 characters
    if (len(user) > 15) or (len(pwrd) < 6):
        # username or password deemed invalid
        raise Exception('illogical username or password\nplease check you have correctly entered your login information \n@ login_info.py\n'
                        f'current user = {user} (len={len(user)})\ncurrent password = {pwrd} (len={len(pwrd)})') 

    # call for status
    my_tweet = 'testing out the new bot.. this thing on?'  # input("what's your status? ")

    # check max length for compliance
    if len(my_tweet) > 280:
        # tweet deemed too long
        raise Exception(f'tweet too long: {len(my_tweet)} > 280\n')
    # check min length for compliance
    elif len(my_tweet) < 1:
        # tweet deemed too short 
        raise Exception(f'tweet too short: {len(my_tweet)} < 1\n')

    # set TwitterBot instance
    tb = TwitterBot(username=user)

    # start up selenium webdriver 
    tb.set_browser()

    # log in to Twitter
    tb.login(password=pwrd)

    # tweet out status input
    tb.send_status(status=my_tweet)

    # shut down shop
    tb.close_browser()

    # report back the tweet that was sent and account it was sent to
    print(f'sent tweet: {tb.status} \nto account: {tb.username}')
