while True:
    print("\n\")t\t\t -- Calculadora Simples --")

    print ("1. Soma")
    print ("2.Subtração")
    print ("3.Multiplicação")
    print ("4.Divisão")
    print ("5.Sair")

    op = int(input("\nOpção: "))
    
    if op == 1:
        print("\n\")t\t\t -- Soma -- \n")

        n1 = float(input("Informe N1: "))
        n2 = float(input("Informe N2: "))

        total = n1+n2

        print("\n\t\t{} + {} = {}\n".format(n1, n2, total))

    elif op == 2:
        print("\n\")t\t\t -- Subtração -- \n")
        
        n1 = float(input("Informe N1: "))
        n2 = float(input("Informe N2: "))
        
        total = n1-n2
        
        print("\n\t\t{} - {} = {}\n".format(n1, n2, total))

    elif op == 3:
        print("\n\")t\t\t -- Multiplicação -- \n")
        
        n1 = float(input("Informe N1: "))
        n2 = float(input("Informe N2: "))
        
        total = n1*n2
        
        print("\n\t\t{} * {} = {}\n".format(n1, n2, total))

    elif op == 4:
        print("\n\")t\t\t -- Divisão -- \n")
        
        n1 = float(input("Informe N1: "))
        n2 = float(input("Informe N2: "))
        
        total = n1/n2
        
        print("\n\t\t{} / {} = {}\n".format(n1, n2, total))

    elif op == 5:
        print("\n\")t\t\t -- Saindo -- \n")
        break
    else:
        print("\n\nOpção {} incoreta!\n\n".format(op))
        
