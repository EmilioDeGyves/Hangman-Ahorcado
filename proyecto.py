import random as rand

palabras =[["héroe","dragón","caos","belleza","tono","cultura"],["mitología","saponificar","ideología","hegemonía","armonía","estoicismo"],["jurisprudencia","estructuralismo","posmodernismo","fenomenología","paleoantropología","antropogénesis"]]
estado= {'oportunidades' : 5, 'errores' : 0, 'intentos' : 0}

def inicio(palabras,Dificultad):
    progreso = []
    definiciones = [["Persona ilustre y famosa por sus hazañas o virtudes.","Animal fabuloso con forma de reptil muy corpulento, con garras y alas, y de extraña fiereza y voracidad.","Estado amorfo e indefinido que se supone anterior a la ordenación del cosmos.","Persona o cosa notable por su hermosura.","Cualidad de los sonidos, dependiente de su frecuencia, que permite ordenarlos de graves a agudos.","Conjunto de conocimientos que permite a alguien desarrollar su juicio crítico."],["Conjunto de mitos de un pueblo o de una cultura, especialmente de la griega y romana.","Transformar en jabón una sustancia grasa combinándola con sosa.","Conjunto de ideas fundamentales que caracteriza el pensamiento de una persona, colectividad o época, de un movimiento cultural, religioso o político, etc.","Supremacía que un Estado ejerce sobre otros.","Proporción y correspondencia de unas cosas con otras en el conjunto que componen.","Fortaleza o dominio sobre la propia sensibilidad."],["Ciencia del derecho.","Teoría y método científicos que consideran un conjunto de datos como una estructura o sistema de interrelaciones.","Movimiento poético nacido entre el modernismo y las primeras vanguardias, que rechaza el refinamiento modernista y se propone plasmar de forma subjetiva el entorno inmediato y la vida cotidiana.","Método desarrollado por Edmund Husserl que, partiendo de la descripción de las entidades y cosas presentes a la intuición intelectual, logra captar la esencia pura de dichas entidades, trascendente a la misma consciencia.","Rama de la antropología que estudia la evolución de la especie humana a partir de sus restos fósiles.","Estudio del origen y evolución del hombre."]]
    num= 0
    palabra = rand.choice(palabras[Dificultad])
    print("\nRecuerda poner Acentos a las palabras que lo requieran")
    for z in range(6):
        c=palabras[Dificultad][z]
        if palabra == c:
            num= z
          
    definicion = definiciones[Dificultad][num]
    print ("\nPista\n",definicion)
    print("Palabra de tamaño: ", len(palabra), '\n')
    for i in range(len(palabra)):
        progreso.append('_')
        print(progreso[i], end=' ')
        
    jugar(progreso, palabra)
    
def jugar(progreso, palabra):
    letra = input('\n\nIngrese letra o palabra: ')
    if len(letra) == 1:
        if letra in palabra:
            estado['intentos'] += 1
            for i, l in enumerate(palabra): 
                if l.lower() == letra.lower(): 
                    progreso[i] = l 
            for i in progreso:
                print(i, end=' ')
            if '_' not in progreso:
                print('\n\tPALABRA CORRECTA!\n' )
                print('Lo resolviste en %i intento(s).'%estado['intentos'])
                res = input('¿Jugar de nuevo?(S/N): ')
                if res.upper() == 'S':
                    estado['oportunidades'] = 5
                    estado['errores'] = 0
                    estado['intentos'] = 0
                    main()
                else:
                    print("Adios")
                    exit()
            else:
                 jugar(progreso, palabra)
        elif estado['oportunidades'] == 0:
            print('ERROR!')
            print('\n\t\tGAME OVER!!\n',"\n",palabra,"\n")
            res = input('¿Deseas jugar de nuevo?(S/N): ') 
            if res.upper() == 'S':
                estado['oportunidades'] = 5
                estado['errores'] = 0
                main()
        else:
            estado['oportunidades'] -= 1 
            estado['errores'] += 1 
            estado['intentos'] += 1 
            print('ERROR! Vuelve a intentarlo!')
            jugar(progreso, palabra)

    elif letra == palabra:
        estado['intentos'] += 1
        print('\n\tPALABRA CORRECTA!\n')
            
        print('Lo resolviste en %i intento(s).'%estado['intentos'])
        res = input('¿Jugar de nuevo?(S/N): ')
        if res.upper() == 'S':
            estado['oportunidades'] = 5
            estado['errores'] = 0
            estado['intentos'] = 0
            main()
        else:
                 print("Adios")
                 exit()

    else: 
        estado['oportunidades'] -= 1 
        estado['errores'] += 1 
        estado['intentos'] += 1 
        print('ERROR! Vuelve a intentarlo!')
        jugar(progreso, palabra)
            
def main():
    print("\t\t\tAhorcado Tec\n")
    res = input('¿Deseas jugar?(S/N): ')
    if res.upper() == 'S':
        Dificultad=input("\nSeleccione dificultad: (F/M/D)")
        Dificultad= Dificultad.upper()
       
        if Dificultad =="F":
            Dificultad=0
            inicio(palabras, Dificultad)
        elif Dificultad=="M":
            Dificultad= 1
            inicio(palabras, Dificultad)
        elif Dificultad=="D":
            Dificultad= 2
            inicio(palabras, Dificultad)
        else:
            print("\nError")
            main()
    elif res.upper() == 'N':
        print("Adios")
        exit()
    else:
        main()
        

main()