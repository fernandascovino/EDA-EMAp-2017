class AVLNode:
    def __init__(self, chave, bal=0, le=None, ld=None):
        self.chave = chave
        self.bal = bal # variável que indica se a árvore está balanceada
        self.le = le
        self.ld = ld
        
    def caso1(self): # balanceia a árvore em que a folha de maior nível está na esquerda
        pt = self
        ptu = pt.le
        if ptu.bal == -1:
            pt.le = ptu.ld, ptu.ld = pt
            pt.bal = 0
            pt = ptu
        else:
            ptv = ptu.ld
            ptu.ld = ptv.le, ptv.le = ptu
            pt.le = ptv.ld, ptv.ld = pt
            if ptv.bal == -1:
                pt.bal = 1
            else:
                pt.bal = 0
            if ptv.bal == 1:
                ptu.bal = -1
            else:
                ptu.bal = 0
            pt = ptv
        pt.bal = 0
        self.h = False
            
    def caso2(self): # balanceia a árvore em que a folha de maior nível está na direita
        pt = self
        ptu = pt.ld
        if ptu.bal == 1:
            pt.ld = ptu.le, ptu.le = pt
            pt.bal = 0
            pt = ptu
        else:
            ptv = ptu.le
            ptu.le = ptv.ld, ptv.ld = ptu
            pt.ld = ptv.le, ptv.le = pt
            if ptv.bal == 1:
                pt.bal = -1
            else:
                pt.bal = 0
            if ptv.bal == -1:
                ptu.bal = 1
            else:
                ptu.bal = 0
            pt = ptv
        pt.bal = 0
        self.h = False

    def ins_AVL(self,x):
        pt = self
        if pt == None: # se a árvore é vazia, inserimos x na raiz
            pt = AVLNode(x)
            self.h = True
        elif x == pt.chave:
            print("O nó já pertence à árvore")
        elif x < pt.chave:
            if pt.le == None: # se pt.le é vazio, podemos inserir x no local
                pt.le = AVLNode(x)
                self.h = True
            else:
                pt.le.ins_AVL(x)
                if self.h == True: # mudamos o balanceamento da árvore com a inserção de x
                    if pt.bal == 1:
                        pt.bal = 0
                        self.h = False
                    elif pt.bal == 0:
                        pt.bal = -1
                        self.h = False
                    elif pt.bal == -1:  # a árvore está desbalanceada "para a esquerda"
                        self.caso1()
        else:
            if pt.ld == None: # se pt.ld é vazio, podemos inserir x no local
                pt.ld = AVLNode(x)
                self.h = True
            else:
                pt.ld.ins_AVL(x)
                if self.h == True:  # mudamos o balanceamento da árvore com a inserção de x
                    if pt.bal == -1:
                        pt.bal = 0
                        self.h = False
                    elif pt.bal == 0:
                        pt.bal = 1
                        self.h = False
                    elif pt.bal == -1: # a árvore está desbalanceada "para a direita"
                        self.caso2()
                        
### função para imprimir a árvore

def traverse(root): # imprime a árvore por níveis
    thislevel = [root]
    my_print = [root.chave]
    print(my_print)
    while thislevel:
        nextlevel = list()
        next_print = list()
        for n in thislevel:
            if n.le: 
                next_print.append(n.le.chave)
                nextlevel.append(n.le)
            if n.ld: 
                next_print.append(n.ld.chave)
                nextlevel.append(n.ld)
            thislevel = nextlevel
        print(next_print)      
# Adaptado de http://stackoverflow.com/questions/34012886/print-binary-tree-level-by-level-in-python/34013268

### testes
Novo = AVLNode(5)
Novo.ins_AVL(2)
Novo.ins_AVL(7)
Novo.ins_AVL(3)
Novo.ins_AVL(4)
Novo.ins_AVL(9)

traverse(Novo) # os nós são agrupados por nível, e não por parentesco

Novo2 = AVLNode(7)
Novo2.ins_AVL(5)
Novo2.ins_AVL(4)
Novo2.ins_AVL(3)
Novo2.ins_AVL(2)
Novo2.ins_AVL(9)

traverse(Novo2) # os nós são agrupados por nível, e não por parentesco

Novo3 = AVLNode(1)
Novo3.ins_AVL(2)
Novo3.ins_AVL(3)
Novo3.ins_AVL(4)
Novo3.ins_AVL(5)
Novo3.ins_AVL(7)

traverse(Novo3) # os nós são agrupados por nível, e não por parentesco
