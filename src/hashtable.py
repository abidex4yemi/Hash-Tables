# '''
# Linked List hash table key/value pair
# '''


class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

    def __str__(self):
        return "<Node: (%s, %s), next: %s>" % (self.key, self.value, self.next)


class HashTable:
    def __init__(self, capacity):
        self.capacity = capacity
        self.size = 0
        self.storage = [None] * self.capacity

    def _hash(self, key):
        sum = 0
        for pos in range(len(key)):
            sum = sum + ord(key[pos])

        return sum % self.capacity

    def _hash_djb2(self, key):
        pass

    def _hash_mod(self, key):
        return self._hash(key) % self.capacity

    def insert(self, key, value):
        self.size += 1

        index = self._hash(key)

        node = self.storage[index]

        if node is None:
            self.storage[index] = LinkedPair(key, value)
            return

        prev = node
        while node is not None:
            if prev.key == key:
                prev.value = value
            prev = node
            node = node.next

        prev.next = LinkedPair(key, value)

    def remove(self, key):
        index = self._hash(key)
        node = self.storage[index]
        prev = None

        while node is not None and node.key != key:
            prev = node
            node = node.next

        if node is None:
            return None
        else:
            self.size -= 1
            result = node.value

            if prev is None:
                node = None
            else:
                prev.next = prev.next.next

            return result

    def retrieve(self, key):
        index = self._hash(key)

        node = self.storage[index]

        while node is not None and node.key != key:
            node = node.next

        if node is None:
            return None
        else:
            return node.value

    def resize(self):
        self.capacity *= 2

        old_storage_content = self.storage

        self.storage = [None] * self.capacity
        for node in old_storage_content:
            if node:
                self.insert(node.key, node.value)


if __name__ == "__main__":
    ht = HashTable(3)

    ht.insert("line_1", "Tiny hash table")
    ht.insert("line_2", "Filled beyond capacity")
    ht.insert("line_3", "Linked list saves the day!")

    print("")

    # Test storing beyond capacity
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    # Test resizing
    old_capacity = len(ht.storage)
    ht.resize()
    new_capacity = len(ht.storage)

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    print("")
