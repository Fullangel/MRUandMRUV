class Variable():
    lista_var = [] # Lista de variables
    lista_corto = [] #lista de CORTO

    """
    Esta clase define las variables a partir de su nombre, su estado (Boolean),
    su valor numérico y su nombre corto. Tiene dos atributos (la clase) que son
    dos listas, una contiene los nombres cortos y otra las variables en si.
    """
    def __init__(self, nombre_variable, estado, valor, nombre_corto):
        self.nombre = nombre_variable
        self.estado = estado
        self.valor = valor
        self.corto = nombre_corto

        Variable.lista_var.append(self) #Creación automática de lista de variables 
        Variable.lista_corto.append(self.corto) # Creación de autom. de lista de nombres cortos


class Formulas():
    """
    Esto almacena las diferentes fórmulas. Básicamente, admite el nombre de la variable que resuelven,
    y con que variables faltantes funcionan.
    """    
    def __init__(self, name_variable, list_formulas):
        # Hacemos que los atributos de las instancias de Formulas sean las fórmulas
        self.nombre = name_variable
        self.VF = list_formulas["VF"]
        self.VI = list_formulas["VI"]
        self.A = list_formulas["A"]
        self.T = list_formulas["T"]
        self.D = list_formulas["D"]
        self.V = list_formulas["V"]
    
    def call(self, lef):
        if lef == "VF":
            return self.VF
        elif lef == "VI":
            return self.VI
        elif lef == "A":
            return self.A
        elif lef == "T":
            return self.T
        elif lef == "X":
            return self.X
        elif lef == "D":
            return self.D
        elif lef == "V":
            return self.V


class Run():
    """
    Esto se encarga de hacer la resolución fácil. 
    Le pasamos las fórmulas.
    Le pasamos el objeto de la variable.
    """ 
    def __init__(self, variable, formula):
        pass
        