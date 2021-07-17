from selenium import webdriver

### Driver Setup
PATH = r'/Users/nicholasoxenden/Oxenden/Work/ECON RA/Chromedriver/chromedriver' #needs the r before the filepath in quotes for some reason
driver = webdriver.Chrome(PATH)

### Begin Navigation
google_url = "https://www.google.com/"