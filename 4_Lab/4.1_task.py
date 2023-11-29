class MyString:
    def __init__(self, value):
        self.value = value

    def length(self):
        return len(self.value)

    def uppercase(self):
        return self.value.upper()

    def count_vowels(self):
        vowels = "aeiouAEIOU"
        return sum(1 for char in self.value if char in vowels)

    def reverse(self):
        return self.value[::-1]

    def replace(self, old, new):
        return self.value.replace(old, new)

    def display(self):
        print(self.value)

my_str = MyString("Hello, World!")

print("Original String:")
my_str.display()
print("Length:", my_str.length())
print("Uppercase:")
MyString(my_str.uppercase()).display()
print("Vowel Count:", my_str.count_vowels())
print("Reversed String:")
MyString(my_str.reverse()).display()
print("Replaced String:")
MyString(my_str.replace("Hello", "Hi")).display()