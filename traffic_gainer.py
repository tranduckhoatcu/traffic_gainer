import undetected_chromedriver.v2 as webdriver
from fake_useragent import UserAgent
from random import randint
import time
from requests import get
from http_request_randomizer.requests.proxy.requestProxy import RequestProxy


class WebDriverChrome(object):

    def __init__(self):
        self.user_agent = UserAgent()
        self.driver = self.StartWebdriver()
        

    def StartWebdriver(self):
        options = webdriver.ChromeOptions()
        options.add_argument("start-maximized")
        # options.add_argument("--incognito")
        # options.add_experimental_option("excludeSwitches", ["enable-automation"])
        # options.add_experimental_option("useAutomationExtension", False)
        # options.add_argument(f'user-agent={self.user_agent.random}')
        driver = webdriver.Chrome(options=options)
        return driver

    def RunStart(self):
        self.driver.get('https://nowsecure.nl')
        time.sleep(1.5)
        # self.driver.execute_script("window.scrollBy(0,"+str(randint(300,500))+");")
        # time.sleep(1.5)
        # self.driver.execute_script("window.scrollBy(0,"+str(randint(300,500))+");")
        # time.sleep(1.5)
        # self.driver.execute_script("window.scrollBy(0,"+str(randint(300,500))+");")
        # time.sleep(1.5)
        # self.driver.execute_script("window.scrollBy(0,"+str(randint(300,500))+");")
        # time.sleep(1.5)
        # self.driver.execute_script("window.scrollBy(0,"+str(randint(300,500))+");")
        # time.sleep(1.5)
        # self.driver.execute_script("window.scrollBy(0,"+str(-5000)+");")
        # # self.driver.manage().window().maximize();
        # self.driver.find_element_by_xpath("/html/body/form/div[2]/div[2]/div[2]/div[2]/div/div/div/ul/li[7]").click();
        # # body.click()
        # # body.send_keys(webdriver.common.keys.PAGE_DOWN)
        # time.sleep(1.5)
        # self.driver.execute_script("window.scrollBy(0,"+str(randint(300,500))+");")
        # time.sleep(1.5)
        # self.driver.execute_script("window.scrollBy(0,"+str(randint(300,500))+");")
        # time.sleep(1.5)
        # self.driver.execute_script("window.scrollBy(0,"+str(randint(300,500))+");")
        # time.sleep(1.5)
        # self.driver.execute_script("window.scrollBy(0,"+str(randint(300,500))+");")
        # time.sleep(1.5)
        # self.driver.execute_script("window.scrollBy(0,"+str(randint(300,500))+");")
        # time.sleep(1.5)
        # self.driver.execute_script("window.scrollBy(0,"+str(-5000)+");")
        # time.sleep(10)
        # self.driver.execute_script("window.scrollBy(0,"+str(-1000)+");")
        # self.driver.quit()

if __name__ == '__main__':
    # ip = get('https://api.ipify.org').text
    # print('My public IP address is: {}'.format(ip))
    # req_proxy = RequestProxy() #you may get different number of proxy when  you run this at each time
    # proxies = req_proxy.get_proxy_list()
    # vietnam = [] #int is list of Indian proxy
    # for proxy in proxies:
    #     if proxy.country == 'Vietnam':
    #         vietnam.append(proxy)
    # print(vietnam[0].get_address())
    # print(vietnam[0].country)
    # print('length: ',len(vietnam))
    Crawl = WebDriverChrome()
    Crawl.RunStart()