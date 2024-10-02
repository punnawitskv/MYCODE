class Data:
    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __str__(self):
        return "({0}, {1})".format(self.key, self.value)


class HashTable:
    def __init__(self, size, max_collision):
        self.table = [None] * size
        self.size = size
        self.max_collision = max_collision
        self.collision_count = 0
        self.is_full_message_shown = False

    def get_index(self, key):
        ascii_sum = sum(ord(c) for c in key)
        return ascii_sum % self.size

    def is_full(self):
        return all(self.table)

    def insert(self, data):
        if self.is_full():
            if not self.is_full_message_shown:
                print("This table is full !!!!!!")
                self.is_full_message_shown = True
            return

        index = self.get_index(data.key)
        collision_chain = 0
        while collision_chain < self.max_collision:
            if self.table[index] is None:
                self.table[index] = data
                self.print_table()
                return
            else:
                print(f"collision number {collision_chain+1} at {index}")
                collision_chain += 1
                index = (self.get_index(data.key) + collision_chain ** 2) % self.size

        print("Max of collisionChain")
        self.print_table()

    def print_table(self):
        for i in range(self.size):
            if self.table[i]:
                print(f"#{i+1}\t{self.table[i]}")
            else:
                print(f"#{i+1}\tNone")
        print("---------------------------")


print(" ***** Fun with hashing *****")
user_input = input("Enter Input : ")
left, right = user_input.split('/')
table_size, max_collision = map(int, left.split())
data_pairs = [item.split() for item in right.split(',')]

hash_table = HashTable(table_size, max_collision)

for key, value in data_pairs:
    data = Data(key, value)
    hash_table.insert(data)
