class Tweet:
    def __init__(self, name, followers=0):
        self.name = name
        self.followers = followers;
        print('Hi.', name, followers)
        
    def printName(self):
        print('Name is', self.name)

    def printFollowers(self):
        print('Followers are', self.followers)
 
a = Tweet('Test', 10)
b = Tweet('Test2')

a.printName()
a.printFollowers()


