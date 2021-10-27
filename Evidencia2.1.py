from collections import namedtuple
import csv
import os
cantidades = [] #Esta lista vacia, guardara las cantidades totales de los articulos para despues sumarlas 
v = [] #Esta lista vacia, guardara los datos de la namedtuple para despues hacerles busqueda especifica
diccionario = {} #Este diccionario guardara el folio como clave y dentro de el vendra una variable que tenga guardada la tupla nominada
ventas = namedtuple('ventas', 'folio,desc_articulo, cantidad, precio,fecha')
while True:
    print('')
    print(' ** MENU ** ')
    print('Registrar una venta[1]')
    print('Consultar una venta[2]')
    print('Reporte de ventas para una fecha especifica[3]')
    print('Salir[4]')
    op = input('Introduzca la opcion: ')
    if op == '1':
        folio = int(input('Introduzca el folio: '))
        fecha = input('Introduzca fecha de la venta d/m/y: ')
        if folio in diccionario.keys(): #si el 'folio' que ingreso ya esta registrado que intente con otro
            print('Este folio ya esta registrado, intento con otro: ')
        else:
            while True: #si no, ejecutar este ciclo
                desc_articulo = input('Describa el articulo: ')
                cantidad = int(input('Cantidad de piezas vendidas: '))
                precio = float(input('Precio de venta $: '))
                datos = ventas(folio,desc_articulo,cantidad,precio,fecha)
                #Esta variable guradara los datos de la tupla nominada 
                diccionario[folio,fecha] = datos
                total = precio * cantidad
                cantidades.append(total)
                v.append(datos)
                agregar = input('Desea seguir agregando [S/N]: ')
                if agregar == 'N': #si 'agregar' es igual a 'N', imprimir la suma total de los articulos 
                    iva = sum(cantidades) * .16
                    total_iva = sum(cantidades) + iva
                    print(f'El monto sin iva es: ${sum(cantidades)}')
                    print(f'Desglose de iva(16%): ${iva} ')
                    print(f'Total a pagar con iva: ${total_iva}')
                    break
                with open('ventas.csv','w',newline='') as archivo:
                    grabador = csv.writer(archivo)
                    grabador.writerow(('folio','desc_articulo','cantidad','precio'))
                    grabador.writerows([(folio, datos.desc_articulo, datos.cantidad, datos.precio) for folio, datos in diccionario.items()])
                    print(f'\ngrabado exitoso en {os.getcwd()}')
    elif op == '2':
        busqueda = int(input('Introduzca el folio a buscar: '))
        for elemento in v: #Por cada elemento de la lista 'v' 
            if busqueda == elemento.folio: #si 'busqueda' es igual al folio que esta en la lista, entonces imprime los siguiente: 
                print('')
                print(f'Descripcion del articulo(s): {elemento.desc_articulo} ')
                print(f'Cantidad de piezas vendidass: {elemento.cantidad} ')
                print(f'Precio de cada una: {elemento.precio} ')
                print('')
        print(f'Desglose de iva(16%): ${iva}')
        print(f'Gran total ${total_iva}')
    elif op == '3':
        busq_fecha = input('Introduzca la fecha de la venta a buscar: ')
        for elemento in v: #Por cada elemento de la lista 'v'
            if busq_fecha == elemento.fecha: #si 'busq_fecha' es igual a la fecha que esta en la lista, entonces imprime lo siguiente
                print('')
                print(f'Descripcion del articulo(s): {elemento.desc_articulo}' )
        print(f'Desglose de iva(16%): ${iva}')
        print(f'Gran total ${total_iva}')
    elif op == '4':
        break
