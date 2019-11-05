#Alfredo velasquez. P2E7. VERIFICAR FECHA CORRECTA

dia = int(input('Introduzca un día: '))
mes = int(input('Introduzca un mes: '))
año = int(input('Introduzca un año: '))

if (dia > 31):
    print('%d/%d/%d ->Fecha incorrecta' % (dia, mes, año))
elif (mes > 12):
    print('%d/%d/%d ->Fecha incorrecta' % (dia, mes, año))
elif (año < 0):
    print('%d/%d/%d ->Fecha incorrecta' % (dia, mes, año))
    
