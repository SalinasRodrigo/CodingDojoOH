# insert_at(self, val, n): inserta un nodo con valor val como el n-ésimo nodo en la lista

class SList:
    def __init__(self):
        self.head = None
        self.len=0
        
    def add_to_front(self, val):	# agregó esta línea, toma un valor
        newNode = SLNode(val)	# crea una nueva instancia de nuestra clase Node usando el valor dado
        current_head = self.head
        newNode.next = current_head
        self.head = newNode
        self.len+=1
        return self

    def add_to_back(self, val):
        newNode = SLNode(val)

        if (self.head==None):
            self.head=newNode
            self.len+=1
            return self

        pointer=self.head
        while(pointer.next!=None):
            pointer=pointer.next
        pointer.next=newNode

        self.len+=1
        return self

    def insert_at(self, val, n):
        if(n==0):
            self.add_to_front(val)
            return self
        if(n==self.len):
            self.add_to_back(val)
            return self
        if(n>self.len):
            print("error, n es mayor a la longitud de la lista")
            return self

        newNode = SLNode(val)
        pointer=self.head
        for i in range(n-1):
            pointer=pointer.next
        aux=pointer.next
        pointer.next=newNode
        pointer.next.next=aux

        self.len+=1
        return self

    def remove_from_front(self):
        num=self.head.value
        if(self.head==None):
            self.len-=1
            return self

        self.head=self.head.next
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


        self.len-=1
        return self

    def print_values(self):
        runner = self.head
        while(runner!=None):
            print(runner.value)
            runner=runner.next
        return self
        

class SLNode:
        def __init__(self, val):
            self.value = val
            self.next = None

lista1 = SList()
lista1.add_to_front(1)
lista1.add_to_front(2)
lista1.add_to_front(3)
lista1.add_to_front(4)
lista1.add_to_front(5)
lista1.add_to_back(6)
lista1.add_to_back(7)
lista1.add_to_back(8)
lista1.print_values()
print("Longitud:",lista1.len)
print("eliminamos: ",lista1.remove_from_front())
print("eliminamos: ",lista1.remove_from_front())
lista1.print_values()
print("Longitud:",lista1.len)
print("eliminamos: ",lista1.remove_from_back())
print("eliminamos: ",lista1.remove_from_back())
lista1.print_values()
print("Longitud:",lista1.len)
print("eliminamos: 2")
lista1.remove_val(2)
lista1.print_values()
print("Longitud:",lista1.len)
print("eliminamos: 3")
lista1.remove_val(3)
lista1.print_values()
print("Longitud:",lista1.len)
print("eliminamos: 6")
lista1.remove_val(6)
print("eliminamos: 1")
lista1.remove_val(1)
lista1.print_values()
print("Longitud:",lista1.len)
print("Agregamos los valores otra vez")
lista1.add_to_front(1)
lista1.add_to_front(2)
lista1.add_to_front(3)
lista1.add_to_front(4)
lista1.add_to_front(5)
lista1.add_to_back(6)
lista1.add_to_back(7)
lista1.add_to_back(8)
lista1.print_values()
print("Longitud:",lista1.len)
print("incertamos el 9 en la posición 2")
lista1.insert_at(9,2)
lista1.print_values()
print("Longitud:",lista1.len)
print("incertamos el 20 en la posición 1")
lista1.insert_at(20,1)
lista1.print_values()
print("Longitud:",lista1.len)
print("incertamos el 15 en la posición 0")
lista1.insert_at(15,0)
lista1.print_values()
print("Longitud:",lista1.len)
