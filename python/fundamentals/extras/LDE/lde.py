# insert_at(self, val, n): inserta un nodo con valor val como el n-ésimo nodo en la lista

class DList:
    def __init__(self):
        self.head = None
        self.len=0
        
    def add_to_front(self, val):	# agregó esta línea, toma un valor
        newNode = DLNode(val)	# crea una nueva instancia de nuestra clase Node usando el valor dado
        if (self.len==0):
            self.head=newNode
            self.len+=1
            return self
        
        current_head = self.head
        newNode.next = current_head
        current_head.previous=newNode
        self.head = newNode
        self.len+=1
        return self

    def add_to_back(self, val):
        newNode = DLNode(val)

        if (self.head==None):
            self.head=newNode
            self.len+=1
            return self

        pointer=self.head
        while(pointer.next!=None):
            pointer=pointer.next
        pointer.next=newNode
        newNode.previous=pointer
        self.len+=1
        return self

    def remove_from_front(self):
        num=self.head.value
        if(self.head==None):
            return self

        self.head=self.head.next
        self.head.previous=None
        self.len-=1
        return num

    def remove_from_back(self):
        num=0
        if(self.head==None):
            self.len-=1
            return self

        pointer=self.head
        while(pointer.next.next!=None):
            pointer=pointer.next
        num=pointer.next.value
        pointer.next=None

        self.len-=1
        return num

    def remove_val(self, val):
        if(self.head.value==val):
            self.head=self.head.next
            self.len-=1
            return self

        pointer=self.head
        while(pointer.next.value!=val):
            pointer=pointer.next
        pointer.next=pointer.next.next
        if(pointer.next!=None):
            pointer.next.previous=pointer

        self.len-=1
        return self

    def print_values(self):
        runner = self.head
        while(runner!=None):
            print(runner.value)
            runner=runner.next
        return self
        
    def invertir(self):
        
        pointer = self.head
        while(pointer.next!=None):
            aux=pointer.next
            pointer.next=pointer.previous
            pointer.previous=aux
            pointer=aux   
        aux=pointer.next
        pointer.next=pointer.previous
        pointer.previous=aux
        self.head=pointer

        return self


class DLNode:
        def __init__(self, val):
            self.value = val
            self.next = None
            self.previous=None


lista1 = DList()
lista1.add_to_front(1)
lista1.add_to_front(2)
lista1.add_to_back(3)
lista1.add_to_front(4)
lista1.add_to_front(5)
lista1.add_to_back(6)
lista1.add_to_front(7)
lista1.add_to_front(8)
lista1.add_to_back(9)

lista1.print_values()
print("invertir")
lista1.invertir()
lista1.print_values()
