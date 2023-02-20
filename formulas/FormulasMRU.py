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