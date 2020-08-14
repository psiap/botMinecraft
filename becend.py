from selenium import webdriver

class voteCraft(object):
    def __init__(self,login,password,nick):
        self.__login = login
        self.__password = password
        self.__nick = nick
        self.topcraft = r'https://topcraft.ru/servers/308/'
        self.mineTrain = r'http://minecraftrating.ru/projects/excalibur-craft/'
        self.mcTop = r'https://mctop.su/servers/1088/'
        self.mcRate = r'http://mcrate.su/project/4396'

    def voteTopcraft(self):
        self.driver = webdriver.Chrome()
        self.driver.get(self.topcraft)
        self.driver.find_element_by_xpath('//*[text()="ГОЛОСОВАТЬ"]').click()
        self.loginVk()
        self.driver.find_element_by_name("nick").send_keys(self.__nick)
        self.driver.find_element_by_xpath("//*[@class='btn btn-info btn-vote voteBtn']").click()
        self.driver.close()

    def voteMinTren(self):
        self.driver = webdriver.Chrome()
        self.driver.get(self.mineTrain)
        self.driver.find_element_by_name("nick").send_keys(self.__nick)
        self.driver.find_element_by_xpath("//*[@class='btn btn-success btn-xs']").click()
        self.loginVk()
        self.driver.close()

    def voteMcTop(self):
        self.driver = webdriver.Chrome()
        self.driver.get(self.mcTop)
        self.driver.find_element_by_xpath("//*[@class='btn btn-info btn-vote openLoginModal']").click()
        self.loginVk()
        self.driver.find_element_by_name("nick").send_keys(self.__nick)
        self.driver.find_element_by_xpath("//*[@class='btn btn-info btn-vote voteBtn']").click()
        self.driver.close()

    def voteMcRate(self):
        self.driver = webdriver.Chrome()
        self.driver.get(self.mcRate)
        self.driver.find_element_by_xpath("//*[@class='fa fa-thumbs-o-up']").click()
        self.driver.find_element_by_class_name('vk_authorization').click()
        self.loginVk()
        self.driver.find_element_by_name('login_player').send_keys(self.__nick)
        self.driver.find_element_by_name('button_blue').click()

    def loginVk(self):
        self.loginError()
        self.driver.find_element_by_name("email").send_keys(self.__login)
        self.driver.find_element_by_name("pass").send_keys(self.__password)
        self.driver.find_element_by_id("install_allow").click()

    def loginError(self):
        try:
            self.driver.find_element_by_xpath("//*[@class='login__social-lnk login__social-vk modalVkLogin']").click()
        except Exception:
            print("Nothing")

