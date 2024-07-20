from selenium import webdriver
from selenium.webdriver.common.by import By
import arabic_reshaper
from bidi.algorithm import get_display
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def convert(text):
    reshaped_text = arabic_reshaper.reshape(text)
    converted = get_display(reshaped_text)
    return converted

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(options=options)

cities = ["tehran", "mashhad", "karaj", "shiraz", "isfahan", "ahvaz", "tabriz", "kermanshah", "qom", "rasht"]
categories = []
dataIndexes = set()
links = []
data = {}
enteredCity = 1

try:
    print("Enter The Cities:")
    for i, city in enumerate(cities, start=1):
        print(f"{i}: {convert(city)}")
    enteredCity = int(input())
    driver.get(f"https://divar.ir/s/{cities[enteredCity - 1]}")
    
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "kt-accordion-item__header")))
    
    categoriesTemp = driver.find_elements(By.CLASS_NAME, "kt-accordion-item__header")
    for category in categoriesTemp:
        categories.append(category)
    
    print("Select a Category:")
    for i, c in enumerate(categories, start=1):
        categoryName = convert(c.accessible_name.partition(' ')[2])
        print(f"{i}: {categoryName}")
    chosenCategory = int(input()) - 1
    categories[chosenCategory].click()
    
    datanum = int(input("How many?\n"))
    loaded_indexes = 0
    current_scroll = 0
    while loaded_indexes < datanum:
        try:
            indexes = driver.find_elements(By.CSS_SELECTOR, '[data-index]')
            for index in indexes:
                if index not in dataIndexes:
                    dataIndexes.add(index)
                    loaded_indexes += 1
                    print(f"Loaded indexes: {loaded_indexes}")
                    
                    item_container = index.find_element(By.CLASS_NAME, 'post-list__items-container-e437f')
                    widget_cols = item_container.find_elements(By.CLASS_NAME, 'post-list__widget-col-a3fe3')
                    for widget in widget_cols:
                        link = widget.find_element(By.TAG_NAME, 'a').get_attribute('href')
                        links.append(link)
                    
                    if loaded_indexes >= datanum:
                        break

            try:
                load_more_button = driver.find_element(By.CLASS_NAME, value='post-list__load-more-btn-d46f4')
                if load_more_button:
                    load_more_button.click()
                    WebDriverWait(driver, 10).until(EC.staleness_of(load_more_button))
            except:
                pass

        except Exception as e:
            if 'stale element reference' not in str(e):
                print(f"An error occurred while processing elements: {e}")

        current_scroll += 100
        driver.execute_script(f"window.scrollTo(0, {current_scroll});")
        time.sleep(0.025)
        
except Exception as e:
    print(f"An error occurred: {e}")

finally:
    print("Work finished. Closing...")
    driver.quit()

driver = webdriver.Chrome(options=options)
i = 1
for link in links:
    driver.get(link)
    try:
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'post-actions__get-contact')))
        contact_button = driver.find_element(By.CLASS_NAME, 'post-actions__get-contact')
        if contact_button:
            contact_button.click()
            if i == 1:
                WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'kt-textfield__input')))
                phone_input = driver.find_element(By.CLASS_NAME, 'kt-textfield__input')
                phone_number = input("Enter your phone number: ")
                phone_input.send_keys(phone_number)
                
                WebDriverWait(driver, 10).until(EC.staleness_of(phone_input))
                sms_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'kt-textfield__input')))
                sms_code = input("Enter the sms sent to your phone: ")
                sms_input.send_keys(sms_code)
                
                WebDriverWait(driver, 10).until(EC.staleness_of(sms_input))
            
            time.sleep(1)

            title = driver.find_element(By.CLASS_NAME, 'kt-page-title__title').text
            time_element = driver.find_element(By.CLASS_NAME, 'kt-page-title__subtitle').text
            phone = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'kt-unexpandable-row__action'))).text
            data[link] = {
                "title": title,
                "time": time_element,
                "phone": phone
            }

            print(f"data {i} processed successfully.")
            i += 1
        
    except Exception as e:
        print(f"An error occurred while processing link {link}: {e}")
        continue

with open(f"{cities[enteredCity - 1] + str(len(links))}.txt", "w", encoding='utf-8') as file:
    for link, info in data.items():
        file.write(f"Link: {link}\n")
        for key, value in info.items():
            file.write(f"{key.capitalize()}: {value}\n")
        file.write("\n")

print("Finished Scraping The Data. Closing...")
driver.quit()