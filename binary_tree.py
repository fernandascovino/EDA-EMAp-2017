class ABNode: # numa árvore binária, cada nó tem de 0 a 2 filhos
    def __init__(self, raiz=None, le=None, ld=None):
        self.raiz = raiz # o nó tem uma raiz (que contém seu valor)
        self.le = le # ponteiro esquerdo (le), aponta para o nó filho à esquerda
        self.ld = ld # ponteiro direito (ld), aponta para o nó filho à direita

class BTree:
    def __init__(self, raiz=None):
        self.raiz = raiz
        
    def inserir(v,local="le"): # insere um nó v, na subárvore direita ou esquerda
        if self.raiz == None:
            self.raiz = v
        else:
            if local == "le":
                self.raiz.le.inserir(v, local)
            elif local == "ld":
                self.raiz.ld.inserir(v, local)
            else:
                "Local não existe -- Escolha entre esquerda (le) e direita (ld)"
    
    def visita(v): # visita a um nó v
        print(v)
    
    def pre_ordem(self): # percurso em pós-ordem
        if self!=None:
            visita(self.raiz) # visita a raiz
            pre_ordem(self.le)  # percorre a subárvore esquerda em pré-ordem
            pre_ordem(self.ld)  # percorre a subárvore direita em pré-ordem
    
    def pos_ordem(self): # percurso em pré-ordem
        if self!=None:
            pos_ordem(self.le) # percorre a subárvore esquerda em pós-ordem
            pos_ordem(self.ld) # percorre a subárvore direita em pós-ordem
            visita(self.raiz) # visita a raiz
            
    def ordem_sim(self): # percurso em ordem simétrica
        if self!=None:
            pos_ordem(self.le) # percorre a subárvore esquerda em ordem simétrica
            pos_ordem(self.ld) # percorre a subárvore direita em ordem simétrica
            visita(self.raiz) # visita a raiz
