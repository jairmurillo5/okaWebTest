Feature: Prueba WEB
  #El usuario procede a ingresar a la plataforma desde la vista principal
  Scenario: Validar Login Exitoso
    Given soy un usuario
    When ingrese mis credenciales
    Then accedere al main de la plataforma

  #El usuario no procederá a ingresar a la plataforma
  Scenario: Validar Login Fallido
    Given soy un usuario
    When ingrese mis credenciales incorrectamente
    Then no accedere al main de la plataforma

#El usuario utiliza el filtro para visualizar unicamente los usuarios que
#tienen el rol de: [Admin].
  Scenario: Validar privilegios de un usuario Admin
    Given soy un usuario
    When ingrese mis credenciales
    Then accedere al main de la plataforma
    And podré filtrar a user que tengan el rol de Admin


 # El usuario hace click en el boton “Add” para agregar uno nuevo para
 #posterior mense filtrarlo y validar que este fue exitosamente creado
  Scenario: Validar usuario creado correctamente
    Given soy un usuario
    When ingrese mis credenciales
    Then accedere al main de la plataforma
    And podré agregar a un usuario con rol ADMIN
    And podre validar que fue exitosamente creado



