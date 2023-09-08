# Cookie Jar class
class Jar:

    # initialize a cookie jar with the given capacity,  If capacity is not a non-negative int, though, __init__ should instead raise a ValueError.
    def __init__(self, capacity=12):
        if capacity < 0:
            raise ValueError("Jar can't have a negative capacity")
        self.capacity = capacity
        self.size = 0

    # n 🍪, where n is the number of cookies in the cookie jar.if there are 3 cookies in the cookie jar, then str should return "🍪🍪🍪"
    def __str__(self):
        return "🍪" * self.size


    # adds n cookies to the cookie jar. If adding that many would exceed the cookie jar’s capacity, though, instead raise a ValueError.
    def deposit(self, n):
        if(n + self.size) > self.capacity:
            raise ValueError("You've exceeded the jar capacity")
        self.size = self.size + n

    # removes n cookies from the cookie jar. Nom nom nom. If there aren’t that many cookies in the cookie jar, though, withdraw should instead raise a ValueError.
    def withdraw(self, n):
        if(self.size - n) < 0:
            raise ValueError("There isn't enough cookies in the cookie jar")
        self.size = self.size - n

    # returns the cookie jar’s capacity.
    @property
    def capacity(self):
        return self._capacity

    #This is the capacity  of cookie jar setter >:|
    @capacity.setter
    def capacity(self, capacity):
        self._capacity = capacity

    # returns the number of cookies actually in the cookie jar, initially 0.
    @property
    def size(self):
        return self._size

    #This is the cookie size setter >:|
    @size.setter
    def size(self, size):
        self._size = size

# Main methods
def main():
    jar = get_jar()
    print(jar)

def get_jar():
    capacity = input("Jar capacity: ")
    return Jar(int(capacity))

if __name__ == "__main__":
    main()