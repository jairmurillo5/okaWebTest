from behave import *
from selenium import webdriver

from Funciones.FuncionesPrueba import Funciones_Globales

@given(u'soy un usuario')
def step_impl(context):
    global driver, g
    context.driver = webdriver.Chrome()
    g = Funciones_Globales(context.driver)
    context.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    context.driver.maximize_window()
    g.Time(3)




@when(u'ingrese mis credenciales')
def step_impl(context):
    global g
    g = Funciones_Globales(context.driver)
    g.Iniciar_Sesion()
    g.Time(3)


@then(u'accedere al main de la plataforma')
def step_impl(context):
    global g
    g = Funciones_Globales(context.driver)
    g.validar_inicioSesion()


@when(u'ingrese mis credenciales incorrectamente')
def step_impl(context):
    g = Funciones_Globales(context.driver)
    g.Login_Fallido()



@then(u'no accedere al main de la plataforma')
def step_impl(context):
    g = Funciones_Globales(context.driver)
    g.validar_login_fallido()


@then(u'podré filtrar a user que tengan el rol de Admin')
def step_impl(context):
    g = Funciones_Globales(context.driver)
    g.filtrar_us_admin()



@then(u'podré agregar a un usuario con rol ADMIN')
def step_impl(context):
    g = Funciones_Globales(context.driver)
    g.add_us()


@then(u'podre validar que fue exitosamente creado')
def step_impl(context):
    print(u'STEP: Then podre validar que fue exitosamente creado')



