from formulas import classFormulas

# Creamos los diccionarios de formulas

d_formu = {
    'D': 'v*t',
    'D': 'vi*t + 1/2*a*t^2',
    'D': 'vf*t - 1/2*a*t^2',
    'D': '(vi + vf) / 2*t',
}
v_formu = {
    'V': 'D/T',
    'V': 'D/T - 1/2*a*t',
    'V': 'D/T + 1/2*a*t',
}
t_formu = {
    'T': 'D/V',
    'T': 'D/V - 1/2*a*t',
    'T': 'D/V + 1/2*a*t',
}

# Objetos que almacenan las formulas

obj_d = classFormulas.Formulas('D', d_formu)
obj_v = classFormulas.Formulas('V', v_formu)
obj_t = classFormulas.Formulas('T', t_formu)

#Funcion para tener acceso a las formulas
def variables(indice, list_variables):
    d = list_variables[0].valor
    v = list_variables[1].valor
    t = list_variables[2].valor

    i = 0
    while True:
        try:
            if list_variables[i].corto == indice:
                list_variables.pop(i)

            i += 1
        except:
                break

#variables faltantes
    for variable in list_variables:
        if variable.estado == False:
            if indice == 'D':
                res = eval(obj_d.call(variable.corto))
            elif indice == 'V':
                res = eval(obj_v.call(variable.corto))
            elif indice == 'T':
                res = eval(obj_t.call(variable.corto))
    return res