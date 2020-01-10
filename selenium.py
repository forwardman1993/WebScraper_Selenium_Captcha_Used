from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from sys import exit

import urllib
from selenium import webdriver

if __name__=="__main__":
    driver = webdriver.Firefox()
    driver.get('https://sehmoney.xyz/')

    in_str = input ("Enter OK :")
    if in_str.lower() != 'ok':
        exit()

    # get the image source
    img = driver.find_element_by_xpath('//div[@id="recaptcha_image"]/img')
    src = img.get_attribute('src')

    # download the image
    urllib.urlretrieve(src, "captcha.png")

    driver.close()
