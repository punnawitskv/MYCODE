class Data:
    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __str__(self):
        return "({0}, {1})".format(self.key, self.value)


class Hash:
    def __init__(self, size, max_collision):
        self.size = size
        self.max_collision = max_collision
        self.table = [None] * size
        self.full_message_shown = False

    def get_index(self, key):
        total_ascii = sum(ord(char) for char in key)
        return total_ascii % self.size

    def is_full(self):
        return all(slot is not None for slot in self.table)

    def insert(self, data):
        index = self.get_index(data.key)
        collision_count = 0

        while self.table[index] is not None:
            print(f"collision number {collision_count + 1} at {index}")
            collision_count += 1
            if collision_count >= self.max_collision:
                print("Max of collisionChain")
                return

            index = (self.get_index(data.key) + collision_count**2) % self.size

            if self.is_full():
                if not self.full_message_shown:
                    print("This table is full !!!!!!")
                    self.full_message_shown = True
                return

        self.table[index] = data

    def display(self):
        for i in range(self.size):
            print(f"#{i+1}\t{self.table[i]}")
        print("---------------------------")


print(" ***** Fun with hashing *****")
left, right = input("Enter Input : ").split('/')
size, max_collision = map(int, left.split())
hash_table = Hash(size, max_collision)

data_entries = right.split(',')
for entry in data_entries:
    key, value = entry.split()
    data = Data(key, value)
    hash_table.insert(data)
    hash_table.display()
