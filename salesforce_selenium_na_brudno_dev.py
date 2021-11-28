# -*- coding: utf-8 -*-
"""
Created on Sat Nov 20 13:08:27 2021

@author: krzys
"""

#automatyzacja testów funkcjonalnych i testów regresyjnych

#jako menadzer moge:
    #1.Dodac szanse sprzedazowa
    #2.Usunac szanse sprzedazowe
    #3.Wyedytowac dowolna szanse sprzedazowa

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from datetime import datetime
import time
from simple_salesforce import Salesforce
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException, ElementClickInterceptedException
import os, sys

path = r'C:\MyPythonScripts\selenium_salesforce'
os.chdir(path)

hasla = open("hasla.txt", "r")

username = ''
password = ''
token = ''
domain = 'login'

n = 0

for i in hasla:
    if n == 0:
        username = i.rstrip()
    elif n == 1:
        password = i.rstrip()
    elif n == 2:
        token = i.rstrip()
    n = n + 1

hasla.close()

options = webdriver.ChromeOptions()
options.add_argument(r"--user-data-dir=C:\Users\krzys\AppData\Local\Google\Chrome\User Data") #e.g. C:\Users\You\AppData\Local\Google\Chrome\User Data
options.add_argument(r'--profile-directory=Profile 0') #e.g. Profile 3
driver = webdriver.Chrome(executable_path=r'C:\MyPythonScripts\selenium_salesforce\chromedriver.exe', chrome_options=options)
driver.get("https://noname96-dev-ed.lightning.force.com/lightning/o/Opportunity/list?filterName=00B7Q000001nTvsUAE")
driver.find_element_by_id('username').send_keys(username)
driver.find_element_by_id('password').send_keys(password)
driver.find_element_by_id('Login').click()

iteracja = 1

