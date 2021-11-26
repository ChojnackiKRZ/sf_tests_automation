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
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from datetime import datetime
import time

username = 'kch141992-b6z5@force.com'
password = '7u8i9o0p'

options = webdriver.ChromeOptions()
options.add_argument(r"--user-data-dir=C:\Users\krzys\AppData\Local\Google\Chrome\User Data") #e.g. C:\Users\You\AppData\Local\Google\Chrome\User Data
options.add_argument(r'--profile-directory=Profile 0') #e.g. Profile 3
driver = webdriver.Chrome(executable_path=r'C:\MyPythonScripts\selenium_salesforce\chromedriver.exe', chrome_options=options)
driver.get("https://santander-f.lightning.force.com/lightning/o/Opportunity/list?filterName=00B7Q000004jIKFUA2")
driver.find_element_by_id('username').send_keys(username)
driver.find_element_by_id('password').send_keys(password)
driver.find_element_by_id('Login').click()

iteracja = 1

for potworzenia in range (1, 3):
    time.sleep(5)
    driver.find_element_by_xpath("//a[@title='New']").click()
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y_%H:%M:%S")
    
    time.sleep(5)
    driver.find_element_by_xpath("//*[@Name='Name']").send_keys(f'Szansa_testowa_{dt_string}')
    
    driver.find_element_by_xpath("/html/body/div[4]/div[2]/div/div[2]/div/div[2]/div/div/div/records-modal-lwc-detail-panel-wrapper/records-record-layout-event-broker/slot/records-lwc-detail-panel/records-base-record-form/div/div/div/div/records-lwc-record-layout/forcegenerated-detailpanel_opportunity___012000000000000aaa___full___create___recordlayout2/force-record-layout-block/slot/force-record-layout-section[1]/div/div/div/slot/force-record-layout-row[2]/slot/force-record-layout-item[1]/div/span/slot/slot/force-record-layout-lookup/lightning-lookup/lightning-lookup-desktop/lightning-grouped-combobox/div[1]/div/lightning-base-combobox/div/div[1]/input").click()
    driver.find_element_by_xpath("/html/body/div[4]/div[2]/div/div[2]/div/div[2]/div/div/div/records-modal-lwc-detail-panel-wrapper/records-record-layout-event-broker/slot/records-lwc-detail-panel/records-base-record-form/div/div/div/div/records-lwc-record-layout/forcegenerated-detailpanel_opportunity___012000000000000aaa___full___create___recordlayout2/force-record-layout-block/slot/force-record-layout-section[1]/div/div/div/slot/force-record-layout-row[2]/slot/force-record-layout-item[1]/div/span/slot/slot/force-record-layout-lookup/lightning-lookup/lightning-lookup-desktop/lightning-grouped-combobox/div[1]/div/lightning-base-combobox/div/div[1]/input").click()
    #driver.find_element_by_xpath("//input[@id='input-260']").click()
    #driver.find_element_by_xpath("/html/body/div[4]/div[2]/div/div[2]/div/div[2]/div/div/div/records-modal-lwc-detail-panel-wrapper/records-record-layout-event-broker/slot/records-lwc-detail-panel/records-base-record-form/div/div/div/div/records-lwc-record-layout/forcegenerated-detailpanel_opportunity___012000000000000aaa___full___create___recordlayout2/force-record-layout-block/slot/force-record-layout-section[1]/div/div/div/slot/force-record-layout-row[2]/slot/force-record-layout-item[1]/div/span/slot/slot/force-record-layout-lookup/lightning-lookup/lightning-lookup-desktop/lightning-grouped-combobox/div[1]/div/lightning-base-combobox/div/div[1]/input").send_keys(Keys.ARROW_DOWN)
    time.sleep(2)
    driver.find_element_by_xpath("/html/body/div[4]/div[2]/div/div[2]/div/div[2]/div/div/div/records-modal-lwc-detail-panel-wrapper/records-record-layout-event-broker/slot/records-lwc-detail-panel/records-base-record-form/div/div/div/div/records-lwc-record-layout/forcegenerated-detailpanel_opportunity___012000000000000aaa___full___create___recordlayout2/force-record-layout-block/slot/force-record-layout-section[1]/div/div/div/slot/force-record-layout-row[2]/slot/force-record-layout-item[1]/div/span/slot/slot/force-record-layout-lookup/lightning-lookup/lightning-lookup-desktop/lightning-grouped-combobox/div[1]/div/lightning-base-combobox/div/div[1]/input").send_keys(Keys.ENTER)
    #driver.find_element_by_xpath("//*[contains(text(), '1 (800)')]").click()
    driver.find_element_by_xpath("//*[@Name='CloseDate']").send_keys('10/11/2021')
    # driver.find_element_by_xpath("//*[starts-with(@id, 'input-326') and contains(@class,'slds-combobox__')]")
    time.sleep(5)
    driver.find_element_by_xpath("/html/body/div[4]/div[2]/div/div[2]/div/div[2]/div/div/div/records-modal-lwc-detail-panel-wrapper/records-record-layout-event-broker/slot/records-lwc-detail-panel/records-base-record-form/div/div/div/div/records-lwc-record-layout/forcegenerated-detailpanel_opportunity___012000000000000aaa___full___create___recordlayout2/force-record-layout-block/slot/force-record-layout-section[1]/div/div/div/slot/force-record-layout-row[3]/slot/force-record-layout-item[2]/div/span/slot/slot/sfa-input-stage-name/force-record-picklist/force-form-picklist/lightning-picklist/lightning-combobox/div/lightning-base-combobox/div/div[1]/input").click()
    driver.find_element_by_xpath("/html/body/div[4]/div[2]/div/div[2]/div/div[2]/div/div/div/records-modal-lwc-detail-panel-wrapper/records-record-layout-event-broker/slot/records-lwc-detail-panel/records-base-record-form/div/div/div/div/records-lwc-record-layout/forcegenerated-detailpanel_opportunity___012000000000000aaa___full___create___recordlayout2/force-record-layout-block/slot/force-record-layout-section[1]/div/div/div/slot/force-record-layout-row[3]/slot/force-record-layout-item[2]/div/span/slot/slot/sfa-input-stage-name/force-record-picklist/force-form-picklist/lightning-picklist/lightning-combobox/div/lightning-base-combobox/div/div[1]/input").send_keys(Keys.ARROW_DOWN)
    driver.find_element_by_xpath("/html/body/div[4]/div[2]/div/div[2]/div/div[2]/div/div/div/records-modal-lwc-detail-panel-wrapper/records-record-layout-event-broker/slot/records-lwc-detail-panel/records-base-record-form/div/div/div/div/records-lwc-record-layout/forcegenerated-detailpanel_opportunity___012000000000000aaa___full___create___recordlayout2/force-record-layout-block/slot/force-record-layout-section[1]/div/div/div/slot/force-record-layout-row[3]/slot/force-record-layout-item[2]/div/span/slot/slot/sfa-input-stage-name/force-record-picklist/force-form-picklist/lightning-picklist/lightning-combobox/div/lightning-base-combobox/div/div[1]/input").send_keys(Keys.ENTER)
    driver.find_element_by_xpath("/html/body/div[4]/div[2]/div/div[2]/div/div[2]/div/div/div/records-modal-lwc-detail-panel-wrapper/records-record-layout-event-broker/slot/records-lwc-detail-panel/records-base-record-form/div/div/div/force-form-footer/div/div/div/runtime_platform_actions-actions-ribbon/ul/li[3]/runtime_platform_actions-action-renderer/runtime_platform_actions-executor-lwc-headless/slot[1]/slot/lightning-button/button").click()
    
    time.sleep(5)
    #qualification
    mark_as_complete = driver.find_element_by_xpath("/html/body/div[4]/div[1]/section/div[1]/div[2]/div[2]/div[1]/div/div/div/div/div/one-record-home-flexipage2/forcegenerated-adg-rollup_component___force-generated__flexipage_-record-page___-opportunity_-record_-page___-opportunity___-v-i-e-w/forcegenerated-flexipage_opportunity_record_page_opportunity__view_js/record_flexipage-record-page-decorator/div[1]/records-record-layout-event-broker/slot/slot/flexipage-record-home-with-subheader-template-desktop2/div/div[2]/slot/slot/flexipage-component2/slot/flexipage-aura-wrapper/div/div/article/div/div/div/div[1]/div[2]/button/span")
    #qualification = driver.find_element_by_xpath("/html/body/div[4]/div[1]/section/div[1]/div[2]/div[2]/div[1]/div/div/div/div/div/one-record-home-flexipage2/forcegenerated-adg-rollup_component___force-generated__flexipage_-record-page___-opportunity_-record_-page___-opportunity___-v-i-e-w/forcegenerated-flexipage_opportunity_record_page_opportunity__view_js/record_flexipage-record-page-decorator/div[1]/records-record-layout-event-broker/slot/slot/flexipage-record-home-with-subheader-template-desktop2/div/div[2]/slot/slot/flexipage-component2/slot/flexipage-aura-wrapper/div/div/article/div/div/div/div[1]/div[1]/div[1]/div/div/ul/li[1]/a/span[2]")
    #driver.execute_script("arguments[0].click();", qualification)
    driver.execute_script("arguments[0].click();", mark_as_complete)
    
    time.sleep(2)
    #needs analysis
    mark_as_complete = driver.find_element_by_xpath("/html/body/div[4]/div[1]/section/div[1]/div[2]/div[2]/div[1]/div/div/div/div/div/one-record-home-flexipage2/forcegenerated-adg-rollup_component___force-generated__flexipage_-record-page___-opportunity_-record_-page___-opportunity___-v-i-e-w/forcegenerated-flexipage_opportunity_record_page_opportunity__view_js/record_flexipage-record-page-decorator/div[1]/records-record-layout-event-broker/slot/slot/flexipage-record-home-with-subheader-template-desktop2/div/div[2]/slot/slot/flexipage-component2/slot/flexipage-aura-wrapper/div/div/article/div/div/div/div[1]/div[2]/button/span")
    driver.execute_script("arguments[0].click();", mark_as_complete)
    
    time.sleep(2)
    #proposal
    mark_as_complete = driver.find_element_by_xpath("/html/body/div[4]/div[1]/section/div[1]/div[2]/div[2]/div[1]/div/div/div/div/div/one-record-home-flexipage2/forcegenerated-adg-rollup_component___force-generated__flexipage_-record-page___-opportunity_-record_-page___-opportunity___-v-i-e-w/forcegenerated-flexipage_opportunity_record_page_opportunity__view_js/record_flexipage-record-page-decorator/div[1]/records-record-layout-event-broker/slot/slot/flexipage-record-home-with-subheader-template-desktop2/div/div[2]/slot/slot/flexipage-component2/slot/flexipage-aura-wrapper/div/div/article/div/div/div/div[1]/div[2]/button/span")
    driver.execute_script("arguments[0].click();", mark_as_complete)
    
    time.sleep(2)
    #negotiation
    mark_as_complete = driver.find_element_by_xpath("/html/body/div[4]/div[1]/section/div[1]/div[2]/div[2]/div[1]/div/div/div/div/div/one-record-home-flexipage2/forcegenerated-adg-rollup_component___force-generated__flexipage_-record-page___-opportunity_-record_-page___-opportunity___-v-i-e-w/forcegenerated-flexipage_opportunity_record_page_opportunity__view_js/record_flexipage-record-page-decorator/div[1]/records-record-layout-event-broker/slot/slot/flexipage-record-home-with-subheader-template-desktop2/div/div[2]/slot/slot/flexipage-component2/slot/flexipage-aura-wrapper/div/div/article/div/div/div/div[1]/div[2]/button/span")
    driver.execute_script("arguments[0].click();", mark_as_complete)
    
    time.sleep(5)
    if iteracja == 1:
        #szansa wygrana
        driver.find_element_by_xpath("/html/body/div[4]/div[2]/div/div[2]/div/div[2]/div/div/div/select").send_keys(Keys.ARROW_DOWN)
        driver.find_element_by_xpath("/html/body/div[4]/div[2]/div/div[2]/div/div[2]/div/div/div/select").send_keys(Keys.ENTER)
        driver.find_element_by_xpath("/html/body/div[4]/div[2]/div/div[2]/div/div[3]/div/button[2]/span").click()
    
    if iteracja == 2:
        driver.find_element_by_xpath("/html/body/div[4]/div[2]/div/div[2]/div/div[2]/div/div/div/select").send_keys(Keys.ARROW_DOWN)
        driver.find_element_by_xpath("/html/body/div[4]/div[2]/div/div[2]/div/div[2]/div/div/div/select").send_keys(Keys.ARROW_DOWN)
        driver.find_element_by_xpath("/html/body/div[4]/div[2]/div/div[2]/div/div[2]/div/div/div/select").send_keys(Keys.ENTER)
        driver.find_element_by_xpath("/html/body/div[4]/div[2]/div/div[2]/div/div[3]/div/button[2]/span").click()
            
    time.sleep(3)
    driver.get("https://santander-f.lightning.force.com/lightning/o/Opportunity/list?filterName=00B7Q000004jIKFUA2")
    
    iteracja = iteracja + 1