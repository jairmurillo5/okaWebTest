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


  Scenario: Validar privilegios de un usuario Admin
    Given soy un usuario
    When ingrese mis credenciales
    Then accedere al main de la plataforma
    And podré filtrar a user que tengan el rol de Admin



