class Hashing:
  def __init__(self,c1,c2,m):
    self.hashtable = []
    for i in range(m):
        self.hashtable.append(None)     
    self.c1 = c1
    self.c2 = c2
    self.m = m
  def store_data(self, data):
      hk = data % self.m
      flag = 0
      for j in range(self.m):
        if self.hashtable[j] == None:
          flag = 1
      if flag == 1:
        if self.hashtable[hk] == None:
          self.hashtable[hk] = data
        else:
          for i in range(1,self.m):
            hki = (hk + self.c1*i + self.c2*i*i)%self.m
            if hki<self.m:
              if self.hashtable[hki] == None:
                self.hashtable[hki] = data
                break
      else:
          print("Hash table is full")
  def display_hashtable(self):
      return self.hashtable
c1 = int(input())
c2 = int(input())
m = int(input())
data=eval(input())
A = Hashing(c1,c2,m)
for i in data:
	A.store_data(i)
print(A.display_hashtable())