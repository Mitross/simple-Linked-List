class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insertAtBegin(self,data):
        nn = Node(data)
        if self.head is None:
            self.head = nn
            return
        else:
            nn.next = self.head
            self.head = nn

    def insertAtEnd(self,data):
        nn = Node(data)
        if self.head is None:
            self.head = nn
            return
        cn = self.head
        while (cn.next):
            cn = cn.next
        cn.next = nn

    def insertAtIndex(self,data,index):
        if (index==0):
            self.insertAtBegin(data)
            return
        pos = 0
        cn = self.head
        while (cn != None and pos!=index):
            pos = pos + 1
            cn = cn.next
        if(cn!=None):
            nn = Node(data)
            nn.next = cn.next
            cn.next = nn
        else:
            print("index not present")

    def updateIndex(self,val,index):
        if(index==0):
            self.head.data = val
            return
        
        pos = 0
        cn = self.head
        while(cn!= None and pos+1!=index):
            pos = pos+1
            cn = cn.next

        if(cn is not None):
            cn.data = val
        else:
            print("index not present")

    def removeFisrtNode(self):
        if(self.head is None):
            return
        self.head = self.head.next
        
    def removeLastNode(self):
        if(self.head is None):
            return
        cn = self.head
        while(cn.next!=None and cn.next.next!=None):
            cn = cn.next
        cn.next = None
    
    def removeAtIndex(self,index):
        if (self.head is None):
            return
        
        pos=0
        cn = self.head

        while(cn is not None and pos<index+1):
            cn=cn.next
        
        if(cn is None or cn.next is None):
            print("index not present")
        else:
            cn.next = cn.next.next

    def remove_node(self,val):
        if (self.head is None):
            return
        
        cn = self.head 
        if(cn.data==val): 
            self.removeFisrtNode
        
        
        while(cn is not None and cn.next is not None and cn.next.data!=val):
            cn = cn.next

        if(cn is not None and cn.next is not None):
            cn.next = cn.next.next
            return
        
        print("no such node")

    def size(self):
        if self.head is None: 
            return 0
        
        count = 1
        cn = self.head
        while(cn.nest is not None):
            pos = pos + 1
            cn=cn.next
        return count
    
if __name__ == "__main__":
    import datetime
    print(datetime.datetime.now())
    print("---ALL GOOD---")
    print("this file has all the functions for  o linked list")

        
        


