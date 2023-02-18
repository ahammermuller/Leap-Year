# Function inside a class is called method and the first argument is always self

class Example:
    def __init__(self, greeting) -> None:
        print("I AM IN THE CONSTRUCTOR")
        self.text = greeting


    def hello(self, text2, text3="default value"):
        print(self.text)
        print(text2)
        print(text3)




# obj = Example()
# type(obj)
# obj.hello()

