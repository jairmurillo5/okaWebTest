import time
import logging
from selenium.webdriver.support.select import Select

from select import select

logging.basicConfig(level=logging.INFO)

class Funciones_Globales():
    def __init__(self, driver):
        self.driver = driver


    def Iniciar_Sesion(self):
        driver = self.driver
        us= driver.find_element("name", "username")
        us.send_keys("Admin")
        time.sleep(1)

        passw = driver.find_element("name", "password")
        passw.send_keys("admin123")
        time.sleep(1)

        botonLogin = driver.find_element("xpath", "//button[@type='submit'][contains(.,'Login')]")
        botonLogin.click()
        time.sleep(3)

    def Time(self, tie):
        time.sleep(tie)

    def validar_inicioSesion(self):
        driver = self.driver
        elem_pag_ini=driver.find_element("xpath", "//h6[contains(.,'Dashboard')]")
        if elem_pag_ini.is_displayed():
            logging.info("Inicio de sesión exitoso.")
        else:
            logging.info("Error: El elemento de bienvenida no está visible.")


    def Login_Fallido(self):
        driver = self.driver
        us= driver.find_element("name", "username")
        us.send_keys("Admin")
        time.sleep(1)

        passw = driver.find_element("name", "password")
        passw.send_keys("admin1234")
        time.sleep(1)

        botonLogin = driver.find_element("xpath", "//button[@type='submit'][contains(.,'Login')]")
        botonLogin.click()
        time.sleep(3)

    def validar_login_fallido(self):
        driver = self.driver
        msg_error= driver.find_element("xpath", "//p[contains(.,'Invalid credentials')]")
        if msg_error.is_displayed():
            logging.info("Inicio de sesión fallido.")

    def filtrar_us_admin(self):
        driver = self.driver
        btn_Admin= driver.find_element("xpath", "(//span[contains(.,'Admin')])[1]")
        btn_Admin.click()
        time.sleep(2)

        btn_select= driver.find_element("xpath", "(//div[contains(.,'-- Select --')])[14]")
        btn_select.click()
        time.sleep(2)


        us_role = driver.find_element("xpath", "(//div[contains(.,'Admin')])[19]")
        us_role.click()
        time.sleep(2)

        btn_search = driver.find_element("xpath", "//button[contains(.,'Search')]")
        btn_search.click()
        time.sleep(2)

        #Validar si tiene los privilegios de eliminar y editar
        btn_eliminar=driver.find_element("xpath", "//i[contains(@class,'oxd-icon bi-trash')]")
        btn_editar=driver.find_element("xpath", "//i[contains(@class,'oxd-icon bi-trash')]")
        if btn_editar.is_displayed() and btn_eliminar.is_displayed():
            logging.info("El usuario ADMIN tiene los privilegios de editar y eliminar")



