'''

Implementează o clasă Login care să moștenească unittest.TestCase

'''

import unittest
from unittest import TestCase
from selenium.webdriver.common.by import By
from selenium import webdriver
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys


'''

Implementează o clasă Login care să moștenească unittest.TestCase
Gasește elementele în partea de sus folosind ce selectors dorești:
- setUp()
- Driver
https://the-internet.herokuapp.com/
Click pe Form Authentication
tearDown()
Quit browser

'''

class Login(TestCase):

    Form_Authentication = (By.LINK_TEXT, "Form Authentication")
    LOG_URL = "https://the-internet.herokuapp.com/login"
    Login_Header_H2 = (By.XPATH, "//*[@id='content']/div/h2")
    Button_Login = (By.XPATH, "//*[@type='submit']")
    Elemental_Selenium = (By.XPATH, "//*[@id='page-footer']/div/div/a")
    Message_Error_Displayed = (By.XPATH, "//*[@class='flash error']")
    Complet_User = (By.ID, "username")
    Complet_Password = (By.ID, "password")
    Flash_Succes = (By.XPATH, "//*[@class='flash success']")
    Button_Logout = (By.XPATH, "//*[@id='content']/div/a")

    def setUp(self):
        self.chrome = webdriver.Chrome()
        self.chrome.implicitly_wait(2)
        self.chrome.get("https://the-internet.herokuapp.com/")          # navigam la url respectiv
        self.chrome.find_element(*self.Form_Authentication).click()     # navigam pe url de login, folosim tuple unpacking

    def tearDown(self):
        self.chrome.quit()


'''

● Test 1
- Verifică dacă noul url e corect

'''


def test_url(self):
    actual_url = self.chrome.current_url
    expected_url = self.LOG_URL
    self.assertEqual(actual_url, expected_url, "Noul Url este incorect")


'''
● Test 2
- Verifică dacă page title e corect
'''


def test_page_title(self):
    actual_title = self.chrome.title
    expected_title = "The Internet"
    self.assertEqual(actual_title, expected_title, "Page Title is incorrect")


''''
Test 3
- Verifică textul de pe elementul xpath=//h2 e corect
'''


def test_element_page_h2(self):
    actual_h2 = self.chrome.find_element(*self.Login_Header_H2).text
    expected_h2 = "Login Page"
    self.assertEqual(actual_h2, expected_h2, "Header H2 is incorrect")

'''
Test 4
- Verifică dacă butonul de login este displayed
'''


def test_button_login_displayed(self):
    actual_button = self.chrome.find_element(*self.Button_Login)
    self.assertTrue(actual_button.is_displayed(), "Button is not displayed")


'''
 Test 5
- Verifică dacă atributul href al linkului ‘Elemental Selenium’ e corect
'''


def test_element_selenium_href(self):
    actual_element_href = self.chrome.find_element(*self.Elemental_Selenium).get_attribute('href')
    expected_element_href = "http://elementalselenium.com/"
    self.assertEqual(actual_element_href, expected_element_href, "Elemental Selenium href attribute is incorrect")


'''
Test 6
- Lasă goale user și pass
- Click login
- Verifică dacă eroarea e displayed
'''


def test_empty_fields_error(self):
    self.chrome.find_element(*self.Button_Login).click()
    error_message = self.chrome.find_element(*self.Message_Error_Displayed)
    self.assertTrue(error_message.is_displayed(), "The error is not displayed")


'''
Test 7
- Completează cu user și pass invalide
- Click login
- Verifică dacă mesajul de pe eroare e corect
- Este și un x pus acolo extra așa că vom folosi soluția de mai jos
expected = 'Your username is invalid!'
self.assertTrue(expected in actual, 'Error message text is
incorrect')
'''

def test_invalid_login(self):
        self.chrome.find_element(*self.Complet_User).send_keys("TnsStefan")
        self.chrome.find_element(*self.Complet_Password).send_keys("313658")
        self.chrome.find_element(*self.Button_Login).click()
        actual_error = self.chrome.find_element(*self.Message_Error_Displayed).text
        expected_error = "Your username is invalid!"
        self.assertTrue(expected_error in actual_error, "Error message text is incorrect")

'''Test 8
- Lasă goale user și pass
- Click login
- Apasă x la eroare
- Verifică dacă eroarea a dispărut
'''


