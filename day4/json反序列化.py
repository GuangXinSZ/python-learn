import pickle

def sayhi(name):
  print("hello", name)

f = open("test.txt", "rb")

data = pickle.loads(f.read())
 
print(data['fun']('namsse'))