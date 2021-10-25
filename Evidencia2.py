from collections import namedtuple
import csv
import os
cantidades = []
v = []
diccionario = {}
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
        if folio in diccionario.keys():
            print('Este folio ya esta registrado, intento con otro: ')
        else:
            while True:
                desc_articulo = input('Describa el articulo: ')
                cantidad = int(input('Cantidad de piezas vendidas: '))
                precio = float(input('Precio de venta $: '))
                datos = ventas(folio,desc_articulo,cantidad,precio,fecha)
                diccionario[folio,fecha] = datos
                total = precio * cantidad
                cantidades.append(total)
                v.append(datos)
                agregar = input('Desea seguir agregando [S/N]: ')
                if agregar == 'N':
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
        for elemento in v:
            if busqueda == elemento.folio:
                print('')
                print(f'Descripcion del articulo(s): {elemento.desc_articulo} ')
                print(f'Cantidad de piezas vendidass: {elemento.cantidad} ')
                print(f'Precio de cada una: {elemento.precio} ')
                print('')
        print(f'Desglose de iva(16%): ${iva}')
        print(f'Gran total ${total_iva}')
    elif op == '3':
        busq_fecha = input('Introduzca la fecha de la venta a buscar: ')
        for elemento in v:
            if busq_fecha == elemento.fecha:
                print('')
                print(f'Descripcion del articulo(s): {elemento.desc_articulo}' )
        print(f'Desglose de iva(16%): ${iva}')
        print(f'Gran total ${total_iva}')
    elif op == '4':
        break
