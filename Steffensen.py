from sympy import *
from tabulate import tabulate

a = 0
b = 0
error = 0

x = Symbol("x")
f=""
fx = str(f)
f = lambda x: eval(fx)

# Metodo de Steffensen
def Steffensen(a, b, error):
    tabla = []
    ep = 0
    i=1
    #Calcular x0
    x0 = (a+b)/2
    xn=x0

    while (ep >= error or ep == 0):
        #p1 = f(x_n)
        p1 = f(xn)

        #p2 = f(x_n)
        p2 = f(xn+p1)
        try:
            #p = x_n+1 = xn - (f(x)^2/(f(xn + f(xn))-f(xn))
            p = xn - (pow(p1,2)/(p2 - p1))  
        except ZeroDivisionError:
            break
        ep = abs(p-xn)
        tabla.append([i, xn, p1, p2, p, ep])
        xn = p
        i+=1    
    return(tabla)


# Menú
continuar = True
while continuar:
    try:
        print("""

        Proyecto 3 - Métodos de Steffensen
                [1]Presentación
                [2]Método de Steffensen
                """)
        opt = int(input("Seleccione una opción: "))

        if(opt < 1 or opt > 2):
            print("opcion equivocada, favor validar")
        else:

            if opt>1:
                fx = input("Ingrese la funcion: ")
                print("Ingrese el intervalo a evaluar:")
                a = float(input("a: "))
                b = float(input("b: "))

                assert a<b
                assert f(a)*f(b)<0

                error = float(input("error: "))
            if opt == 1:
                print("""
                    Desarrollado por:
                        Cortez, Brandool
                        Estribí, Fernando

                    Grupo: 1SF131""")
            elif opt == 2:
                tabla = Steffensen(a, b, error)
                ntabla = len(tabla)

                # Salida del metodo de Steffensen
                header = ['i', 'xn', 'f(xn)', 'f(xn + f(xn))', 'xn+1', 'ep']
                print(tabulate(tabla, headers=header, floatfmt=".4f"))

                print('raiz:  ', "{:.4f}".format(tabla[len(tabla)-1][4]))
                print('error: ', "{:.4f}".format(tabla[ len(tabla)-1][5]))
           
    except ValueError:
        print("Dato ingresado no numérico. Intente de nuevo.")
    except AssertionError:
        print("""Se deben cumplir las siguientes condiciones:
                  a<b 
                  f(a)*f(b)<0
        Intente de nuevo.""")

    answer = None
    while answer not in ("y", "n"):
        answer = input("¿Desea realizar otro procedimiento? [y/n]: ")
        if answer == "y":
            pass
        elif answer == "n":
            continuar = False
        else:
            print("Opcion invalida. Intente de nuevo.")