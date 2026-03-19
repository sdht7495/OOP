def row() :
    print('+', '----', end=' ')

def colum() :
    print('|    ', end=' ')

def row2():
    row()
    row()
    print('+')

def colum2():
    colum()
    colum()
    print('|')

def row4():
    row()
    row()
    row()
    row()
    print('+')

def colum4():
    colum()
    colum()
    colum()
    colum()
    print('|')

def net2():
    row2()
    colum2()
    row2()
    colum2()
    row2()

def net4():
    row4()
    colum4()
    row4()
    colum4()
    row4()
    colum4()
    row4()
    colum4()
    row4()

net2()
net4()





