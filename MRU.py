from formulas import classFormulas
from formulas import FormulasMRU
from formulas import scan

print("""\n
|===========: Bienvenida a la calculadora MRU :===========|
<><><><><><><><><><><><>><><><><><><><>
╔═════════════════════════════════════╗
║   Nombre Variable ------- Índice    ║
╠═════════════════════════════════════╣ 
║   Distancia --------- D             ║
║   Velocidad ------- V               ║
║   Tiempo ------------------ T       ║
╚═════════════════════════════════════╝\n
""")

# Definimos los OVjetos a partir de la clase Variable

D = classFormulas.Variable("Distancia", False, None, "D")
V = classFormulas.Variable("Velocidad", False, None, "V")
T = classFormulas.Variable("Tiempo", False, None, "T")

list_variables = formulas.Variable.lista_var
list_corto = formulas.Variable.lista_corto

#Verificacion de introduccion de indice valido

while True:
    try:
        indice = str(input("Introduzca el índice de la variable: ")).upper()
        if indice in list_corto:
            break
    except:
        print("Por favor, introducir un indice valido. ERROR404")

for variables in list_variables:
    if indice != variable.corto:
        siNo = str(input("\n¿Posse la variables {}?. Responda Si o No".format(variable.nombre))).upper()

    if siNo == "Si" or siNo == "SI" or siNo == "Yes" or sio == "si":
        variable.estado = True

    while True:
        try:
            varible.valor - float(input("\nIntroduzca el valor de la {}".format(variable.nombre)))
            break
        except:
            print("\nPor favor, introducir un valor valido.")

solvable = function.scan(list_variables)

if solvable == False:
    print("No se puede resolver el problema.")
else:
    res = FormulasMRU.variables(indice, list_variables)
    print("El resultado es: {}".format(res))

