from selenium import webdriver
import chromedriver_autoinstaller
import sys
import time
import os


def get_bb_slot(url):
    # auto-install chromedriver 
    chromedriver_autoinstaller.install() 
    
    driver = webdriver.Chrome()
    driver.get(url)
    print("Please login and then wait for a while.")
    time.sleep(120)


    while 1:
        driver.get(url)     
        time.sleep(2)
        print("Trying to find a slot!")
        try:
            driver.find_element_by_xpath("//button[@data-automation-id = 'reserveBtn']").click()

            time.sleep(5)  #driver take a few sec to update the new url
            driver.find_element_by_xpath('//button[text()="Delivery"]').click()
            time.sleep(2)
            availability = driver.find_elements_by_xpath("//div[text()='Not Available']");
            if len(availability) < 7 : # 7 days in a week
                print("Found the slots!")
                for i in range(5):
                     notify("Slots Available!", "Please go and choose the slots!")
                     time.sleep(20)
        except Exception  as e:
            print("If this message pops up multiple times, please find the error and create a PR!")
            print (e)
            pass
        print("No Slots found. Will retry again.")
        time.sleep(300)

def notify(title, text):
    if os.name == 'posix':
        os.system("""
              osascript -e 'display notification "{}" with title "{}"'
              """.format(text, title))
        os.system('say "Slots for delivery available!"')
    elif os.name == 'Linux':
        os.system('spd-say "Slots for delivery available!"')

def main():
    get_bb_slot("https://www.walmart.com/account/login?tid=0&vid=2&returnUrl=%2F")

if __name__ == '__main__':
    main()
