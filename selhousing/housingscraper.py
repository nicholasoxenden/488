from time import sleep

import pandas as pd
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys

from housinginit import Complex, complex_objects, failed_complexes, complex_names
from driverinit import driver,google_url

driver.get(google_url)
driver.maximize_window()

####################################
# Begin Loop Through Complex Names #
###################################
for i in range(len(complex_names)):

    sleep(1)

    try:
        complex_name = complex_names[i] + " apartments provo"
    except TypeError:
        continue

    ### Navigate to the complex
    try:
        driver.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys(complex_name)
        driver.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys(Keys.RETURN)
    except :
        print(f"Error thrown for the following complex: {complex_name}. Continuing to the next complex.")
        failed_complexes.append(complex_name)
        driver.get(google_url)
        continue
    
    try:

        sleep(1)

        ### Identify the correct review link and click
        review_links_xpath = '//*[@id="rhs"]//a'
        sidebar_links = driver.find_elements_by_xpath(review_links_xpath)

        try:
            link_index = None
            for a in range(len(sidebar_links)):
                if 'review' in sidebar_links[a].text:
                    link_index = a
                    break
            driver.execute_script("arguments[0].click();", sidebar_links[a])
        except IndexError:
            print(f"Index error for the following complex: {complex_name}")
            failed_complexes.append(complex_name)
            driver.get(google_url)
            continue

        sleep(2)

        ### Now scrape review in pop up
        review = driver.find_element_by_xpath('//*[@class="review-score-container"]/div')
        rating = review.text.split('\n')[0]
        num_of_reviews = review.text.split('\n')[1].split(' ')[0]

        ### Scrape Name and Address
        top = driver.find_element_by_xpath('//*[@class="fp-w review-dialog-top"]')
        name_and_address = top.find_element_by_xpath('./div/div')
        name, address = name_and_address.text.split('\n')

        ### Create APT Complex Object and add to dict
        complex_objects[complex_name] = Complex(complex_name,address,rating)

        sleep(2)

        ### Nav Out
        buttons = driver.find_elements_by_xpath('//*[@class="Xvesr"]')
        close_button_index = len(buttons) - 1
        driver.execute_script("arguments[0].click();", buttons[close_button_index])
        google_button = driver.find_element_by_xpath('//*[@id="logo"]')
        driver.execute_script("arguments[0].click();", google_button)

        sleep(2)
    
    except NoSuchElementException:
        print(f"Error thrown for the following complex: {complex_name}. Continuing to the next complex.")
        failed_complexes.append(complex_name)
        driver.get(google_url)


### Unpack complex_objects and create df
data = {"complex_names": [b.name for a,b in complex_objects.items()], "complex_address": [b.address for a,b in complex_objects.items()], "complex_rating": [b.rating for a,b in complex_objects.items()]}
df = pd.DataFrame(data=data)










    
    



