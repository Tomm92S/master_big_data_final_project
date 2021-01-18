# -*- coding: utf-8 -*-
"""
Created on Fri Oct 16 09:49:10 2020

@author: Tommaso Lo Sterzo
"""






from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
from random import uniform
import csv
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import StaleElementReferenceException
from datetime import datetime


start = datetime.now()

#0.1) SET THE INITIAL URL
URL = 'https://www.immobiliare.it/mercato-immobiliare/veneto/'


#0.2) SET THE WEBDRIVER
#use this to have a look:
#driver = webdriver.Chrome('C:\\Users\\Federico\\Anaconda3\\Lib\\site-packages\\chromedriver.exe')
#driver.get(URL)

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
driver = webdriver.Chrome('C:\\Users\\Federico\\Anaconda3\\Lib\\site-packages\\chromedriver.exe',chrome_options=chrome_options)
driver.get(URL)


    
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#1) SEZIONE REGIONE
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    
#1.1) OPEN FILE TO WRITE (AFFITTI REGION) 
with open('Raw_data\\Veneto_affitti.csv', 'w',encoding="utf-8") as iterator1:
    writer_reg_a = csv.writer(iterator1, delimiter=',', quotechar='"' )
    
    row_reg_a = [URL]    


    #A) MOVE MOUSE TO  AFFITTI/VENDITE WINDOW      
    try:
        visible_button = WebDriverWait(driver, 60).until(EC.visibility_of_element_located((By.CSS_SELECTOR , 'div.nd-cgSummaryBox__options nd-select:first-of-type div')))
    
    except TimeoutException or StaleElementReferenceException:
        
        driver.close()
        sleep(2)
        
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--headless')
        driver = webdriver.Chrome('C:\\Users\\Federico\\Anaconda3\\Lib\\site-packages\\chromedriver.exe',chrome_options=chrome_options)
        driver.get(URL)
        
        print('exception_zone')
        sleep(3)
        visible_button = WebDriverWait(driver, 60).until(EC.visibility_of_element_located((By.CSS_SELECTOR , 'div.nd-cgSummaryBox__options nd-select:first-of-type div')))
        ActionChains(driver).move_to_element(visible_button).click().perform()
        sleep(uniform(0,1))         
        
    else:
        ActionChains(driver).move_to_element(visible_button).click().perform()
        sleep(uniform(0,1))

    #B) CLICK AFFITTI SECTION
    try:
        visible_button = WebDriverWait(driver, 60).until(EC.visibility_of_element_located((By.CSS_SELECTOR , 'div.nd-cgSummaryBox__options nd-select:first-of-type div.nd-select__menu ul li:last-child')))
        
   
    except TimeoutException or StaleElementReferenceException:
            
        driver.close()
        sleep(2)
        
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--headless')
        driver = webdriver.Chrome('C:\\Users\\Federico\\Anaconda3\\Lib\\site-packages\\chromedriver.exe',chrome_options=chrome_options)
        driver.get(URL)

        print('exception_zone')
        sleep(3)
        down = driver.find_element_by_css_selector('body > div.nd-cityGuide__content.has-fixedNav > nd-cityguide > nd-cityguide-sections > section:nth-child(2) > div > nd-price-chart > div.ct-chart.ct-perfect-fourth > svg')
        ActionChains(driver).move_to_element(down).perform()
        
        visible_button = WebDriverWait(driver, 60).until(EC.visibility_of_element_located((By.CSS_SELECTOR , 'body > div.nd-cityGuide__content.has-fixedNav > nd-cityguide > nd-cityguide-sections > section:nth-child(2) > div > nd-price-chart > div.nd-cgSummaryBox > div.nd-cgSummaryBox__options > nd-select:nth-child(1) > div')))
        ActionChains(driver).move_to_element(visible_button).click().perform()
        sleep(uniform(0,1))
            
        visible_button = WebDriverWait(driver, 60).until(EC.visibility_of_element_located((By.CSS_SELECTOR , 'div.nd-cgSummaryBox__options nd-select:first-of-type div.nd-select__menu ul li:last-child')))
        ActionChains(driver).move_to_element(visible_button).click().perform()
        
    else:
        ActionChains(driver).move_to_element(visible_button).click().perform()

    #C) MOVE MOUSE TO NEUTRAL ZONE
    neutral_zone = WebDriverWait(driver, 60).until(EC.visibility_of_element_located((By.CSS_SELECTOR , 'body > div.nd-cityGuide__content.has-fixedNav > nd-cityguide > nd-cityguide-sections > section:nth-child(2) > div > nd-price-chart > div.nd-cgSummaryBox > div.nd-cgSummaryBox__texts')))
    ActionChains(driver).move_to_element(neutral_zone).click().perform()
    sleep(uniform(0,1))

    #D) MOVE MOUSE TO LINE PLOT    
    down = driver.find_element_by_css_selector('div.nd-cgSection__trends')
    ActionChains(driver).move_to_element(down).perform()
    sleep(uniform(0,1))
                                

    #E) FIND ALL POINTS OF THE GRAPH
    points = driver.find_elements_by_css_selector('nd-price-chart div.ct-perfect-fourth svg g.ct-series-a > line')
    
    #F) GRAB PRICE AND DATE FOR EVERY POINT IN GRAPH
    for point in points:
        ActionChains(driver).move_to_element(point).perform() 
        prezzo = WebDriverWait(driver, 60).until(EC.visibility_of_element_located((By.CSS_SELECTOR , 'div.nd-price-chart__tooltip div.nd-tooltip__container div:first-child')))

        data = WebDriverWait(driver, 60).until(EC.visibility_of_element_located((By.CSS_SELECTOR , 'div.nd-price-chart__tooltip div.nd-tooltip__container div:last-child')))

        #sleep(uniform(0,1))
        row_reg_a.append('-'.join([data.text,prezzo.text]))
    
    writer_reg_a.writerow(row_reg_a)
    
    
    #1.2) OPEN FILE TO WRITE (VENDITE REGION) 
    with open('Raw_data\\Veneto_vendite.csv', 'w',encoding="utf-8") as iterator2:
        writer_reg_v = csv.writer(iterator2, delimiter=',', quotechar='"' )
        
        row_reg_v = [URL]
        
        #A) MOVE MOUSE TO  AFFITTI/VENDITE WINDOW       
        try:
            visible_button = WebDriverWait(driver, 60).until(EC.visibility_of_element_located((By.CSS_SELECTOR , 'div.nd-cgSummaryBox__options nd-select:first-of-type div')))
        
        except TimeoutException or StaleElementReferenceException:
            
            driver.close()
            sleep(2)
            
            chrome_options = webdriver.ChromeOptions()
            chrome_options.add_argument('--headless')
            driver = webdriver.Chrome('C:\\Users\\Federico\\Anaconda3\\Lib\\site-packages\\chromedriver.exe',chrome_options=chrome_options)
            driver.get(URL)
            
            print('exception_zone')
            sleep(3)
            visible_button = WebDriverWait(driver, 60).until(EC.visibility_of_element_located((By.CSS_SELECTOR , 'div.nd-cgSummaryBox__options nd-select:first-of-type div')))
            ActionChains(driver).move_to_element(visible_button).click().perform()
            sleep(uniform(0,1))         
            
        else:
            ActionChains(driver).move_to_element(visible_button).click().perform()
            sleep(uniform(0,1))

        #B) CLICK VENDITE SECTION
        try:
            visible_button = WebDriverWait(driver, 60).until(EC.visibility_of_element_located((By.CSS_SELECTOR , 'div.nd-cgSummaryBox__options nd-select:first-of-type div.nd-select__menu ul li:first-child')))
            
       
        except TimeoutException or StaleElementReferenceException:
                
            driver.close()
            sleep(2)
            
            chrome_options = webdriver.ChromeOptions()
            chrome_options.add_argument('--headless')
            driver = webdriver.Chrome('C:\\Users\\Federico\\Anaconda3\\Lib\\site-packages\\chromedriver.exe',chrome_options=chrome_options)
            driver.get(URL)

            print('exception_zone')
            sleep(3)
            down = driver.find_element_by_css_selector('body > div.nd-cityGuide__content.has-fixedNav > nd-cityguide > nd-cityguide-sections > section:nth-child(2) > div > nd-price-chart > div.ct-chart.ct-perfect-fourth > svg')
            ActionChains(driver).move_to_element(down).perform()
            
            visible_button = WebDriverWait(driver, 60).until(EC.visibility_of_element_located((By.CSS_SELECTOR , 'body > div.nd-cityGuide__content.has-fixedNav > nd-cityguide > nd-cityguide-sections > section:nth-child(2) > div > nd-price-chart > div.nd-cgSummaryBox > div.nd-cgSummaryBox__options > nd-select:nth-child(1) > div')))
            ActionChains(driver).move_to_element(visible_button).click().perform()
            sleep(uniform(0,1))
                
            visible_button = WebDriverWait(driver, 60).until(EC.visibility_of_element_located((By.CSS_SELECTOR , 'div.nd-cgSummaryBox__options nd-select:first-of-type div.nd-select__menu ul li:first-child')))
            ActionChains(driver).move_to_element(visible_button).click().perform()
            
        else:
            ActionChains(driver).move_to_element(visible_button).click().perform()


        #C) MOVE MOUSE TO NEUTRAL ZONE
        neutral_zone = WebDriverWait(driver, 60).until(EC.visibility_of_element_located((By.CSS_SELECTOR , 'body > div.nd-cityGuide__content.has-fixedNav > nd-cityguide > nd-cityguide-sections > section:nth-child(2) > div > nd-price-chart > div.nd-cgSummaryBox > div.nd-cgSummaryBox__texts')))
        ActionChains(driver).move_to_element(neutral_zone).click().perform()
        sleep(uniform(0,1))

        #D) MOVE MOUSE TO LINE PLOT
        down = driver.find_element_by_css_selector('div.nd-cgSection__trends')
        ActionChains(driver).move_to_element(down).perform()
        sleep(uniform(0,1))
        
        #E) FIND ALL POINTS OF THE GRAPH
        points = driver.find_elements_by_css_selector('nd-price-chart div.ct-perfect-fourth svg g.ct-series-a > line')

        #F) GRAB PRICE AND DATE FOR EVERY POINT IN GRAPH
        for point in points:
            ActionChains(driver).move_to_element(point).perform() 
            prezzo = WebDriverWait(driver, 60).until(EC.visibility_of_element_located((By.CSS_SELECTOR , 'div.nd-price-chart__tooltip div.nd-tooltip__container div:first-child')))

            data = WebDriverWait(driver, 60).until(EC.visibility_of_element_located((By.CSS_SELECTOR , 'div.nd-price-chart__tooltip div.nd-tooltip__container div:last-child')))

            row_reg_v.append('-'.join([data.text,prezzo.text]))
            
        writer_reg_v.writerow(row_reg_v)


