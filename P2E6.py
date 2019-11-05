#Alfredo velasquez. P2E6. CALCULAR IVA
import time
pp = float(input('Ingrese el precio del producto: '))
pn = input('Ingrese el nombre del producto: ')

print('Calculando iva')
time.sleep(1)
print('Calculando iva...')
time.sleep(1)
print('Calculando iva......')
time.sleep(1)
print('Calculando iva.........')
time.sleep(1)
c = (pp * 21) / 100
ct = pp+c
print('Tu %s vale %d euros y con el iva se queda en %f euros en total' % (pn, pp, ct)) 
