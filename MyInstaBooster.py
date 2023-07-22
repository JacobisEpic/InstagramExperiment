from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.common.keys import Keys
from random import randint
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC
from instagrapi import Client


class Bot():

    links = []

    comments = [
        'Great post!', 'Awesome!'
    ]

    def __init__(self):
        self.login('USERNAME HERE','PASSWORD HERE')
        self.like_comment_by_hashtag('programming')

    # def login(self,username,password): # Github
    #     self.driver = webdriver.Chrome(r"/Applications/chrome.exe")
    #     self.driver.get("https://instagram.com/")
    #     sleep(5)
    #     username_box=self.driver.find_element_by_css_selector("input[name='username']")
    #     username_box.click()
    #     username_box.send_keys(username)
    #     sleep(2)
    #     password_box=self.driver.find_element_by_css_selector("input[name='password']")
    #     password_box.click()
    #     password_box.send_keys(password)
    #     sleep(2)
    #     login_btn = self.driver.find_element_by_css_selector("button[type='submit']")
    #     login_btn.click()
    #     sleep(5)
    #     self.driver.find_element_by_xpath("//button[contains(text(),'Not Now')]").click()
    #     sleep(5)
    #     self.driver.find_element_by_xpath("//button[contains(text(),'Not Now')]").click()
    #     sleep(5)

    def login(self, username, password):
        cl = Client()
        cl.login(username, password)

        followers = cl.user_followers(cl.user_id)
        print(followers)

        followers = cl.user_followers(cl.user_id)
        for user_id in followers.keys():
            cl.user_unfollow(user_id)


        self.driver = webdriver.Chrome()
        self.driver.get('https://instagram.com/')
        sleep(2)
        username_input = self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[1]/div/label/input')

        username_input.send_keys(username)
        sleep(1)
        password_input = self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[2]/div/label/input')
        password_input.send_keys(password)
        sleep(3)
        # self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[3]/button').click()
        self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[3]').click()
        
        sleep(4)
        # self.driver.get('https://www.instagram.com/'+username+'/')
        # sleep(3)
        # self.driver.get('https://www.instagram.com/'+'rap' +'/followers/')
        
        self.driver.get('https://www.instagram.com/'+'apple'+'/')
        sleep(5)

        self.driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/div[2]/section/main/div/header/section/div[1]/div[2]/div/div[1]/button/div/div').click()
        sleep(100)
        # self.driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/div[2]/section/main/div/ul/li[2]/a/span/span/span')
        # followButton = self.driver.find_element(By.CSS_SELECTOR,'button')
        # if followButton != 'Message':
        #     followButton.click()
        #     sleep(5)
        # sleep(100)   

       
        # self.driver.find_element(By.XPATH,'//*[@id="mount_0_0_GS"]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/section/main/div/div/div/div/div').click() # clicking 'not now btn'
        # self.driver.find_element(By.CLASS_NAME,'"Not Now').click() # clicking 'not now btn'
        # self.driver.find_element(By.XPATH, '//button[text() = "Not Now")]').click()
        # WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH,'//button[text() = "Not Now"]'))).click()
        self.driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/section/main/div/div/div/div/div').click()


        sleep(3)
        # self.driver.find_element(By.XPATH,'//*[@id="mount_0_0_kw"]/div/div/div[3]').click() # clicking 'not now btn'
        self.driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[3]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]').click()

        sleep(3)
        # self.driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[1]/div/div/div/div/div[2]/div[8]/div/span/div/a/div/div[2]').click()
        self.driver.get('https://www.instagram.com/jacob_is_awesome_and_u_know_it/')
        sleep(100)
    def nav(self, target):
        self.driver.get('https://www.instagram.com/'+target+'/')
        self.driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/div[2]/section/main/div/header/section/div[1]/div[1]/div/div/button')

    # def like_comment_by_hashtag(self, hashtag):
    #     self.driver.get('https://www.instagram.com/explore/tags/{}/'.format(hashtag))
    #     links = self.driver.find_elements_by_tag_name('a')

    #     def condition(link):
    #         return '.com/p/' in link.get_attribute('href')
    #     valid_links = list(filter(condition, links))

    #     for i in range(5):
    #         link = valid_links[i].get_attribute('href')
    #         if link not in self.links:
    #             self.links.append(link)

    #     for link in self.links:
    #         self.driver.get(link)
    #         # like
    #         sleep(3)
    #         self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div[1]/article/div[3]/section[1]/span[1]/button').click()
    #         sleep(5)

    #         # comment
    #         self.driver.find_element_by_class_name('RxpZH').click() 
    #         sleep(1)
    #         self.driver.find_element_by_xpath("//textarea[@placeholder='Add a comment…']").send_keys(self.comments[randint(0,1)])
    #         sleep(1)
    #         self.driver.find_element_by_xpath("//button[@type='submit']").click()

def main():

    while True:
        my_bot = Bot()
        sleep(60*60) # one hour

if __name__ == '__main__':
    main()
