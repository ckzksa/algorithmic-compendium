import mmh3
from bitarray import bitarray

class BloomFilter:
    def __init__(self, size, hash_count):
        self.size = size
        self.hash_count = hash_count
        self.bit_array = bitarray(size)
        self.bit_array.setall(False)

    def _get_hash_indexes(self, element):
        hash_indexes = []
        for seed in range(self.hash_count):
            hash_value = mmh3.hash(element, seed) % self.size
            hash_indexes.append(hash_value)
        return hash_indexes

    def add(self, element):
        hash_indexes = self._get_hash_indexes(element)

        bit_values = [self.bit_array[index] for index in hash_indexes]
        if all(bit_values):
            print(f"Collision detected - {element}")
            return

        for index in hash_indexes:
            self.bit_array[index] = True

    def check(self, element):
        return all([self.bit_array[index] for index in self._get_hash_indexes(element)])


if __name__ == "__main__":
    bf = BloomFilter(size=42, hash_count=3)
    elements = ["alpha", "beta", "gamma", "gamma"]
    for element in elements:
        bf.add(element)

    print(bf.check("alpha"))
    print(bf.check("beta"))
    print(bf.check("gamma"))
    print(bf.check("delta"))