#1.3) TAKE ALL PROVINCE URL
province = driver.find_element_by_css_selector('table tbody').find_elements_by_css_selector('tr')

URL_province = []
for provincia in province:
    provincia = provincia.find_element_by_css_selector('td a').get_attribute('href')
    URL_province.append(provincia)
    sleep(uniform(0, 1))
    
print('ho preso url delle province...')

#0.3)OPEN FILES TO WRITE
with open('Raw_data\\Veneto_province_affitti.csv', 'w',encoding="utf-8") as iterator3:
    writer_prov_a = csv.writer(iterator3, delimiter=',', quotechar='"' )
    with open('Raw_data\\Veneto_province_vendite.csv', 'w',encoding="utf-8") as iterator4:
        writer_prov_v = csv.writer(iterator4, delimiter=',', quotechar='"' )
        with open('Raw_data\\Veneto_comuni_affitti.csv', 'w',encoding="utf-8") as iterator5:
            writer_com_a = csv.writer(iterator5, delimiter=',', quotechar='"' )
            with open('Raw_data\\Veneto_comuni_vendite.csv', 'w',encoding="utf-8") as iterator6:
                writer_com_v = csv.writer(iterator6, delimiter=',', quotechar='"' )
                with open('Raw_data\\Veneto_zone_affitti.csv', 'w',encoding="utf-8") as iterator7:
                    writer_zone_a = csv.writer(iterator7, delimiter=',', quotechar='"' )
                    with open('Raw_data\\Veneto_zone_vendite.csv', 'w',encoding="utf-8") as iterator8:
                        writer_zone_v = csv.writer(iterator8, delimiter=',', quotechar='"' )  
                        
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#2) SEZIONE PROVINCE
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
                        
                        #FOR ALL PROVINCE:
                        count_p = 0

                        for URL in URL_province:

                            #2.1) GET URL
                            driver.get(URL)
                            row_prov_a = [URL]
                            row_prov_v = [URL]
                            
                            count_p += 1
                            print('province: ', count_p,'/',len(URL_province))
                            
                            #A) MOVE MOUSE TO  AFFITTI/VENDITE WINDOW
                            try:
                                visible_button = WebDriverWait(driver, 60).until(EC.visibility_of_element_located((By.CSS_SELECTOR , 'div.nd-cgSummaryBox__options nd-select:first-of-type div')))
                            
                            except TimeoutException or StaleElementReferenceException:
                                
                                driver.close()
                                sleep(2)
                                
                                chrome_options = webdriver.ChromeOptions()
                                chrome_options.add_argument('--headless')
                                driver = webdriver.Chrome('C:\\Users\\Federico\\Anaconda3\\Lib\\site-packages\\chromedriver.exe',chrome_options=chrome_options)
                                driver.get(URL)
                                
                                print('exception_zone')
                                sleep(3)
                                visible_button = WebDriverWait(driver, 60).until(EC.visibility_of_element_located((By.CSS_SELECTOR , 'div.nd-cgSummaryBox__options nd-select:first-of-type div')))
                                ActionChains(driver).move_to_element(visible_button).click().perform()
                                sleep(uniform(0,1))         
                                
                            else:
                                ActionChains(driver).move_to_element(visible_button).click().perform()
                                sleep(uniform(0,1))
                            
                            #B) CLICK AFFITTI SECTION
                            try:
                                visible_button = WebDriverWait(driver, 60).until(EC.visibility_of_element_located((By.CSS_SELECTOR , 'div.nd-cgSummaryBox__options nd-select:first-of-type div.nd-select__menu ul li:last-child')))
                                
                           
                            except TimeoutException or StaleElementReferenceException:
                                    
                                driver.close()
                                sleep(2)
                                
                                chrome_options = webdriver.ChromeOptions()
                                chrome_options.add_argument('--headless')
                                driver = webdriver.Chrome('C:\\Users\\Federico\\Anaconda3\\Lib\\site-packages\\chromedriver.exe',chrome_options=chrome_options)
                                driver.get(URL)

                                print('exception_zone')
                                sleep(3)
                                down = driver.find_element_by_css_selector('body > div.nd-cityGuide__content.has-fixedNav > nd-cityguide > nd-cityguide-sections > section:nth-child(2) > div > nd-price-chart > div.ct-chart.ct-perfect-fourth > svg')
                                ActionChains(driver).move_to_element(down).perform()
                                
                                visible_button = WebDriverWait(driver, 60).until(EC.visibility_of_element_located((By.CSS_SELECTOR , 'body > div.nd-cityGuide__content.has-fixedNav > nd-cityguide > nd-cityguide-sections > section:nth-child(2) > div > nd-price-chart > div.nd-cgSummaryBox > div.nd-cgSummaryBox__options > nd-select:nth-child(1) > div')))
                                ActionChains(driver).move_to_element(visible_button).click().perform()
                                sleep(uniform(0,1))
                                    
                                visible_button = WebDriverWait(driver, 60).until(EC.visibility_of_element_located((By.CSS_SELECTOR , 'div.nd-cgSummaryBox__options nd-select:first-of-type div.nd-select__menu ul li:last-child')))
                                ActionChains(driver).move_to_element(visible_button).click().perform()
                                
                            else:
                                ActionChains(driver).move_to_element(visible_button).click().perform()

                            
                            #C) MOVE MOUSE TO NEUTRAL ZONE
                            neutral_zone = WebDriverWait(driver, 60).until(EC.visibility_of_element_located((By.CSS_SELECTOR , 'body > div.nd-cityGuide__content.has-fixedNav > nd-cityguide > nd-cityguide-sections > section:nth-child(2) > div > nd-price-chart > div.nd-cgSummaryBox > div.nd-cgSummaryBox__texts')))
                            ActionChains(driver).move_to_element(neutral_zone).click().perform()
                            sleep(uniform(0,1))
                            
                            #D) MOVE MOUSE TO LINE PLOT 
                            down = driver.find_element_by_css_selector('div.nd-cgSection__trends')
                            ActionChains(driver).move_to_element(down).perform()
                            sleep(uniform(0,1))
                            
                            #E) FIND ALL POINTS OF THE GRAPH
                            points = driver.find_elements_by_css_selector('nd-price-chart div.ct-perfect-fourth svg g.ct-series-a > line')
                            
                            #F) GRAB PRICE AND DATE FOR EVERY POINT IN GRAPH
                            try:
                                for point in points:
                                
                                    ActionChains(driver).move_to_element(point).perform() 
                                    prezzo = WebDriverWait(driver, 60).until(EC.visibility_of_element_located((By.CSS_SELECTOR , 'div.nd-price-chart__tooltip div.nd-tooltip__container div:first-child')))
                                
                                    data = WebDriverWait(driver, 60).until(EC.visibility_of_element_located((By.CSS_SELECTOR , 'div.nd-price-chart__tooltip div.nd-tooltip__container div:last-child')))
                                    row_prov_a.append('-'.join([data.text,prezzo.text]))
                                    
                                writer_prov_a.writerow(row_prov_a)
                                
                            except:
                                driver.refresh()
                                row_prov_a.clear()
                                row_prov_a = [URL]
                                sleep(15+uniform(0,1))
                                points = driver.find_elements_by_css_selector('nd-price-chart div.ct-perfect-fourth svg g.ct-series-a > line')
                                
                                for point in points:
                                    
                                    ActionChains(driver).move_to_element(point).perform() 
                                    prezzo = WebDriverWait(driver, 60).until(EC.visibility_of_element_located((By.CSS_SELECTOR , 'div.nd-price-chart__tooltip div.nd-tooltip__container div:first-child')))
                                
                                    data = WebDriverWait(driver, 60).until(EC.visibility_of_element_located((By.CSS_SELECTOR , 'div.nd-price-chart__tooltip div.nd-tooltip__container div:last-child')))
                                    
                                    
                                    row_prov_a.append('-'.join([data.text,prezzo.text]))
                                
                                writer_prov_a.writerow(row_prov_a)
        
                            #A) MOVE MOUSE TO  AFFITTI/VENDITE WINDOW
                            try:
                                visible_button = WebDriverWait(driver, 60).until(EC.visibility_of_element_located((By.CSS_SELECTOR , 'div.nd-cgSummaryBox__options nd-select:first-of-type div')))
                            
                            except TimeoutException or StaleElementReferenceException:
                                
                                driver.close()
                                sleep(2)
                                
                                chrome_options = webdriver.ChromeOptions()
                                chrome_options.add_argument('--headless')
                                driver = webdriver.Chrome('C:\\Users\\Federico\\Anaconda3\\Lib\\site-packages\\chromedriver.exe',chrome_options=chrome_options)
                                driver.get(URL)
                                
                                print('exception_zone')
                                sleep(3)
                                visible_button = WebDriverWait(driver, 60).until(EC.visibility_of_element_located((By.CSS_SELECTOR , 'div.nd-cgSummaryBox__options nd-select:first-of-type div')))
                                ActionChains(driver).move_to_element(visible_button).click().perform()
                                sleep(uniform(0,1))         
                                
                            else:
                                ActionChains(driver).move_to_element(visible_button).click().perform()
                                sleep(uniform(0,1))
                            
                            #B) CLICK VENDITE SECTION
                            try:
                                visible_button = WebDriverWait(driver, 60).until(EC.visibility_of_element_located((By.CSS_SELECTOR , 'div.nd-cgSummaryBox__options nd-select:first-of-type div.nd-select__menu ul li:first-child')))
                                
                           
                            except TimeoutException or StaleElementReferenceException:
                                    
                                driver.close()
                                sleep(2)
                                
                                chrome_options = webdriver.ChromeOptions()
                                chrome_options.add_argument('--headless')
                                driver = webdriver.Chrome('C:\\Users\\Federico\\Anaconda3\\Lib\\site-packages\\chromedriver.exe',chrome_options=chrome_options)
                                driver.get(URL)

                                print('exception_zone')
                                sleep(3)
                                down = driver.find_element_by_css_selector('body > div.nd-cityGuide__content.has-fixedNav > nd-cityguide > nd-cityguide-sections > section:nth-child(2) > div > nd-price-chart > div.ct-chart.ct-perfect-fourth > svg')
                                ActionChains(driver).move_to_element(down).perform()
                                
                                visible_button = WebDriverWait(driver, 60).until(EC.visibility_of_element_located((By.CSS_SELECTOR , 'body > div.nd-cityGuide__content.has-fixedNav > nd-cityguide > nd-cityguide-sections > section:nth-child(2) > div > nd-price-chart > div.nd-cgSummaryBox > div.nd-cgSummaryBox__options > nd-select:nth-child(1) > div')))
                                ActionChains(driver).move_to_element(visible_button).click().perform()
                                sleep(uniform(0,1))
                                    
                                visible_button = WebDriverWait(driver, 60).until(EC.visibility_of_element_located((By.CSS_SELECTOR , 'div.nd-cgSummaryBox__options nd-select:first-of-type div.nd-select__menu ul li:first-child')))
                                ActionChains(driver).move_to_element(visible_button).click().perform()
                                
                            else:
                                ActionChains(driver).move_to_element(visible_button).click().perform()
                            
                            
                            #C) MOVE MOUSE TO NEUTRAL ZONE
                            neutral_zone = WebDriverWait(driver, 60).until(EC.visibility_of_element_located((By.CSS_SELECTOR , 'body > div.nd-cityGuide__content.has-fixedNav > nd-cityguide > nd-cityguide-sections > section:nth-child(2) > div > nd-price-chart > div.nd-cgSummaryBox > div.nd-cgSummaryBox__texts')))
                            ActionChains(driver).move_to_element(neutral_zone).click().perform()
                            sleep(uniform(0,1))
                            
                            #D) MOVE MOUSE TO LINE PLOT
                            down = driver.find_element_by_css_selector('div.nd-cgSection__trends')
                            ActionChains(driver).move_to_element(down).perform()
                            sleep(uniform(0,1))
                            
                            #E) FIND ALL POINTS OF THE GRAPH
                            points = driver.find_elements_by_css_selector('nd-price-chart div.ct-perfect-fourth svg g.ct-series-a > line')
                            
                            #F) GRAB PRICE AND DATE FOR EVERY POINT IN GRAPH
                            try:
                                for point in points:
                                
                                    ActionChains(driver).move_to_element(point).perform() 
                                    prezzo = WebDriverWait(driver, 60).until(EC.visibility_of_element_located((By.CSS_SELECTOR , 'div.nd-price-chart__tooltip div.nd-tooltip__container div:first-child')))
                                
                                    data = WebDriverWait(driver, 60).until(EC.visibility_of_element_located((By.CSS_SELECTOR , 'div.nd-price-chart__tooltip div.nd-tooltip__container div:last-child')))
                                    row_prov_v.append('-'.join([data.text,prezzo.text]))
                                    
                                writer_prov_v.writerow(row_prov_v)
                                                                
                            except:
                                driver.refresh()
                                row_prov_v.clear()
                                row_prov_v = [URL]
                                sleep(15+uniform(0,1))
                                points = driver.find_elements_by_css_selector('nd-price-chart div.ct-perfect-fourth svg g.ct-series-a > line')
                                
                                for point in points:
                                    
                                    ActionChains(driver).move_to_element(point).perform() 
                                    prezzo = WebDriverWait(driver, 60).until(EC.visibility_of_element_located((By.CSS_SELECTOR , 'div.nd-price-chart__tooltip div.nd-tooltip__container div:first-child')))
                                
                                    data = WebDriverWait(driver, 60).until(EC.visibility_of_element_located((By.CSS_SELECTOR , 'div.nd-price-chart__tooltip div.nd-tooltip__container div:last-child')))
                                    
                                    
                                    row_prov_v.append('-'.join([data.text,prezzo.text]))
                                    
                                writer_prov_v.writerow(row_prov_v)

    
    
                            #2.2) ESPANDI TAB COMUNI
                            
                            last_row = driver.find_element_by_css_selector('table tbody:last-child')
                            ActionChains(driver).move_to_element(last_row).perform()
                            
                            try :
                                visible_button = WebDriverWait(driver, 60).until(EC.visibility_of_element_located((By.CSS_SELECTOR , 'body div nd-cityguide nd-cityguide-sections section:last-child button')))
                            except:
                                print('there aren\'t so many comuni here' )
                            else:
                                visible_button.click()
                                
                            sleep(uniform(3, 4))
     
                            URL_comuni = []
                            comuni = driver.find_element_by_css_selector('table tbody').find_elements_by_css_selector('tr')
                            print('ho espanso tab comuni della provincia...')
                    
                            #2.3) TAKE ALL COMUNI URL
                            for comune in comuni:
                    
                                comune = comune.find_element_by_css_selector('td a').get_attribute('href')
                     
                                URL_comuni.append(comune)
                                sleep(uniform(0, 1))
                            print('ho preso url dei comuni...')
                            
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#3) SEZIONE COMUNI                            
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
                            
                            #FOR ALL COMUNI:
                            count_c = 0

                            for URL in URL_comuni:
                                
                                #3.1) GET URL
                                driver.get(URL)
                                row_com_a = [URL]
                                row_com_v = [URL]
                                count_c += 1
                                print('comuni: ', count_c,'/',len(URL_comuni))
            
    
                           
                                #A) MOVE MOUSE TO  AFFITTI/VENDITE WINDOW
                                try:
                                    visible_button = WebDriverWait(driver, 60).until(EC.visibility_of_element_located((By.CSS_SELECTOR , 'div.nd-cgSummaryBox__options nd-select:first-of-type div')))
                                
                                except TimeoutException or StaleElementReferenceException:
                                    
                                    driver.close()
                                    sleep(2)
                                    
                                    chrome_options = webdriver.ChromeOptions()
                                    chrome_options.add_argument('--headless')
                                    driver = webdriver.Chrome('C:\\Users\\Federico\\Anaconda3\\Lib\\site-packages\\chromedriver.exe',chrome_options=chrome_options)
                                    driver.get(URL)
                                    
                                    print('exception_zone')
                                    sleep(3)
                                    visible_button = WebDriverWait(driver, 60).until(EC.visibility_of_element_located((By.CSS_SELECTOR , 'div.nd-cgSummaryBox__options nd-select:first-of-type div')))
                                    ActionChains(driver).move_to_element(visible_button).click().perform()
                                    sleep(uniform(0,1))         
                                    
                                else:
                                    ActionChains(driver).move_to_element(visible_button).click().perform()
                                    sleep(uniform(0,1))
                                #B) CLICK TO  AFFITTI SECTION
                                try:
                                    visible_button = WebDriverWait(driver, 60).until(EC.visibility_of_element_located((By.CSS_SELECTOR , 'div.nd-cgSummaryBox__options nd-select:first-of-type div.nd-select__menu ul li:last-child')))
                                    
                               
                                except TimeoutException or StaleElementReferenceException:
                                        
                                    driver.close()
                                    sleep(2)
                                    
                                    chrome_options = webdriver.ChromeOptions()
                                    chrome_options.add_argument('--headless')
                                    driver = webdriver.Chrome('C:\\Users\\Federico\\Anaconda3\\Lib\\site-packages\\chromedriver.exe',chrome_options=chrome_options)
                                    driver.get(URL)

                                    print('exception_zone')
                                    sleep(3)
                                    down = driver.find_element_by_css_selector('body > div.nd-cityGuide__content.has-fixedNav > nd-cityguide > nd-cityguide-sections > section:nth-child(2) > div > nd-price-chart > div.ct-chart.ct-perfect-fourth > svg')
                                    ActionChains(driver).move_to_element(down).perform()
                                    
                                    visible_button = WebDriverWait(driver, 60).until(EC.visibility_of_element_located((By.CSS_SELECTOR , 'body > div.nd-cityGuide__content.has-fixedNav > nd-cityguide > nd-cityguide-sections > section:nth-child(2) > div > nd-price-chart > div.nd-cgSummaryBox > div.nd-cgSummaryBox__options > nd-select:nth-child(1) > div')))
                                    ActionChains(driver).move_to_element(visible_button).click().perform()
                                    sleep(uniform(0,1))
                                        
                                    visible_button = WebDriverWait(driver, 60).until(EC.visibility_of_element_located((By.CSS_SELECTOR , 'div.nd-cgSummaryBox__options nd-select:first-of-type div.nd-select__menu ul li:last-child')))
                                    ActionChains(driver).move_to_element(visible_button).click().perform()
                                    
                                else:
                                    ActionChains(driver).move_to_element(visible_button).click().perform()

                                
                                #C) MOVE MOUSE TO NEUTRAL ZONE
                                neutral_zone = WebDriverWait(driver, 60).until(EC.visibility_of_element_located((By.CSS_SELECTOR , 'body > div.nd-cityGuide__content.has-fixedNav > nd-cityguide > nd-cityguide-sections > section:nth-child(2) > div > nd-price-chart > div.nd-cgSummaryBox > div.nd-cgSummaryBox__texts')))
                                ActionChains(driver).move_to_element(neutral_zone).click().perform()
                                sleep(uniform(0,1))
                                          
                                #D) MOVE MOUSE TO LINE PLOT
                                down = driver.find_element_by_css_selector('div.nd-cgSection__trends')
                                ActionChains(driver).move_to_element(down).perform()
                                sleep(uniform(0,1))
                                
                                #E) FIND ALL POINTS OF THE GRAPH
                                points = driver.find_elements_by_css_selector('nd-price-chart div.ct-perfect-fourth svg g.ct-series-a > line')
            
                                #F) GRAB PRICE AND DATE FOR EVERY POINT IN GRAPH
                                try:
                                    for point in points:
                                    
                                        ActionChains(driver).move_to_element(point).perform() 
                                        prezzo = WebDriverWait(driver, 60).until(EC.visibility_of_element_located((By.CSS_SELECTOR , 'div.nd-price-chart__tooltip div.nd-tooltip__container div:first-child')))
                                    
                                        data = WebDriverWait(driver, 60).until(EC.visibility_of_element_located((By.CSS_SELECTOR , 'div.nd-price-chart__tooltip div.nd-tooltip__container div:last-child')))
                                        row_com_a.append('-'.join([data.text,prezzo.text]))
                                    writer_com_a.writerow(row_com_a)
                                                                        
                                except:
                                    driver.refresh()
                                    row_com_a.clear()
                                    row_com_a = [URL]
                                    sleep(15+uniform(0,1))
                                    points = driver.find_elements_by_css_selector('nd-price-chart div.ct-perfect-fourth svg g.ct-series-a > line')
                                    
                                    for point in points:
                                        
                                        ActionChains(driver).move_to_element(point).perform() 
                                        prezzo = WebDriverWait(driver, 60).until(EC.visibility_of_element_located((By.CSS_SELECTOR , 'div.nd-price-chart__tooltip div.nd-tooltip__container div:first-child')))
                                    
                                        data = WebDriverWait(driver, 60).until(EC.visibility_of_element_located((By.CSS_SELECTOR , 'div.nd-price-chart__tooltip div.nd-tooltip__container div:last-child')))
                                        
                                        
                                        row_com_a.append('-'.join([data.text,prezzo.text]))
                                        
                                    writer_com_a.writerow(row_com_a)
                        
                                #A) MOVE MOUSE TO  AFFITTI/VENDITE WINDOW
                                try:
                                    visible_button = WebDriverWait(driver, 60).until(EC.visibility_of_element_located((By.CSS_SELECTOR , 'div.nd-cgSummaryBox__options nd-select:first-of-type div')))
                                
                                except TimeoutException or StaleElementReferenceException:
                                    
                                    driver.close()
                                    sleep(2)
                                    
                                    chrome_options = webdriver.ChromeOptions()
                                    chrome_options.add_argument('--headless')
                                    driver = webdriver.Chrome('C:\\Users\\Federico\\Anaconda3\\Lib\\site-packages\\chromedriver.exe',chrome_options=chrome_options)
                                    driver.get(URL)
                                    
                                    print('exception_zone')
                                    sleep(3)
                                    visible_button = WebDriverWait(driver, 60).until(EC.visibility_of_element_located((By.CSS_SELECTOR , 'div.nd-cgSummaryBox__options nd-select:first-of-type div')))
                                    ActionChains(driver).move_to_element(visible_button).click().perform()
                                    sleep(uniform(0,1))         
                                    
                                else:
                                    ActionChains(driver).move_to_element(visible_button).click().perform()
                                    sleep(uniform(0,1))
        
                                #B) CLICK VENDITE SECTION
                                try:
                                    visible_button = WebDriverWait(driver, 60).until(EC.visibility_of_element_located((By.CSS_SELECTOR , 'div.nd-cgSummaryBox__options nd-select:first-of-type div.nd-select__menu ul li:first-child')))
                                    
                                
                                except TimeoutException or StaleElementReferenceException:
                                    
                                    driver.close()
                                    sleep(2)
                                    
                                    chrome_options = webdriver.ChromeOptions()
                                    chrome_options.add_argument('--headless')
                                    driver = webdriver.Chrome('C:\\Users\\Federico\\Anaconda3\\Lib\\site-packages\\chromedriver.exe',chrome_options=chrome_options)
                                    driver.get(URL)
                                    print('exception')
                                    sleep(3)
                                    
                                    down = driver.find_element_by_css_selector('body > div.nd-cityGuide__content.has-fixedNav > nd-cityguide > nd-cityguide-sections > section:nth-child(2) > div > nd-price-chart > div.ct-chart.ct-perfect-fourth > svg')
                                    ActionChains(driver).move_to_element(down).perform()
                                    
                                    visible_button = WebDriverWait(driver, 60).until(EC.visibility_of_element_located((By.CSS_SELECTOR , 'body > div.nd-cityGuide__content.has-fixedNav > nd-cityguide > nd-cityguide-sections > section:nth-child(2) > div > nd-price-chart > div.nd-cgSummaryBox > div.nd-cgSummaryBox__options > nd-select:nth-child(1) > div')))
                                    
                                    ActionChains(driver).move_to_element(visible_button).click().perform()
                                    sleep(uniform(0,1))
                                        
                                    visible_button = WebDriverWait(driver, 60).until(EC.visibility_of_element_located((By.CSS_SELECTOR , 'div.nd-cgSummaryBox__options nd-select:first-of-type div.nd-select__menu ul li:first-child')))
                                    ActionChains(driver).move_to_element(visible_button).click().perform()
                                
                                else:
                                    ActionChains(driver).move_to_element(visible_button).click().perform()

                                
                                #C) MOVE MOUSE TO NEUTRAL ZONE
                                neutral_zone = WebDriverWait(driver, 60).until(EC.visibility_of_element_located((By.CSS_SELECTOR , 'body > div.nd-cityGuide__content.has-fixedNav > nd-cityguide > nd-cityguide-sections > section:nth-child(2) > div > nd-price-chart > div.nd-cgSummaryBox > div.nd-cgSummaryBox__texts')))
                                ActionChains(driver).move_to_element(neutral_zone).click().perform()
                                sleep(uniform(0,1))
                                
                                #D) MOVE MOUSE TO LINE PLOT
                                down = driver.find_element_by_css_selector('div.nd-cgSection__trends')
                                ActionChains(driver).move_to_element(down).perform()
                                sleep(uniform(0,1))
        
                                #E) FIND ALL POINTS OF THE GRAPH
                                points = driver.find_elements_by_css_selector('nd-price-chart div.ct-perfect-fourth svg g.ct-series-a > line')
                                
                                #F) GRAB PRICE AND DATE FOR EVERY POINT IN GRAPH
                                try:
                                    for point in points:
                                    
                                        ActionChains(driver).move_to_element(point).perform() 
                                        prezzo = WebDriverWait(driver, 60).until(EC.visibility_of_element_located((By.CSS_SELECTOR , 'div.nd-price-chart__tooltip div.nd-tooltip__container div:first-child')))
                                    
                                        data = WebDriverWait(driver, 60).until(EC.visibility_of_element_located((By.CSS_SELECTOR , 'div.nd-price-chart__tooltip div.nd-tooltip__container div:last-child')))
                                        row_com_v.append('-'.join([data.text,prezzo.text]))
                                    writer_com_v.writerow(row_com_v)
                                                                            
                                except:
                                    driver.refresh()
                                    row_com_v.clear()
                                    row_com_v = [URL]
                                    sleep(15+uniform(0,1))
                                    points = driver.find_elements_by_css_selector('nd-price-chart div.ct-perfect-fourth svg g.ct-series-a > line')
                                    
                                    for point in points:
                                        
                                        ActionChains(driver).move_to_element(point).perform() 
                                        prezzo = WebDriverWait(driver, 60).until(EC.visibility_of_element_located((By.CSS_SELECTOR , 'div.nd-price-chart__tooltip div.nd-tooltip__container div:first-child')))
                                    
                                        data = WebDriverWait(driver, 60).until(EC.visibility_of_element_located((By.CSS_SELECTOR , 'div.nd-price-chart__tooltip div.nd-tooltip__container div:last-child')))
                                        
                                        
                                        row_com_v.append('-'.join([data.text,prezzo.text]))
                                    writer_com_v.writerow(row_com_v)
    
                            
                                #3.2) ESPANDI TAB ZONE
                                check_zone = driver.find_element_by_css_selector('table thead tr th:first-child').text
                                if check_zone == 'Comuni':
                                    print('qui NON CI SONO ZONE!!!!')
                                    continue
                                else: 
                                    print('zone PRESENTI!')
                                last_row = driver.find_element_by_css_selector('table tbody:last-child')
                                ActionChains(driver).move_to_element(last_row).perform()
                                try:
                                    visible_button = WebDriverWait(driver, 60).until(EC.visibility_of_element_located((By.CSS_SELECTOR , 'body div nd-cityguide nd-cityguide-sections section:last-child button')))
                                except:
                                    print('there aren\'t so many zone here' )
                                else:
                                    visible_button.click()
                                    sleep(uniform(0,1))
        
                                URL_zone = []
                                zone = driver.find_element_by_css_selector('table tbody').find_elements_by_css_selector('tr')
                                print('ho espanso tab zone della provincia...')
                
                                #3.3) TAKE ALL ZONE URL
                                for zona in zone:
                                    
                                    zona = zona.find_element_by_css_selector('td a').get_attribute('href')
                                    URL_zone.append(zona)

                                print('ho preso url delle zone...')
                    
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#4) SEZIONE ZONE                              
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
                                
                                #FOR ALL ZONE:
                                count_z = 0
                
                                for URL in URL_zone:
                                    
                                    #4.1) GET URL
                                    driver.get(URL)
                                    row_zone_a = [URL]
                                    row_zone_v = [URL]
                                    count_z += 1
                                    print('zone: ', count_z,'/',len(URL_zone))
                                
    
                                     
    
                                    #A) MOVE MOUSE TO  AFFITTI/VENDITE WINDOW
                                    try:
                                        visible_button = WebDriverWait(driver, 60).until(EC.visibility_of_element_located((By.CSS_SELECTOR , 'div.nd-cgSummaryBox__options nd-select:first-of-type div')))
                                    
                                    except TimeoutException or StaleElementReferenceException:
                                        
                                        driver.close()
                                        sleep(2)
                                        
                                        chrome_options = webdriver.ChromeOptions()
                                        chrome_options.add_argument('--headless')
                                        driver = webdriver.Chrome('C:\\Users\\Federico\\Anaconda3\\Lib\\site-packages\\chromedriver.exe',chrome_options=chrome_options)
                                        driver.get(URL)
                                        
                                        print('exception_zone')
                                        sleep(3)
                                        visible_button = WebDriverWait(driver, 60).until(EC.visibility_of_element_located((By.CSS_SELECTOR , 'div.nd-cgSummaryBox__options nd-select:first-of-type div')))
                                        ActionChains(driver).move_to_element(visible_button).click().perform()
                                        sleep(uniform(0,1))         
                                        
                                    else:
                                        ActionChains(driver).move_to_element(visible_button).click().perform()
                                        sleep(uniform(0,1))
                                    
                                    #B) CLICK AFFITTI SECTION                                    
                                    try:
                                        visible_button = WebDriverWait(driver, 60).until(EC.visibility_of_element_located((By.CSS_SELECTOR , 'div.nd-cgSummaryBox__options nd-select:first-of-type div.nd-select__menu ul li:last-child')))
                                        
                                   
                                    except TimeoutException or StaleElementReferenceException:
                                            
                                        driver.close()
                                        sleep(2)
                                        
                                        chrome_options = webdriver.ChromeOptions()
                                        chrome_options.add_argument('--headless')
                                        driver = webdriver.Chrome('C:\\Users\\Federico\\Anaconda3\\Lib\\site-packages\\chromedriver.exe',chrome_options=chrome_options)
                                        driver.get(URL)

                                        print('exception_zone')
                                        sleep(3)
                                        down = driver.find_element_by_css_selector('body > div.nd-cityGuide__content.has-fixedNav > nd-cityguide > nd-cityguide-sections > section:nth-child(2) > div > nd-price-chart > div.ct-chart.ct-perfect-fourth > svg')
                                        ActionChains(driver).move_to_element(down).perform()
                                        
                                        visible_button = WebDriverWait(driver, 60).until(EC.visibility_of_element_located((By.CSS_SELECTOR , 'body > div.nd-cityGuide__content.has-fixedNav > nd-cityguide > nd-cityguide-sections > section:nth-child(2) > div > nd-price-chart > div.nd-cgSummaryBox > div.nd-cgSummaryBox__options > nd-select:nth-child(1) > div')))
                                        ActionChains(driver).move_to_element(visible_button).click().perform()
                                        sleep(uniform(0,1))
                                            
                                        visible_button = WebDriverWait(driver, 60).until(EC.visibility_of_element_located((By.CSS_SELECTOR , 'div.nd-cgSummaryBox__options nd-select:first-of-type div.nd-select__menu ul li:last-child')))
                                        ActionChains(driver).move_to_element(visible_button).click().perform()
                                        
                                    else:
                                        ActionChains(driver).move_to_element(visible_button).click().perform()
                                
                                    #C) MOVE MOUSE TO NEUTRAL ZONE
                                    neutral_zone = WebDriverWait(driver, 60).until(EC.visibility_of_element_located((By.CSS_SELECTOR , 'body > div.nd-cityGuide__content.has-fixedNav > nd-cityguide > nd-cityguide-sections > section:nth-child(2) > div > nd-price-chart > div.nd-cgSummaryBox > div.nd-cgSummaryBox__texts')))
                                    ActionChains(driver).move_to_element(neutral_zone).click().perform()
                                    sleep(uniform(0,1))
                                    
                                    #D) MOVE MOUSE TO LINE PLOT 
                                    down = driver.find_element_by_css_selector('div.nd-cgSection__trends')
                                    ActionChains(driver).move_to_element(down).perform()
                                    sleep(uniform(0,1))
                                
                                    #E) FIND ALL POINTS OF THE GRAPH
                                    points = driver.find_elements_by_css_selector('nd-price-chart div.ct-perfect-fourth svg g.ct-series-a > line')
                                    
                                    #F) GRAB PRICE AND DATE FOR EVERY POINT IN GRAPH
                                    try:
                                        for point in points:
                                        
                                            ActionChains(driver).move_to_element(point).perform() 
                                            prezzo = WebDriverWait(driver, 60).until(EC.visibility_of_element_located((By.CSS_SELECTOR , 'div.nd-price-chart__tooltip div.nd-tooltip__container div:first-child')))
                                        
                                            data = WebDriverWait(driver, 60).until(EC.visibility_of_element_located((By.CSS_SELECTOR , 'div.nd-price-chart__tooltip div.nd-tooltip__container div:last-child')))
                                            row_zone_a.append('-'.join([data.text,prezzo.text]))
                                        writer_zone_a.writerow(row_zone_a)
                                                                                
                                    except:
                                        driver.refresh()
                                        row_zone_a.clear()
                                        row_zone_a = [URL]
                                        sleep(15+uniform(0,1))
                                        points = driver.find_elements_by_css_selector('nd-price-chart div.ct-perfect-fourth svg g.ct-series-a > line')
                                        
                                        for point in points:
                                            
                                            ActionChains(driver).move_to_element(point).perform() 
                                            prezzo = WebDriverWait(driver, 60).until(EC.visibility_of_element_located((By.CSS_SELECTOR , 'div.nd-price-chart__tooltip div.nd-tooltip__container div:first-child')))
                                        
                                            data = WebDriverWait(driver, 60).until(EC.visibility_of_element_located((By.CSS_SELECTOR , 'div.nd-price-chart__tooltip div.nd-tooltip__container div:last-child')))
                                            
                                            
                                            row_zone_a.append('-'.join([data.text,prezzo.text]))
                                        writer_zone_a.writerow(row_zone_a)
                                    
                                    
                                    
    
    
                                    #A) MOVE MOUSE TO  AFFITTI/VENDITE WINDOW
                                    try:
                                        visible_button = WebDriverWait(driver, 60).until(EC.visibility_of_element_located((By.CSS_SELECTOR , 'div.nd-cgSummaryBox__options nd-select:first-of-type div')))
                                    
                                    except TimeoutException or StaleElementReferenceException:
                                        
                                        driver.close()
                                        sleep(2)
                                        
                                        chrome_options = webdriver.ChromeOptions()
                                        chrome_options.add_argument('--headless')
                                        driver = webdriver.Chrome('C:\\Users\\Federico\\Anaconda3\\Lib\\site-packages\\chromedriver.exe',chrome_options=chrome_options)
                                        driver.get(URL)
                                        
                                        print('exception_zone')
                                        sleep(3)
                                        visible_button = WebDriverWait(driver, 60).until(EC.visibility_of_element_located((By.CSS_SELECTOR , 'div.nd-cgSummaryBox__options nd-select:first-of-type div')))
                                        ActionChains(driver).move_to_element(visible_button).click().perform()
                                        sleep(uniform(0,1))         
                                        
                                    else:
                                        ActionChains(driver).move_to_element(visible_button).click().perform()
                                        sleep(uniform(0,1))
                                    
                                    
                                    
                                    #B) CLICK VENDITE SECTION
                                    try:
                                        visible_button = WebDriverWait(driver, 60).until(EC.visibility_of_element_located((By.CSS_SELECTOR , 'div.nd-cgSummaryBox__options nd-select:first-of-type div.nd-select__menu ul li:first-child')))
                                        
                                   
                                    except TimeoutException or StaleElementReferenceException:
                                            
                                        driver.close()
                                        sleep(2)
                                        
                                        chrome_options = webdriver.ChromeOptions()
                                        chrome_options.add_argument('--headless')
                                        driver = webdriver.Chrome('C:\\Users\\Federico\\Anaconda3\\Lib\\site-packages\\chromedriver.exe',chrome_options=chrome_options)
                                        driver.get(URL)

                                        print('exception_zone')
                                        sleep(3)
                                        down = driver.find_element_by_css_selector('body > div.nd-cityGuide__content.has-fixedNav > nd-cityguide > nd-cityguide-sections > section:nth-child(2) > div > nd-price-chart > div.ct-chart.ct-perfect-fourth > svg')
                                        ActionChains(driver).move_to_element(down).perform()
                                        
                                        visible_button = WebDriverWait(driver, 60).until(EC.visibility_of_element_located((By.CSS_SELECTOR , 'body > div.nd-cityGuide__content.has-fixedNav > nd-cityguide > nd-cityguide-sections > section:nth-child(2) > div > nd-price-chart > div.nd-cgSummaryBox > div.nd-cgSummaryBox__options > nd-select:nth-child(1) > div')))
                                        ActionChains(driver).move_to_element(visible_button).click().perform()
                                        sleep(uniform(0,1))
                                            
                                        visible_button = WebDriverWait(driver, 60).until(EC.visibility_of_element_located((By.CSS_SELECTOR , 'div.nd-cgSummaryBox__options nd-select:first-of-type div.nd-select__menu ul li:first-child')))
                                        ActionChains(driver).move_to_element(visible_button).click().perform()
                                        
                                    else:
                                        ActionChains(driver).move_to_element(visible_button).click().perform()
                                        
       
                                    #C) MOVE MOUSE TO NEUTRAL ZONE
                                    neutral_zone = WebDriverWait(driver, 60).until(EC.visibility_of_element_located((By.CSS_SELECTOR , 'body > div.nd-cityGuide__content.has-fixedNav > nd-cityguide > nd-cityguide-sections > section:nth-child(2) > div > nd-price-chart > div.nd-cgSummaryBox > div.nd-cgSummaryBox__texts')))
                                    ActionChains(driver).move_to_element(neutral_zone).click().perform()
                                    sleep(uniform(0,1))
                                    
                                    #D) MOVE MOUSE TO LINE PLOT
                                    down = driver.find_element_by_css_selector('div.nd-cgSection__trends')
                                    ActionChains(driver).move_to_element(down).perform()
                                    sleep(uniform(0,1))

    
                                    #E) FIND ALL POINTS OF THE GRAPH
                                    points = driver.find_elements_by_css_selector('nd-price-chart div.ct-perfect-fourth svg g.ct-series-a > line')
                                    
                                    #F) GRAB PRICE AND DATE FOR EVERY POINT IN GRAPH
                                    try:
                                        for point in points:
                                        
                                            ActionChains(driver).move_to_element(point).perform() 
                                            prezzo = WebDriverWait(driver, 60).until(EC.visibility_of_element_located((By.CSS_SELECTOR , 'div.nd-price-chart__tooltip div.nd-tooltip__container div:first-child')))
                                        
                                            data = WebDriverWait(driver, 60).until(EC.visibility_of_element_located((By.CSS_SELECTOR , 'div.nd-price-chart__tooltip div.nd-tooltip__container div:last-child')))
                                            row_zone_v.append('-'.join([data.text,prezzo.text]))
                                        writer_zone_v.writerow(row_zone_v)
                                        
                                    except:
                                        driver.refresh()
                                        row_zone_v.clear()
                                        row_zone_v = [URL]
                                        sleep(15+uniform(0,1))
                                        points = driver.find_elements_by_css_selector('nd-price-chart div.ct-perfect-fourth svg g.ct-series-a > line')
                                        
                                        for point in points:
                                            
                                            ActionChains(driver).move_to_element(point).perform() 
                                            prezzo = WebDriverWait(driver, 60).until(EC.visibility_of_element_located((By.CSS_SELECTOR , 'div.nd-price-chart__tooltip div.nd-tooltip__container div:first-child')))
                                        
                                            data = WebDriverWait(driver, 60).until(EC.visibility_of_element_located((By.CSS_SELECTOR , 'div.nd-price-chart__tooltip div.nd-tooltip__container div:last-child')))
                                            
                                            
                                            row_zone_v.append('-'.join([data.text,prezzo.text]))
                                        writer_zone_v.writerow(row_zone_v)
  
#0.4) CLOSE WEBDRIVER
driver.close()   
end = datetime.now()              
print('THE END')
time_exe = end - start
print(time_exe)
