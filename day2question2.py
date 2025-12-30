print("Hello World")

# using single quate
print('Hello World')

#  using  function
msg = "Hello World"
print(msg)

#  using class
class Hello:
    def say(self):
        print("hello, world")
        Hello().say()

    
#  using f string
text ="world"
print(f"Hello,{text}!")

# One -liear creative Way
print("Hello World",sep="")

#  using generator
def gen():
    yield"Hello World"
    print(next(gen()))

    # using recurrsiom
    def Hello(n):
        if n ==1:
            print("Hello World!")
            Hello(1)


            # using Evl
            eval('print("hello World")')
        