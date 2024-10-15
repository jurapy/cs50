class Jar:
    def __init__(self, capacity=12):
        self.capacity = capacity
        self.cookies = 0

    # Getter
    @property
    def capacity(self):
        return self._capacity

    # Setter
    @capacity.setter
    def capacity(self, capacity):
        if capacity < 0:
            raise ValueError('Capacity less then zero')
        self._capacity = capacity

    def __str__(self):
        return '🍪' * self.cookies

    def deposit(self, value):
        if (self.cookies + value) > self.capacity:
            raise ValueError('To much cookies')
        self.cookies += value

    def withdraw(self, value):
        if (self.cookies - value) < 0:
            raise ValueError('No more cookies')
        self.cookies -= value

    @property
    def size(self):
        return self.cookies


def main():
    jar1 = Jar(1)
    jar1.deposit(0)
    print(str(jar1))
    jar1.withdraw(1)
    sys.exit(0)


if __name__ == '__main__':
    main()
