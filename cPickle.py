import pickle
test_data_file = 'testdata.txt'
test_data = ['save me',123,True]
myname = 'lihh'
myage = 18
data = (test_data, myname, myage)
f = open(test_data_file,'wb')
pickle.dump(data,f)
f.close()
j = open(test_data_file,'rb')
g = pickle.load(j)
print(g)
j.close()