def test_empty_login_delete_error(self):
    self.chrome.maximize_window()
    self.chrome.find_element(*self.Button_Login).click()
    self.chrome.find_element(By.XPATH, "//*[@class='close']").click()
    error_message = self.chrome.find_element(*self.Message_Error_Displayed)
    self.assertTrue(error_message.is_displayed(), "The error message still displayed")

'''
Test 9
- Ia ca o listă toate //label
- Verifică textul ca textul de pe ele să fie cel așteptat (Username și
Password)
- Aici e ok să avem 2 asserturi
'''


def test_text_label_check(self):
    list_check = self.chrome.find_elements(By.TAG_NAME, "label")
    self.assertEqual(list_check[0].text, "Username", "Text on the username incorrect error")
    self.assertEqual(list_check[1].text, "Password", "Text on the password incorrect error")


'''
Test 10
- Completează cu user și pass valide
- Click login
- Verifică ca noul url CONTINE /secure
- Folosește un explicit wait pentru elementul cu clasa ’flash succes’
- Verifică dacă elementul cu clasa=’flash succes’ este displayed
- Verifică dacă mesajul de pe acest element CONȚINE textul ‘secure area!’
'''


def test_login_successfully(self):
    self.chrome.find_element(*self.Complet_User).send_keys("tomsmith")
    self.chrome.find_element(*self.Complet_Password).send_keys("SuperSecretPassword!")
    self.chrome.find_element(*self.Button_Login).click()
    actual_url = self.chrome.current_url
    self.assertTrue("/secure" in actual_url, "Error new url does not contain the word /secure!")
    WebDriverWait(self.chrome, 5).until(EC.presence_of_element_located((By.XPATH, "//*[@class='flash success']")))
    element = self.chrome.find_element(*self.Flash_Succes)
    self.assertTrue(element.is_displayed(), "Element flash succes is not displayed")
    text_element = self.chrome.find_element(*self.Flash_Succes).text

    print(text_element)

    self.assertTrue('secure area!' in text_element, "Message does not contain secure area!")


'''
Test 11
- Completează cu user și pass valide
- Click login
- Click logout
- Verifică dacă ai ajuns pe https://the-internet.herokuapp.com/login
'''


def test_login_logout(self):
    self.chrome.find_element(*self.Complet_User).send_keys("grinn")
    self.chrome.find_element(*self.Complet_Password).send_keys("tnsstefan23")
    self.chrome.find_element(*self.Button_Login).click()
    self.chrome.find_element(*self.Button_Logout).click()
    actual_url = self.chrome.current_url
    expected_url = self.LOG_URL
    self.assertEqual(actual_url, expected_url, "New url is incorrect")


'''
● Test 12 - brute force password hacking
- Completează user tomsmith
- Găsește elementul //h4
- Ia textul de pe el și fă split după spațiu. Consideră fiecare cuvânt ca o
potențială parolă.
- Folosește o structură iterativă prin care să introduci rând pe rând
parolele și să apeși pe login.
- La final testul trebuie să îmi printeze fie
‘Nu am reușit să găsesc parola’
‘Parola secretă este [parola]’
'''


def test_force_hacking(self):
    text_h4 = self.chrome.find_element(By.XPATH, "//*[@id='content']/div/h4").text.split()

    print(text_h4)


    for cuvant in text_h4:

        self.chrome.find_element(*self.Complet_User).send_keys("tomsmith")

        self.chrome.find_element(*self.Complet_Password).send_keys(cuvant)

        self.chrome.find_element(*self.Button_Login).click()
        actual_url = self.chrome.current_url
        expected_url = "https://the-internet.herokuapp.com/secure"

        if actual_url == expected_url:
            print(f"Parola secreta este {cuvant}")
            break
        else:
            print("Nu am reusit sa gasesc parola")


def test_submit_login_additional_1(self):
    self.chrome.find_element(*self.Button_Login).click()
    error_message = self.chrome.find_element(*self.Message_Error_Displayed)
    err_display = error_message.is_displayed()
    self.assertTrue(error_message.is_displayed(), "It is not displayed the error")
    if err_display == True:
        self.chrome.find_element(*self.Complet_User).send_keys("tomsmith")
        self.chrome.find_element(*self.Complet_Password).send_keys("SuperSecretPassword!")
        self.chrome.find_element(*self.Button_Login).click()



