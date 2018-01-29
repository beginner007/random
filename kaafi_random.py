from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
import random
import string
random_video = ''.join(random.choice(string.ascii_uppercase + string.digits + string.ascii_lowercase) for _ in range(11))
driver = webdriver.Chrome("/usr/lib/chromium-browser/chromedriver")
driver.get("https://www.youtube.com/watch?v={}".format(random_video))
