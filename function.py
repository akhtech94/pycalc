def test(*args, **kwargs):
    print(args)
    print(kwargs)
    
mylist = ['Sreeshma', 'Shaji', 'Akhil', 'Ajit']
mydict = {'sister': 'Shilpa', 'Mother':'Sreeji'}

test(*mylist, **mydict)    
