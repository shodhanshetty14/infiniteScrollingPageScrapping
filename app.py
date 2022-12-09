from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import re


url = "https://startuplister.com/"

driver = webdriver.Chrome()
driver.maximize_window() 


def startuplink():
    driver.get(url)
    driver.implicitly_wait(5)
    company_links = []
    sleep(5)
    i = 1
    screen_height = driver.execute_script("return window.screen.height;")
    
    while len(company_links) != 25 :
        driver.execute_script("window.scrollTo(0, {screen_height}*{i});".format(screen_height=screen_height, i=i))
        i += 1
        sleep(2)
        scroll_height = driver.execute_script("return document.body.scrollHeight;") 
        
        
        # if (screen_height) * i > scroll_height:
        #     break
        
        sleep(2)
        
        jobs_body = driver.find_elements(By.CSS_SELECTOR, 'div.GroupItem')
        
        for item in jobs_body:
            job_cards = item.find_elements(By.TAG_NAME, 'a')
            
            for jobItems in job_cards:
                all_links = jobItems.get_attribute('href')
                
                if all_links not in company_links:
                    company_links.append(all_links)
                
        
        # print(company_links)
        
        
    # print(company_links\n)
    companyDetails(company_links)
    



def companyDetails(compantLinks):
    company = {}
    for link in compantLinks:
        driver.get(link)
        driver.implicitly_wait(5)
        sleep(3)
        name_path = driver.find_element(
                            By.XPATH, '/html/body/div[1]/div[2]/div/div/div[2]/div[1]/div/div[1]/div[2]/div/div[2]/div/a')
        company_link = name_path.get_attribute('href')
        name = name_path.text
        # sleep(3) 
        # print(company_link)
        company['name'] = name
        company['website'] = company_link

        description = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div/div/div[2]/div[1]/div/div[2]/div/div[1]').text
        company['desc'] = description

        twitter = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div/div/div[2]/div[2]/div/div[3]/div/div/div/div').text
        # print(twitter)
        op = re.sub(r'\bFollow\b\s+',"",twitter)

        company['twitter'] = 'https://twitter.com/' + op 
        print(company)
        print()

startuplink()
