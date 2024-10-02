def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def next_prime(num):
    while True:
        num += 1
        if is_prime(num):
            return num

class HashTable:
    def __init__(self, size, max_collision, threshold):
        self.size = size
        self.max_collision = max_collision
        self.threshold = threshold / 100
        self.table = [None] * size
        self.count = 0

    def load_factor(self):
        return ((self.count + 1) / self.size) 

    def rehash(self, key = None):
        new_size = next_prime(self.size * 2)
        old_table = self.table
        self.table = [None] * new_size
        self.size = new_size
        self.count = 0

        for index in range(len(old_table) -1, -1, -1):
            item = old_table[index]
            if item is not None:
                self.add(item)

        if key is not None:
            self.add(key)

    def add(self, key):
        index = key % self.size
        index_start = index
        collisions = 0
        
        if self.load_factor() >= self.threshold:
            print("****** Data over threshold - Rehash !!! ******")
            self.rehash(key)
            # self.add(key)
            return

        while self.table[index] is not None:
            collisions += 1
            print(f"collision number {collisions} at {index}")

            if collisions >= self.max_collision:
                print("****** Max collision - Rehash !!! ******")
                self.rehash()
                self.add(key)
                return

            index = (index_start + collisions**2) % self.size
        
        self.count += 1
        self.table[index] = key

    def display(self):
        for i, v in enumerate(self.table):
            print(f"#{i + 1}\t{v}")

def main():
    print(" ***** Rehashing *****")
    input_data = input("Enter Input : ").strip().split('/')
    left_part = list(map(int, input_data[0].split()))
    right_part = list(map(int, input_data[1].split()))

    size, max_collision, threshold = left_part
    hash_table = HashTable(size, max_collision, threshold)

    print("Initial Table :")
    hash_table.display()
    print("----------------------------------------")

    for value in right_part:
        print(f"Add : {value}")
        hash_table.add(value)
        hash_table.display()
        print("----------------------------------------")

if __name__ == "__main__":
    main()
