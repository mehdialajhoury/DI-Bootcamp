import math
"""Goal:

Create a Pagination class that simulates a basic pagination system.



Step 1: Create the Pagination Class

Define a class called Pagination to represent paginated content.
It should optionally accept a list of items and a page size when initialized.


Step 2: Implement the __init__ Method

Accept two optional parameters:
items (default None): a list of items
page_size (default 10): number of items per page

Behavior:

If items is None, initialize it as an empty list.
Save page_size and set current_idx (current page index) to 0.
Calculate total number of pages using math.ceil.


Step 3: Implement the get_visible_items() Method

This method returns the list of items visible on the current page.
Use slicing based on the current_idx and page_size.


Step 4: Implement Navigation Methods

These methods should help navigate through pages:

go_to_page(page_num)
→ Goes to the specified page number (1-based indexing).
→ If page_num is out of range, raise a ValueError.

first_page()
→ Navigates to the first page.

last_page()
→ Navigates to the last page.

next_page()
→ Moves one page forward (if not already on the last page).

previous_page()
→ Moves one page backward (if not already on the first page).

📝 Note:

Pages are indexed internally from 0, but user input is expected to start at 1.
All navigation methods (except go_to_page) should return self to allow method chaining.


Bonus
Step 5: Add a Custom __str__() Method**

This magic method should return a string displaying the items on the current page, each on a new line.
Example:

alphabetList = list("abcdefghijklmnopqrstuvwxyz")
p = Pagination(alphabetList, 4)
print(str(p))
# Output:
# a
# b
# c
# d


Step 6: Test Your Code

Use the following test cases:

alphabetList = list("abcdefghijklmnopqrstuvwxyz")
p = Pagination(alphabetList, 4)

print(p.get_visible_items())
# ['a', 'b', 'c', 'd']

p.next_page()
print(p.get_visible_items())
# ['e', 'f', 'g', 'h']

p.last_page()
print(p.get_visible_items())
# ['y', 'z']

p.go_to_page(10)
print(p.current_idx + 1)
# Output: ValueError

p.go_to_page(0)
# Raises ValueError"""

class Pagination:

    def __init__(self,items=None,page_size=10):
        
        self.items=items
        self.page_size = page_size

        if self.items == None:
            self.items = []

        self.current_idx = 0
        # Total pages : Number of items / Page Size => We apply ceil, to get to the superior integer
        self.total_pages = math.ceil(len(self.items) / self.page_size)

    # Return the item visibles, according to the page_size specified
    def get_visible_items(self):
        first_item = self.current_idx * self.page_size
        last_item = first_item + self.page_size
        return self.items[first_item:last_item]
    
    # We pay attention here to the page_num entered by ther user
    # If the page_num is superior to the max page -> Raise an error
    # If the page_num is 1, the index is 0 ! (The index of the items list)
    # For all other page_num entered, we substract 1 to the index
    def go_to_page(self, page_num):
        if page_num > self.total_pages:
            raise ValueError(f"The page specified is out of range. Max page = {self.total_pages}")
        elif page_num == 1:
            self.current_idx = 0
        else:
            self.current_idx = page_num - 1

    def first_page(self):
        self.current_idx = 0
        return self

    def last_page(self):
        self.current_idx = self.total_pages -1
        return self

    def next_page(self):
        if self.current_idx != self.total_pages:
            self.current_idx += 1
        else:
            print("Your are already at the last page !")
        return self

    def previous_page(self):
        if self.current_idx != 0:
            self.current_idx -= 1
        else:
            print("You are already at the first page !")
        return self
    
    # Bonus :
    def __str__(self):
        string_item = ""
        for item in self.get_visible_items():
            if string_item != "":
                string_item = string_item + "\n"+ item
            else:
                string_item = item
        return string_item

    

# Test program :

alphabetList = list("abcdefghijklmnopqrstuvwxyz")
p = Pagination(alphabetList, 4)

print(f"start page : {p.get_visible_items()}")
p.go_to_page(1)
print(f"Page 1 : {p.get_visible_items()}")
p.go_to_page(3)
print(f"Page 3 : {p.get_visible_items()}")
p.previous_page()
print(f"Previous page : {p.get_visible_items()}")
p.next_page()
print(f"Next page : {p.get_visible_items()}")
p.last_page()
print(f"Last page : {p.get_visible_items()}")
# Test page does not exist
#p.go_to_page(10)

# Test Bonus str
print(p.__str__())