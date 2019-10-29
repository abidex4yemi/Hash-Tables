# '''
# Linked List hash table key/value pair
# '''


class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class HashTable:
    def __init__(self, size):
        self.capacity = 25
        self.size = 0
        self.storage = [None] * self.capacity

    def _hash(self, key):
        hashsum = 0
        # For each character in the key

        for idx, c in enumerate(key):
            # Add (index + length of key) ^ (current char code)

            hashsum += (idx + len(key)) ** ord(c)
            # Perform modulus to keep hashsum in range [0, self.capacity - 1]

            hashsum = hashsum % self.capacity
        return hashsum

    def _hash_djb2(self, key):
        pass

    def _hash_mod(self, key):
        return self._hash(key) % self.capacity

    def insert(self, key, value):
        # 1. Increment size

        self.size += 1
        # 2. Compute index of key

        index = self._hash(key)
        # Go to the node corresponding to the hash

        node = self.storage[index]
        # 3. If bucket is empty:

        if node is None:
            # Create node, add it, return

            self.storage[index] = LinkedPair(key, value)
            return
        # 4. Collision! Iterate to the end of the linked list at provided index

        prev = node
        while node is not None:
            prev = node
            node = node.next
        # Add a new node at the end of the list with provided key/value

        prev.next = LinkedPair(key, value)

    def remove(self, key):
        # 1. Compute hash

        index = self._hash(key)
        node = self.storage[index]
        prev = None
        # 2. Iterate to the requested node

        while node is not None and node.key != key:
            prev = node
            node = node.next
        # Now, node is either the requested node or none

        if node is None:
            # 3. Key not found

            return None
        else:
            # 4. The key was found.

            self.size -= 1
            result = node.value
            # Delete this element in linked list

            if prev is None:
                node = None
            else:
                prev.next = prev.next.next
            # Return the deleted language

            return result

    def retrieve(self, key):
        # 1. Compute hash

        index = self._hash(key)
        # 2. Go to first node in list at bucket

        node = self.storage[index]
        # 3. Traverse the linked list at this node

        while node is not None and node.key != key:
            node = node.next
        # 4. Now, node is the requested key/value pair or None

        if node is None:
            # Not found

            return None
        else:
            # Found - return the data value

            return node.value

    def resize(self):
        pass


if __name__ == "__main__":
    ht = HashTable(2)

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
