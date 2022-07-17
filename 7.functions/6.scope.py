#global scope

x = 'global x'

def function():
    x= 'local x'
    print(x)


function()
print(x)


##################
name="hasan"

def greeting():
    #name= 'Mustafa'
    
    def hello():
        #name = 'Murtaza'
        print('Hello' + " " +name)
        
    hello()

greeting()

########################3

x = 50

def test():
    global x
    print(f'x : {x}')
    
    x = 100
    print(f'x : {x}')
    
    
test()
print(f'x : {x}')