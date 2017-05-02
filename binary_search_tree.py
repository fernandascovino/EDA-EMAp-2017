class BSNode: 
    def __init__(self, chave, raiz=None, le=None, ld=None):
        self.chave = chave # a chave irá nos auxiliar na ordenação dos elementos
        self.raiz = raiz
        self.le = le
        self.ld = ld

class BSTree: 
    
    """
    Uma árvore binária de busca é aquela em que, para todo nó v, 
    todo elemento menor que v está na subárvore a sua esquerda
    e todo elemento maior que v está na subárvore a sua direita
    """
    
    def __init__(self, chave=None, raiz=None, le=None, ld=None):
        self.chave = chave
        self.raiz = raiz
        self.le = le
        self.ld = ld
        
    def busca(self,v):
        
        """
        Retorna:
        0, se a árvore é vazia
        1, se v pertence à árvore
        >1, se v não pertence à árvore
        """
        
        self.f = None
        
        if self.chave == None:
            self.f = 0
        elif self.chave == v.chave:
            f = 1
        elif v.chave < self.chave:
            if self.pt.le == None:
                self.f = 2
            else:
                self = self.le
                self.busca(v)
        elif v.chave > self.chave:
            if self.ld == None:
                self.f = 3
            else:
                self = self.pt.ld
                self.busca(v)
        return self.f
    
    def inserir(self,v):
            
        self.f = self.busca(v)
        
        if self.f == 1:
            "O elemento já existe"
        elif self.f == 0:
            self.pt = v
        elif self.f == 2:
            self.pt.le = v
        elif self.f == 3:
            self.pt.ld = v  
            
    def remove(self,v):
        
        self.busca(v)
        
        if self.f == 1:
            right = self.ld
            left = self.le
            while novo != None: # buscamos o nó mais à esquerda da subárvore direita de v
                    novo = left.le
            novo = self.le # inserimos a subárvore esquerda de v nesse nó
            self = self.ld # substituímos v pela sua subárvore direita