for powtorzenia in range (1, 3):
    etap = 'Klikniecie "New" na stronie'
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y_%H:%M:%S")
    time.sleep(5)
    try:
        driver.find_element_by_xpath("//a[@title='New']").click()
    except:
        the_type, the_value, the_traceback = sys.exc_info()
        with open (r'C:\MyPythonScripts\selenium_salesforce\log_{}.txt'.format(dt_string[:10].replace('/','_')), 'a+') as f:
            print (datetime.now()
                   ,'\n'
                   ,'*{}'.format(etap)
                   , '\n'
                   ,'*{}'.format(the_type)
                   , '\n'
                   ,'*{}'.format(the_value)
                   ,'*{}'.format(the_traceback)
                   , '\n'
                   , file=f)
        time.sleep(3)

    time.sleep(1)
    etap = 'Dodawanie nowej szansy'
    try:
        driver.find_element_by_xpath("//*[@Name='Name']").send_keys(f'Szansa_testowa_{dt_string}')
        driver.find_element_by_xpath("//*[@Name='CloseDate']").send_keys('10/11/2021')
        driver.find_element_by_xpath("/html/body/div[4]/div[2]/div/div[2]/div/div[2]/div/div/div/records-modal-lwc-detail-panel-wrapper/records-record-layout-event-broker/slot/records-lwc-detail-panel/records-base-record-form/div/div/div/div/records-lwc-record-layout/forcegenerated-detailpanel_opportunity___012000000000000aaa___full___create___recordlayout2/force-record-layout-block/slot/force-record-layout-section[1]/div/div/div/slot/force-record-layout-row[4]/slot/force-record-layout-item[2]/div/span/slot/slot/sfa-input-stage-name/force-record-picklist/force-form-picklist/lightning-picklist/lightning-combobox/div[1]/lightning-base-combobox/div/div[1]/input").click()
        driver.find_element_by_xpath("/html/body/div[4]/div[2]/div/div[2]/div/div[2]/div/div/div/records-modal-lwc-detail-panel-wrapper/records-record-layout-event-broker/slot/records-lwc-detail-panel/records-base-record-form/div/div/div/div/records-lwc-record-layout/forcegenerated-detailpanel_opportunity___012000000000000aaa___full___create___recordlayout2/force-record-layout-block/slot/force-record-layout-section[1]/div/div/div/slot/force-record-layout-row[4]/slot/force-record-layout-item[2]/div/span/slot/slot/sfa-input-stage-name/force-record-picklist/force-form-picklist/lightning-picklist/lightning-combobox/div[1]/lightning-base-combobox/div/div[1]/input").send_keys(Keys.ARROW_DOWN)
        driver.find_element_by_xpath("/html/body/div[4]/div[2]/div/div[2]/div/div[2]/div/div/div/records-modal-lwc-detail-panel-wrapper/records-record-layout-event-broker/slot/records-lwc-detail-panel/records-base-record-form/div/div/div/div/records-lwc-record-layout/forcegenerated-detailpanel_opportunity___012000000000000aaa___full___create___recordlayout2/force-record-layout-block/slot/force-record-layout-section[1]/div/div/div/slot/force-record-layout-row[4]/slot/force-record-layout-item[2]/div/span/slot/slot/sfa-input-stage-name/force-record-picklist/force-form-picklist/lightning-picklist/lightning-combobox/div[1]/lightning-base-combobox/div/div[1]/input").send_keys(Keys.ENTER)
        driver.find_element_by_xpath("/html/body/div[4]/div[2]/div/div[2]/div/div[2]/div/div/div/records-modal-lwc-detail-panel-wrapper/records-record-layout-event-broker/slot/records-lwc-detail-panel/records-base-record-form/div/div/div/force-form-footer/div/div/div/runtime_platform_actions-actions-ribbon/ul/li[3]/runtime_platform_actions-action-renderer/runtime_platform_actions-executor-lwc-headless/slot[1]/slot/lightning-button/button").click()
    except:
        the_type, the_value, the_traceback = sys.exc_info()
        with open (r'C:\MyPythonScripts\selenium_salesforce\log_{}.txt'.format(dt_string[:10].replace('/','_')), 'a+') as f:
            print (datetime.now()
                   ,'\n'
                   ,'*{}'.format(etap)
                   , '\n'
                   ,'*{}'.format(the_type)
                   , '\n'
                   ,'*{}'.format(the_value)
                   ,'*{}'.format(the_traceback)
                   , '\n'
                   , file=f)
        time.sleep(3)
    
    etap = 'Kolejne etapy szansy'
    time.sleep(3)
    for i in range (0, 8):
    #prospecting, qualification, needs analysis, value proposition
    #ID. decision making, perception analysis, proposal price quote
    #negotiation review, closed
        try:    
            mark_as_complete = driver.find_element_by_xpath("/html/body/div[4]/div[1]/section/div[1]/div[2]/div[2]/div[1]/div/div/div/div/div/one-record-home-flexipage2/forcegenerated-adg-rollup_component___force-generated__flexipage_-record-page___sfa__-opportunity_rec_-l___-opportunity___-v-i-e-w/forcegenerated-flexipage_opportunity_rec_l_opportunity__view_js/record_flexipage-record-page-decorator/div[1]/records-record-layout-event-broker/slot/slot/flexipage-record-home-with-subheader-template-desktop2/div/div[2]/slot/slot/flexipage-component2/slot/flexipage-aura-wrapper/div/div/article/div/div/div/div[1]/div[2]/button/span")
            driver.execute_script("arguments[0].click();", mark_as_complete)
        except:
            the_type, the_value, the_traceback = sys.exc_info()
            with open (r'C:\MyPythonScripts\selenium_salesforce\log_{}.txt'.format(dt_string[:10].replace('/','_')), 'a+') as f:
                print (datetime.now()
                       ,'\n'
                       ,'*{}'.format(etap)
                       , '\n'
                       ,'*{}'.format(the_type)
                       , '\n'
                       ,'*{}'.format(the_value)
                       ,'*{}'.format(the_traceback)
                       , '\n'
                       , file=f)

        time.sleep(1)
    
    etap = 'Wygrana/przegrana szansa'    
    time.sleep(1)
    if iteracja == 1:
        #szansa wygrana
        try:
            driver.find_element_by_xpath("/html/body/div[4]/div[2]/div/div[2]/div/div[2]/div/div/div/select").send_keys(Keys.ARROW_DOWN)
            driver.find_element_by_xpath("/html/body/div[4]/div[2]/div/div[2]/div/div[2]/div/div/div/select").send_keys(Keys.ENTER)
            driver.find_element_by_xpath("/html/body/div[4]/div[2]/div/div[2]/div/div[3]/div/button[2]/span").click()
        except:
            the_type, the_value, the_traceback = sys.exc_info()
            with open (r'C:\MyPythonScripts\selenium_salesforce\log_{}.txt'.format(dt_string[:10].replace('/','_')), 'a+') as f:
                print (datetime.now()
                       ,'\n'
                       ,'*{}'.format(etap)
                       , '\n'
                       ,'*{}'.format(the_type)
                       , '\n'
                       ,'*{}'.format(the_value)
                       ,'*{}'.format(the_traceback)
                       , '\n'
                       , file=f)
        
        #szansa przegrana
    if iteracja == 2:
        try:
            driver.find_element_by_xpath("/html/body/div[4]/div[2]/div/div[2]/div/div[2]/div/div/div/select").send_keys(Keys.ARROW_DOWN)
            driver.find_element_by_xpath("/html/body/div[4]/div[2]/div/div[2]/div/div[2]/div/div/div/select").send_keys(Keys.ARROW_DOWN)
            driver.find_element_by_xpath("/html/body/div[4]/div[2]/div/div[2]/div/div[2]/div/div/div/select").send_keys(Keys.ENTER)
            driver.find_element_by_xpath("/html/body/div[4]/div[2]/div/div[2]/div/div[3]/div/button[2]/span").click()
        except:
            the_type, the_value, the_traceback = sys.exc_info()
            with open (r'C:\MyPythonScripts\selenium_salesforce\log_{}.txt'.format(dt_string[:10].replace('/','_')), 'a+') as f:
                print (datetime.now()
                       ,'\n'
                       ,'*{}'.format(etap)
                       , '\n'
                       ,'*{}'.format(the_type)
                       , '\n'
                       ,'*{}'.format(the_value)
                       ,'*{}'.format(the_traceback)
                       , '\n'
                       , file=f)
            
    time.sleep(3)
    driver.get("https://noname96-dev-ed.lightning.force.com/lightning/o/Opportunity/list?filterName=00B7Q000001nTvsUAE")
    
    iteracja = iteracja + 1

