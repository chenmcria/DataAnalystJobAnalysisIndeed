from nltk import word_tokenize, Counter
from selenium import webdriver
import pandas as pd
from bs4 import BeautifulSoup

import pandas as pd

## Download the chromedriver from link in description
## And give the location of executable here
from sklearn.feature_extraction import stop_words

driver = webdriver.Chrome("/usr/local/bin/chromedriver")

dataframe = pd.DataFrame(columns=["Title", "Location", "Company", "Salary", "Description"])


for i in range(0, 500, 10):

    ##Step1: Get the page
    driver.get("https://ca.indeed.com/jobs?q=data+analyst&l=Canada&start=" + str(i))
    driver.implicitly_wait(4)

    all_jobs = driver.find_elements_by_class_name('result')
    print(all_jobs)
    for job in all_jobs:

        result_html = job.get_attribute('innerHTML')
        soup = BeautifulSoup(result_html, 'html.parser')

        try:
            title = soup.find("a", class_="jobtitle").text.replace('\n', '')
        except:
            title = 'None'

        try:
            location = soup.find(class_="location").text
        except:
            location = 'None'

        try:
            company = soup.find(class_="company").text.replace("\n", "").strip()
        except:
            company = 'None'

        try:
            salary = soup.find(class_="salary").text.replace("\n", "").strip()
        except:
            salary = 'None'


        sum_div = job.find_elements_by_class_name("summary")[0]
        try:
            sum_div.click()
        except:
            close_button = driver.find_elements_by_class_name("popover-x-button-close")[0]
            close_button.click()
            sum_div.click()

        job_desc = driver.find_element_by_id('vjs-content').text

        dataframe = dataframe.append({'Title': title, 'Location': location, "Company": company,
                                       "Description": job_desc},
                                     ignore_index=True)

dataframe.to_csv("dataanalyst.csv", index=False)








