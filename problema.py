


def llenar_matriz(matriz,tam):
    cont = 1
    while(cont <= tam**2):
        for i in range(tam):
            matriz[i] = [None]*tam
    
        for i in range(tam):
            for j in range(tam):
                matriz[i][j] = str(cont)
                cont += 1


def caracol(matriz,tam):
    caracol = ' '
    for i in range(tam+1):
        for idx,fila in enumerate(matriz):
            if idx == 0:
                caracol += ' '.join(fila)+' '
                del(matriz[0])
       
        if(i == tam):
            return caracol
        
        copia = []  
        k = 1
        while(k < (len(matriz[0])+1)):
            pos = len(fila)- k
            columna = []
            for fila in matriz:
                columna.append(fila[pos])
            copia.append(columna)
            k+=1
                
        matriz = copia
    return caracol


if __name__ == '__main__':
    tam = int(input('Tamanio matriz: '))
    matriz = [None]*tam
    llenar_matriz(matriz,tam)
    print(caracol(matriz,tam))