sf = Salesforce(username = username
                , password = password
                , security_token = token
                , domain = domain)

opps = sf.query_all("SELECT Id FROM Opportunity")

opp_url = 'https://noname96-dev-ed.lightning.force.com/lightning/r/Opportunity/'

for wystapienia in range (0,len(opps['records'])):
    driver.get(opp_url + opps['records'][wystapienia]['Id'] + '/view')
    time.sleep(3)
    try:
        rozwin = driver.find_element_by_xpath("//*[@id='brandBand_2']/div/div/div/div/one-record-home-flexipage2/forcegenerated-adg-rollup_component___force-generated__flexipage_-record-page___sfa__-opportunity_rec_-l___-opportunity___-v-i-e-w/forcegenerated-flexipage_opportunity_rec_l_opportunity__view_js/record_flexipage-record-page-decorator/div[1]/records-record-layout-event-broker/slot/slot/flexipage-record-home-with-subheader-template-desktop2/div/div[1]/slot/slot/flexipage-component2/slot/records-lwc-highlights-panel/records-lwc-record-layout/forcegenerated-highlightspanel_opportunity___012000000000000aaa___compact___view___recordlayout2/force-highlights2/div[1]/div[1]/div[3]/div/runtime_platform_actions-actions-ribbon/ul/li[4]/lightning-button-menu/button/lightning-primitive-icon")
        driver.execute_script("arguments[0].click();", rozwin) 
    except:
        etap = 'Przycisk do rozwijania'
        the_type, the_value, the_traceback = sys.exc_info()
        with open (r'C:\MyPythonScripts\selenium_salesforce\log_{}.txt'.format(dt_string[:10].replace('/','_')), 'a+') as f:
            print (datetime.now()
                   ,'\n'
                   ,'*{}'.format(etap)
                   , '\n'
                   ,'*{}'.format(the_type)
                   , '\n'
                   ,'*{}'.format(the_value)
                   ,'*{}'.format(the_traceback)
                   , '\n'
                   , file=f)
    time.sleep(1)
    try:
        edytuj = driver.find_element_by_xpath("//*[@id='brandBand_2']/div/div/div/div/one-record-home-flexipage2/forcegenerated-adg-rollup_component___force-generated__flexipage_-record-page___sfa__-opportunity_rec_-l___-opportunity___-v-i-e-w/forcegenerated-flexipage_opportunity_rec_l_opportunity__view_js/record_flexipage-record-page-decorator/div[1]/records-record-layout-event-broker/slot/slot/flexipage-record-home-with-subheader-template-desktop2/div/div[1]/slot/slot/flexipage-component2/slot/records-lwc-highlights-panel/records-lwc-record-layout/forcegenerated-highlightspanel_opportunity___012000000000000aaa___compact___view___recordlayout2/force-highlights2/div[1]/div[1]/div[3]/div/runtime_platform_actions-actions-ribbon/ul/li[4]/lightning-button-menu/div/div/slot/runtime_platform_actions-action-renderer[3]/runtime_platform_actions-executor-page-reference/slot/slot/runtime_platform_actions-ribbon-menu-item/a/span")
        driver.execute_script("arguments[0].click();", edytuj)
    except:
        etap = 'Przycisk edytuj'
        the_type, the_value, the_traceback = sys.exc_info()
        with open (r'C:\MyPythonScripts\selenium_salesforce\log_{}.txt'.format(dt_string[:10].replace('/','_')), 'a+') as f:
            print (datetime.now()
                   ,'\n'
                   ,'*{}'.format(etap)
                   , '\n'
                   ,'*{}'.format(the_type)
                   , '\n'
                   ,'*{}'.format(the_value)
                   ,'*{}'.format(the_traceback)
                   , '\n'
                   , file=f)
    time.sleep(1)
    try:
        driver.find_element_by_xpath("//*[@Name='Amount']").send_keys(0)
    except:
        etap = 'Pole "Amount"'
        the_type, the_value, the_traceback = sys.exc_info()
        with open (r'C:\MyPythonScripts\selenium_salesforce\log_{}.txt'.format(dt_string[:10].replace('/','_')), 'a+') as f:
            print (datetime.now()
                   ,'\n'
                   ,'*{}'.format(etap)
                   , '\n'
                   ,'*{}'.format(the_type)
                   , '\n'
                   ,'*{}'.format(the_value)
                   ,'*{}'.format(the_traceback)
                   , '\n'
                   , file=f)        
    time.sleep(1)
    try:
        driver.find_element_by_xpath("//*[@Name='SaveEdit']").click()
    except:
        etap = 'Przycisk "Save"'
        the_type, the_value, the_traceback = sys.exc_info()
        with open (r'C:\MyPythonScripts\selenium_salesforce\log_{}.txt'.format(dt_string[:10].replace('/','_')), 'a+') as f:
            print (datetime.now()
                   ,'\n'
                   ,'*{}'.format(etap)
                   , '\n'
                   ,'*{}'.format(the_type)
                   , '\n'
                   ,'*{}'.format(the_value)
                   ,'*{}'.format(the_traceback)
                   , '\n'
                   , file=f)
    time.sleep(2)
