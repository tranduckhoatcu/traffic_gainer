import subprocess
import secrets
from xvfbwrapper import Xvfb
import undetected_chromedriver.v2 as webdriver
from random import randint, sample
import time
from nordvpn_switcher import initialize_VPN,rotate_VPN
import articles
from selenium.common.exceptions import TimeoutException, NoSuchElementException , WebDriverException
class WebDriverChrome(object):

    def __init__(self):
        self.url_article = articles.daily_url
        self.url_home = ['/xem-mua-luon.chn','/hello-genz.html','/nhom-chu-de/emagazine.chn']
        self.driver = self.StartWebdriver()

    def StartWebdriver(self):
        options = webdriver.ChromeOptions()
        # options.add_argument("start-maximized")
        # options.add_argument("--incognito")
        # options.add_experimental_option("excludeSwitches", ["enable-automation"])
        # options.add_experimental_option("useAutomationExtension", False)
        # options.add_experimental_option("excludeSwitches", ["disable-popup-blocking"])
        options.add_argument(f'user-agent={secrets.choice(articles.user_agent)}')
        options.add_argument('--no-first-run --no-service-autorun --password-store=basic')
        options.add_argument('--user-data-dir=/home/test1/.config/google-chrome/Default')
        options.add_argument(f"--no-sandbox")
        options.add_argument(f"--disable-dev-shm-usage")
        driver = webdriver.Chrome(options=options)
        return driver

    def scroll_down_up(self):
        time.sleep(1)
        for i in range(6):
            self.driver.execute_script("window.scrollBy(0,"+str(randint(300,500))+");")
            time.sleep(1)
        self.driver.execute_script("window.scrollBy(0,"+str(-5000)+");")
    
    def scroll_down(self):
        time.sleep(1)
        for i in range(6):
            self.driver.execute_script("window.scrollBy(0,"+str(randint(600,800))+");")
            time.sleep(1)    

    def scroll_in_article(self):
        time.sleep(1)
        height = self.driver.find_element_by_xpath("/html/body/form/div[2]/div[2]/div[3]/div[1]/div[3]/div[2]/div/div[1]/div[2]/div/div/div[1]").size['height']
        print(height)
        count = 0
        while(count < height):
            rand = randint(200,400)
            self.driver.execute_script("window.scrollBy(0,"+str(rand)+");")
            count += rand
            time.sleep(randint(1,2))
        self.driver.execute_script("window.scrollBy(0,"+str(-5000)+");")
    
    def article_process(self, article_url):
        self.scroll_down()
        self.driver.find_element_by_xpath('//a[@href="'+article_url+'"]').click() # get article by url
        print('Article loaded')
        self.scroll_in_article()
        self.driver.find_element_by_xpath('//a[@href="'+self.url_home[0]+'"]').click() #back to 'mua xem luon' page


    def RunStart(self):
        temp_url = sample(self.url_article , len(self.url_article))
        self.url_article = temp_url

        self.driver.get('https://kenh14.vn/')
        print('Homepage loaded')
        # time.sleep(5)
        self.scroll_down_up()
        self.driver.find_element_by_xpath('//a[@href="'+self.url_home[0]+'"]').click() # load 'mua xem luon' page
        
        for i in range(len(self.url_article)):
            self.article_process(self.url_article[i])      

        self.driver.find_element_by_xpath('//a[@href="'+self.url_home[1]+'"]').click()
        self.scroll_down_up()
        
        self.driver.find_element_by_xpath('//a[@href="'+self.url_home[2]+'"]').click()
        self.scroll_down_up()
        time.sleep(10)
        self.driver.quit()

if __name__ == '__main__':
    command = ['nordvpn','disconnect']
    subprocess.run(command,stdout=subprocess.PIPE,stdin=subprocess.PIPE)
    vdisplay = Xvfb(width=800, height=1280)
    instructions = initialize_VPN(area_input=['Vietnam','Hong Kong','Singapore'], skip_settings=1)
    
    vdisplay.start()
    for i in range(50):
        try:
            rotate_VPN(instructions) #refer to the instructions variable here
        except:
            instructions = initialize_VPN(area_input=['Vietnam','Hong Kong','Singapore'], skip_settings=1)
            continue
            # subprocess.run(command,stdout=subprocess.PIPE,stdin=subprocess.PIPE)
            # break
        for i in range(5):
                try:
                    Crawl = WebDriverChrome()
                    time.sleep(5)
                    Crawl.RunStart()
                except (WebDriverException, TimeoutException,NoSuchElementException) as error:
                    print(error)
                    continue
    vdisplay.stop()
    subprocess.run(command,stdout=subprocess.PIPE,stdin=subprocess.PIPE)