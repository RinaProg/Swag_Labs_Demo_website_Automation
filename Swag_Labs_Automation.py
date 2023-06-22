from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common import keys
from selenium.webdriver.support.wait import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as ec
# from selenium.webdriver.common.action_chains import ActionChains as ac


def Automate_Function():

#--------------Intilized steps---------------
    driver=webdriver.Chrome()
    driver.get('https://www.saucedemo.com/inventory.html')
    driver.maximize_window()


    print('\n')
    print('|====================| AUTOMATION ON SWAG LABS PAGE |====================|')
    print('\n')
    
    #---------------User Login Page check-----------------
    try:
        time.sleep(2)
        wait(driver,10).until(ec.visibility_of_element_located((By.NAME,"user-name")))
        wait(driver,10).until(ec.visibility_of_element_located((By.NAME,"password")))
        print('Login page open successfully...\n')
    except:
        print('!!! Login page not open \n')


    #----------------check Error Button Clickable or not ---------------
    try:
        
        wait(driver,10).until(ec.visibility_of_element_located((By.XPATH,"//button[contains(@class,'error-button')]")))
        print('error button clickable \n ')
    except:
        print('!!! error button not clickable \n ')


    #-----------------epic-sadface error check-------------------
    try:
        time.sleep(2)
        driver.find_element(By.XPATH,"//button[contains(@class,'error-button')]").click()
        print('epic-sadface error remove \n')

    except:
        print('!!! does not remove epic-sadface error \n')


    #-------------------UserName & Password values are Putted on the Login page successfully------------
    try:
        time.sleep(4)
        driver.find_element(By.NAME,'user-name').send_keys('standard_user')
        driver.find_element(By.NAME,'password').send_keys('secret_sauce')
        print('UserName & Password putted successfully  \n')
        time.sleep(6)
    except:
        print('!!! UserName & Password putted unsuccessfully  \n')


    #------------------Login Button clickable or not check----------------------
    try:
        wait(driver,10).until(ec.visibility_of_element_located((By.ID,"login-button")))
        print('login button clickable \n')
    except:
        print('!!! login button not clickable \n')


    #-------------------Login successfull or not check--------------------------
    try:
        driver.find_element(By.ID,"login-button").click()
        print('login successfully \n')
    except:
        print('!!! login unsucessfull \n')


    #-------------------check visibility of dop down list whether it is present or not-------------------------
    try:
        wait(driver,10).until(ec.visibility_of_element_located((By.CSS_SELECTOR,".product_sort_container")))
        print('drop down list clickable  \n')
    except:
        print('!!! clickable function not working for drop down list \n')


    #-------------------check whether select option clickable or not -------------------------
    try:
        
        driver.find_element(By.CSS_SELECTOR,".product_sort_container").click()
        print('click on the selected option \n')

    except:
        print('!!! selected option not clickable \n')


    try:
        
        driver.find_element(By.CSS_SELECTOR,"[value=lohi]").click()
        print('click on Price(low to high) option \n')
        
    except:
        print('!!! drop down list option not working \n')



    #--------------------check whether Add to cart button clickable or not-----------------
    try:
        wait(driver,10).until(ec.element_to_be_clickable((By.XPATH,"//button[contains(text(), 'Add to cart')]"))) 
        print('Add to cart button clickable \n')
        time.sleep(8)
    
    except:
        print('!!! Add to cart button not clickable \n')



    #----------------check whether selected products are added on the cart or not -------------------------------
    try:
        time.sleep(6)
        for t in range(0,3):
            driver.find_element(By.XPATH,f"(//button[contains(text(), 'Add to cart')])[{t+1}]").click()
            price=(wait(driver,10).until(ec.element_to_be_clickable((By.XPATH,f"(//div[contains(@class,'inventory_item_price')])[{t+1}]"))).text)
            # print(price[1:])
            print(f'Product {t+1} add to cart successfully & price is ->{price}')   
        time.sleep(8)
        print('\n')

    except Exception as e:
        print(e)
        print('!!! unable to add products \n')



    #-------------------check whether shopping cart button clickable or not ------------------
    try:
        wait(driver,10).until(ec.element_to_be_clickable((By.XPATH,"//div[contains(@class,'shopping_cart_container')]"))) 
        print('shopping cart button clickable \n')
    except:
        print('!!! shopping cart button unclickable \n')


    try:
        time.sleep(6)
        driver.find_element(By.XPATH,"//div[contains(@class,'shopping_cart_container')]").click()
        print('click on shopping cart button & move next page \n')
        
    except:
        print('!!! unable to click on shopping cart button  \n')



    #---------------calculate total no. of products-------------------
    try:
        num=driver.find_elements(By.CSS_SELECTOR,".cart_quantity")
        a=len(num)
        print(f'Total number of products pesent in cart -> {a} \n')
        
    except:
        print('!!! not working \n')


    #-------------------check whether check-out button clickable or not -----------
    try:
        wait(driver,10).until(ec.visibility_of_element_located((By.ID,"checkout")))
        print('check-out button clickable \n')
    except:
        print('!!! check-out button unclickable \n')

    try:
        time.sleep(6)
        driver.find_element(By.ID,"checkout").click()
        print('click on check-out button & move next page \n')
        
    except:
        print('!!! unable to click on check-out button \n')


    #-------------------check visibility of check-out page whether it is present or not-------------------------
    try:
        wait(driver,10).until(ec.visibility_of_element_located((By.NAME,"firstName")))
        wait(driver,10).until(ec.visibility_of_element_located((By.NAME,"lastName")))
        wait(driver,10).until(ec.visibility_of_element_located((By.NAME,"postalCode")))
        print('check-out page open successfully \n')

    except:
        print('!!! check-out page not open \n')


    #-------------------firstName,lastName & postalCode values are Putted on the check-out page successfully------------
    try:
        time.sleep(6)
        driver.find_element(By.NAME,'firstName').send_keys('puja')
        driver.find_element(By.NAME,'lastName').send_keys('pal')
        driver.find_element(By.NAME,'postalCode').send_keys('700091')
        print('successfully putted all data \n')
        time.sleep(8)
    except:
        print('!!! unsuccessfully putted all data \n')


    #---------------------check the visibility of continue button--------------------
    try:
        wait(driver,10).until(ec.visibility_of_element_located((By.NAME,"continue")))
        print('continue button clickable \n')
    except:
        print('!!! continue button unclickable \n')


    #---------------------check whether the continue button clickable or not--------------------
    try:
        driver.find_element(By.NAME,'continue').click()
        print('click on continue button & move next page \n')
        time.sleep(6) 
    except:
        print('!!! unable to click on continue button \n')


    #----------------visibility checking of total amount---------------------------
    try:
        Total_amt=(wait(driver,10).until(ec.visibility_of_element_located((By.XPATH,'//div[contains(@class,"summary_info_label summary_total_label")]'))).text)
        print(f'Total Amount is -> {Total_amt[6:]} \n')
    except:
        print('!!! unable to print total amount \n')


    #---------------------check whether the finish button clickable or not----------------
    try:
        wait(driver,10).until(ec.visibility_of_element_located((By.NAME,"finish")))
        print('finish button clickable \n')
    except:
        print('!!! finish button unclickable \n')


    try:
        driver.find_element(By.NAME,'finish').click()
        print('click on finish button \n')
        time.sleep(6) 
    except:
        print('!!! unable to click on finish button \n')


    #---------------------check whether the Back-Home button clickable or not----------------------
    try:
        wait(driver,10).until(ec.visibility_of_element_located((By.NAME,"back-to-products")))
        print('Back-Home button clickable \n')
    except:
        print('!!! Back-Home button unclickable \n')


    try:
        driver.find_element(By.NAME,'back-to-products').click()
        print('click on Back-Home button & move to Swag Labs page \n')
        time.sleep(2) 
    except:
        print('!!! unable to click on Back-Home button \n')


    #---------------------check whether the open-menu sandwich button clickable or not----------------------
    try:
        wait(driver,10).until(ec.visibility_of_element_located((By.ID,"react-burger-menu-btn")))
        print('open-menu sandwich button clickable \n')
    except:
        print('!!! open-menu sandwich  button unclickable \n')


    try:
        driver.find_element(By.ID,'react-burger-menu-btn').click()
        print('click on open-menu sandwich  button \n')
        time.sleep(6) 
    except:
        print('!!! unable to click on open-menu sandwich button \n')


    #---------------------check whether the Logout button clickable or not----------------------
    try:
        wait(driver,10).until(ec.visibility_of_element_located((By.ID,"logout_sidebar_link")))
        print('Logout button clickable \n')
    except:
        print('!!! Logout  button unclickable  \n')


    try:
        driver.find_element(By.ID,'logout_sidebar_link').click()
        print('click on Logout button \n')
        time.sleep(2) 
    except:
        print('!!! unable to click on Logout button \n')


if __name__ == '__main__':

    time.sleep(20)   
    Automate_Function()
     