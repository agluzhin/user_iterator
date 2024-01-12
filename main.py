users = ['alex', 'efim', 'alyona', 'john', 'edward', 'vladimir', 'artur']


class UserIterator:

    def __init__(self, collection):
        self.collection = collection
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.collection):
            raise StopIteration()

        user = self.collection[self.index]
        self.index += 1
        return user


for user in UserIterator(users):
    print(user)
