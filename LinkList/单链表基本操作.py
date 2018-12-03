# 结点类
class Node(object):
   def __init__(self,data):
       self.data = data
       self.next = None

# 链表类
class LinkList(object):
   def __init__(self):
       self.head = Node(None)

   # 判断链表是否为空
   def IsEmpty(self):
       p = self.head # 头指针

       if p.next == None:
           print("List is Empty")
           return True
       return False

   # 打印链表
   def PrintList(self):
       if self.IsEmpty():
           return False

       p = self.head
       while p:
           print(p.data,end= ' ')
           p = p.next
   # 创建单链表
   def InitList(self,data):
       self.head = Node(data[0]) # 头结点
       p = self.head # 头指针

       for i in data[1:]:
           node = Node(i)
           p.next = node
           p = p.next

   # 单链表的长度
   def LengthList(self):
       if self.IsEmpty():
           return 0
       p = self.head
       cnt = 0
       while p:
           cnt += 1
           p = p.next
       return cnt

   # 单链表的插入(在第 s 个结点后面插入 data)
   def InsertList(self,s,data):
       if self.IsEmpty() or s < 0 or s > self.LengthList():
           print("Insert failed！")
           return
       p = self.head
       index = 1
       while index < s:
           p = p.next
           index += 1

       node = Node(data)
       node.next = p.next
       p.next = node

   # 单链表的删除(删除第 s 个结点)
   def DeleteList(self, s):
       if self.IsEmpty() or s < 0 or s > self.LengthList():
           print("Delete failed! ")
           return
       p = self.head
       index = 1
       while index < s:
           pre = p
           index += 1
           p = p.next
       pre.next = p.next
       p = None

   # 单链表的读取（获取第 s 个结点的值）
   def GetList(self, s):
       if self.IsEmpty() or s < 0 or s > self.LengthList():
           print("Read failed! ")
           return
       p = self.head
       index = 1
       while index < s:
           index += 1
           p = p.next
       print("第 {} 个值为 {}".format(s, p.data))
