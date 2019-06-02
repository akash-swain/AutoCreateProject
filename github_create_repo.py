from selenium import webdriver
import sys


class GitHub:


    def __init__(self, username, password, url):
        self.username = username
        self.password = password
        self.driver = webdriver.Chrome(executable_path='chromedriver.exe')
        self.url = url

    def login(self):
        self.driver.get(self.url)
        searchLogin = self.driver.find_elements_by_xpath('//*[@id="login_field"]')[0]
        searchPassword = self.driver.find_elements_by_xpath('//*[@id="password"]')[0]
        searchLoginButton = self.driver.find_elements_by_xpath('//*[@id = "login"]/form/div[3]/input[4]')[0]
        # print (searchLogin)
        searchLogin.send_keys(self.username)
        searchPassword.send_keys(self.password)
        searchLoginButton.click()

    def create_new_repository(self):
        searchNewRepositoryButton = self.driver.find_elements_by_xpath('/html/body/div[4]/div/aside[1]/div[2]/div/div/h2/a')[0]
        searchNewRepositoryButton.click()


        searchRepositoryName = self.driver.find_elements_by_xpath('//*[@id="repository_name"]')[0]
        searchRepositoryName.send_keys(sys.argv[1])
        searchRepoPrivate = self.driver.find_elements_by_xpath('//*[@id="repository_visibility_private"]')[0]
        searchRepoPrivate.click()
        searchCreateRepo = self.driver.find_elements_by_xpath('//*[@id="new_repository"]/div[3]/button')[0]
        while not searchCreateRepo.is_enabled():
            continue
        searchCreateRepo.click()
        self.driver.close()




        

# git remote add origin https://github.com/aks16588/NewRepo.git
# git push -u origin master
    
with open("config.txt") as f:
    data = eval(f.read())

ic = GitHub(data["username"], data["password"], "https://github.com/login")
ic.login()
ic.create_new_repository()
