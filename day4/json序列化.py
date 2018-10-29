import pickle

def sayhi(name):
  print("hello", name)

info = {
  'name': 'alex',
  'age': 22,
  'fun': sayhi
}
f = open("test.txt", 'wb')
# f.write(json.dumps(info))
# f.write(pickle.dumps(info))
pickle.dump(info, f)

f.close()