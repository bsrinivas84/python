class HelloWorld:
    def greet(self):
        print("Hello, World!")

    def testList(self):
        my_list = [1, 2, 3, 4, 5]
        for item in my_list:
            print(item)

    def testDictionary(self):
        my_dict = {"name1" : "Mike", "name2": "chi", "name3": "Tao"}
        for key,value in my_dict.items():
            print(my_dict[key])


if __name__ == "__main__":
    hello = HelloWorld()
    #hello.greet()
    #hello.testList()
    hello.testDictionary()