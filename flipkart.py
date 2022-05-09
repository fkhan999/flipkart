from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

s=Service("C:\\Users\\farru\\Downloads\\chrome\\chromedriver.exe")
#d=webdriver.Chrome(ChromeDriverManager().install())
d=webdriver.Chrome(service=s)
d.maximize_window()
d.implicitly_wait(10)
d.get("https://flipkart.com")

d.find_element(By.XPATH,"//button[contains(text(),'✕')]").click()
d.find_element(By.XPATH,"//input[@title='Search for products, brands and more']").send_keys("iphone 11")
d.find_element(By.XPATH,"//*[@id='container']/div/div[1]/div[1]/div[2]/div[2]/form/div/button").click()
d.find_element(By.XPATH,"//*[@id='container']/div/div[3]/div[1]/div[1]/div/div[1]/div/section[3]/div[2]/div/div/div/label/div[1]").click()
#//*[@class='_4rR01T']
#//*[@class='_30jeq3 _1_WHN1']
e=d.find_elements(By.XPATH,"//*[@class='_4rR01T']")


list=[]
list1=[]
list2=[]
for x in e:
    list.append(x.text)
e1=d.find_elements(By.XPATH,"//*[@class='_30jeq3 _1_WHN1']")
for x in e1:
    list1.append(x.text)
e2=d.find_elements(By.XPATH,"//*[@class='_1fQZEK']")
for x in e2:
    list2.append(x.get_attribute('href'))
#print(list,list1,list2)
list3=[]
for x in range(len(list)):
    list3.append([list[x],list1[x],list2[x]])
print(list3)


