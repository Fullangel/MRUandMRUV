from formulas import classFormulas

# Creamos los diccionarios de formulas

vi_formu = {
    'VI': 'vf - a*t',
    'VI': 'vf - 2*a*d',
}
vf_formu = {
    'VF': 'vi + a*t',
    'VF': 'vi + 2*a*d',
}
a_formu = {
    'A': '(vf - vi)/t',
    'A': '(vf - vi)/2*d',
}
t_formu = {
    'T': '2*d/(vf + vi)',
    'T': '(vf - vi)/a',
}
d_formu = {
    'D': '1/2*(vf + vi)*t',
    'D': 'vi*t + 1/2*a*t^2',
    'D': 'vf*t - 1/2*a*t^2',
    'D': '(vi + vf) / 2*t',
}

# Objetos que almacenan las formulas

obj_VI = classFormulas.Formulas('VI', vi_formu)
obj_VF = classFormulas.Formulas('VF', vf_formu)
obj_A = classFormulas.Formulas('A', a_formu)
obj_T = classFormulas.Formulas('T', t_formu)
obj_D = classFormulas.Formulas('D', d_formu)

#Funcion para tener acceso a las formulas
def variables(indice, list_variables):
    vi = list_variables[0].valor
    vf = list_variables[1].valor
    a = list_variables[2].valor
    t = list_variables[3].valor
    d = list_variables[4].valor

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
            if indice == 'VI':
                res = eval(obj_vi.call(variable.corto))
            elif indice == 'VF':
                res = eval(obj_vf.call(variable.corto))
            elif indice == 'A':
                res = eval(obj_a.call(variable.corto))
            elif indice == 'T':
                res = eval(obj_t.call(variable.corto))
            elif indice == 'D':
                res = eval(obj_d.call(variable.corto))
    return res
