class encrpyt:
    def solve(self, s, k):
        def shift(c):
            i = ord(c) - ord('a')
            i += k
            i %= 26
            return chr(ord('a') + i)

        return "".join(map(shift, s))
        
ob = encrpyt()
word = str(input("Enter a message to encrypt: "))
print(("Encrypted message: " + ob.solve(word, 3)))
print(ob.solve("Hello World", 3))