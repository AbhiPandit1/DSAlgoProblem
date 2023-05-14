#Linked list is as linear data structure
#Ordered data structure 


class Node:
  # constructor
  def __init__(self, data = None, next=None): 
    self.data = data
    self.next = next

# A Linked List class with a single head node
class LinkedList:
  def __init__(self):  
    self.head = None
   

#insertion
  def insertionAtEnd(self,data):
    temp1=Node(data)
    if self.head is None:
        self.head=temp1
    else:
        curr=self.head
        while curr.next:
            curr=curr.next
        curr.next=temp1
#Printing the element
  def Print(self):
    curr=self.head
    while curr != None:
        print(curr.data)
        curr=curr.next



    




# Inserting at first Position
  def Finsert(self,data):
    newNode=Node(data)
    if self.head is None:
        self.head=newNode
    else:
        curr=self.head
        self.head=newNode
        newNode.next=curr
    

# Inserting after some value
  def insertAt(self,data,pos):
    newNode=Node(data)
    if pos<1:
        print("not possible")
    elif pos==1:
        LL.Finsert(newNode.data)
    
    else:
        curr=self.head
        for i in range(pos-2):
            if curr!=None:
                curr=curr.next
        if curr!=None:
            newNode.next=curr.next
            curr.next=newNode
  
  
  def DeleteLast(self):
    curr=self.head
    if curr==None:
      print("Nothing Here")
    elif curr.next==None:
      return None
    else:
      while curr.next.next!=None:
        curr=curr.next
      curr.next=None
    LL.Print()

  def DeleteAtPos(self,pos):
    if pos==0:
      print("Not possible")
    else:
      curr=self.head
      for i in range(pos-1):
        curr=curr.next
      prev=curr.next.next
      curr.next=prev
  

  def Reverse(self):
    curr=self.head
    prev=None
    while curr!=None:
      next=curr.next
      curr.next=prev
      prev=curr
      curr=next 
      self.head=prev  
    return 
  

  def mid(self):
    Fast=self.head
    DoubleFast=self.head


    while Fast.next.next!=None:
      Fast=Fast.next
      DoubleFast=DoubleFast.next.next
    print(Fast.data)
      
      
    

      


  

  



# Singly Linked List with insertion and print methods
LL = LinkedList()
LL.insertionAtEnd(3)
LL.insertionAtEnd(5)
LL.insertionAtEnd(7)
LL.insertionAtEnd(9)
LL.insertionAtEnd(11)
LL.insertionAtEnd(13)
LL.insertionAtEnd(15)


#LL.DeleteAtPos(2)
#LL.Print()
LL.Reverse()
LL.mid()
LL.Print()









