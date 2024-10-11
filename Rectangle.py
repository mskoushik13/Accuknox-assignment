class Rectangle:
    def __init__(self, length: int, width: int):
        self.length = length
        self.width = width

    def __iter__(self):
        yield {'length': self.length}
        yield {'width': self.width}

    def __setattr__(self, name, value):
        if name in ('length', 'width') and (not isinstance(value, int) or value <= 0):
            raise ValueError(f"{name.capitalize()} must be a positive integer")
        super().__setattr__(name, value)

def create_rectangle():
    length = int(input("Enter the length of the rectangle: "))
    width = int(input("Enter the width of the rectangle: "))
    return Rectangle(length, width)

rectangle = create_rectangle()

for attribute in rectangle:
    print(attribute)

new_length = int(input("\nEnter new length: "))
new_width = int(input("Enter new width: "))

rectangle.length = new_length
rectangle.width = new_width

print("\nAfter modifying dimensions:")
for attribute in rectangle:
    print(attribute)
