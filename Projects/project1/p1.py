#https://www.jiosaavn.com/search/name of song
from selenium import webdriver
import time
song = input("Enter the name of the song: ")
song = song.replace(" ", "%20")
url = "https://www.jiosaavn.com/search/"+song
driver = webdriver.Firefox(executable_path = '../project1/geckodriver.exe')
driver.get(url)
#xpath of cookies permission /html/body/div[1]/div/div[2]/div/div/span
cookies = driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/div/span')
cookies.click()
time.sleep(2)
#class of <a> tag is u-color-js-gray
clk = driver.find_element_by_xpath('//a[@class="u-color-js-gray"]')
clk.click()
time.sleep(2)
# css selector of play button -- a.c-btn--primary:nth-child(1)
play = driver.find_element_by_css_selector('a.c-btn--primary:nth-child(1)')
play.click()
