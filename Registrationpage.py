# **************************     selenium automation testing     ****************
# Problem Statement: Automate Registration Page Using Selenium and python
import re
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from validate_email import validate_email
driver = webdriver.Chrome()


driver.get("https://www.lambdatest.com/webpage")
time.sleep(2)
driver.maximize_window()
time.sleep(2)
signIn = driver.find_element(By.XPATH,'//*[@id="header"]/nav/div/div/div[2]/div/div/div[2]/a[2]')
if signIn.is_displayed() and signIn.is_enabled():
    print("Is Sign In feild is displayed?  ",signIn.is_displayed())
    print("Is Sign In feild is enabled?    ", signIn.is_enabled())
    signIn.click()
else:
    print("sign in is not displayed and not enabled")

# Name feild
input_Name=driver.find_element(By.ID,'name')
if input_Name.is_displayed() and input_Name.is_enabled():
    print("Name Feild is displayed and enabled")
    input_Name.send_keys("Sakshi Dikole ")
    name_Feild = 'Sakshi Dikole'
    if re.search('^[a-zA-Z0-9_\s]*$', name_Feild):
        print('Name field -is valid')
else:
    print('Name field is not valid')

# Email feild
inputEmail = driver.find_element(By.CSS_SELECTOR,'#email')
if inputEmail.is_displayed() and inputEmail.is_enabled():
    print("Email feild is displayed and enabled")
    inputEmail.send_keys("Sakshidikole101@gmail.com")
    emaiL = 'Sakshidikole101@gmail.com'
    if validate_email(emaiL):
        print("Email - is Valid")
    else:
        print("Email - is not Valid")

# password feild
inputPass = driver.find_element(By.CSS_SELECTOR, '#userpassword')
if inputPass.is_displayed() and inputPass.is_enabled():
    print("Password feild is Displayed and enabled")
    inputPass.send_keys('DSAS@101')
    password_value = 'DSAS@101'
    if re.match(r"^(?=.*[A-Za-z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!%*#?&]{8,}$", password_value):
        print("Password field - is valid!")
    else:
        print("Password field -is invalid!")

# Phone no feild
inputPhoneno = driver.find_element(By.CSS_SELECTOR, '#phone')
if inputPhoneno.is_displayed() and inputPhoneno.is_enabled():
    print("Phone no feild is displayed and enabled")
    inputPhoneno.send_keys('8525038996')
    phone_No = '8525038996'
    if re.search('^[0-9]{10}$',phone_No):
        print("Phone No - is Valid!")
    else:
        print("Phone No - not is Valid!")

# Free Sign up Button
freesignUp = driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div[2]/form/div[6]/button')
if freesignUp.is_displayed() and freesignUp.is_enabled():
    print("Sign up Button is Displayed and Enabed")
    driver.find_element(By.CSS_SELECTOR,'#app > div.bg-lambda-90.relative > div.flex.ml-auto.relative > div.lg\:w-1\/2.flex.bg-white.w-full.right_part.min-h-screen.lg\:ml-auto.mx-auto.xxld\:pt-\[120px\].xxl\:pt-\[120px\].pt-\[120px\] > div > div.login_part > div.clearfix.registeraArea.signUpWithEmail > form > div:nth-child(6) > button').click()
    driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div[2]/div[2]/p/a').click()
    time.sleep(2)
    driver.find_element(By.XPATH, '//*[@id="email"]').send_keys("Sakshidikole101@gmail.com")
    driver.find_element(By.XPATH, '//*[@id="password"]').send_keys('DSAS@101')
    time.sleep(2)
    driver.find_element(By.ID, 'login-button').click()
    time.sleep(1)
else:
    print("Sign up button is not displayed or enabled ")

time.sleep(18)
driver.close()