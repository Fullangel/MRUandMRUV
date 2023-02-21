# Función que se encarga de escanear y ver si se puede resolver
def scan(list_variables):
    """
    La función 'scan' se encarga de aceptar la lista de las variables y verifica si este sistema en específico
    es resolvible. Funciona contando el número de variables que se tienen. Si se tienen 3 variables o más, es 
    posible resolverlo.
    """
    account_variable = 0 # Asignamos el contador inical a 0
    
    for variable in list_variables:
        if variable.estado == True:
            account_variable += 1 

    # Salida
    if account_variable >= 3:
        return True
    else:
        return False