#Código usado para fazer os estudos de caso

def Ford_Fulkerson(grafo: str, d: bool, s, t, disco):
        with open(f'{grafo}.txt', 'r') as arquivo:  #mudar o número do grafo de acordo com o teste 
            texto = [vertice for vertice in arquivo.read().split()] #Cria uma lista com o conteúdo presente no arquivo de teste
            vertices = int(texto[0]) #Pega o primeiro elemento da lista acima, que correnspode ao número de vértices do grafo
            arestas = [] #Lista vazia que vai conter todos os pares de arestas do grafo
            for i in range(len(texto[1:])//3):
                arestas += [[int(texto[3*i+1])]+[int(texto[3*i+2])]+ [float(texto[3*i+3])]] 
        
        g = Graph_l(vertices, arestas, d)
        g.FF(s, t, grafo, disco)

