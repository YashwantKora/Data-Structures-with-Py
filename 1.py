#1 Implement an ADT with all its operations

class Date:
    def __init__(self):
        self.day = 0
        self.month = 0
        self.year = 0

date1 = Date()
date1.day = 23
date1.month = 2
date1.year = 2007

print("Day:", date1.day)
print("month:", date1.month)
print("year:", date1.year)

# Type	Complexity
# Time	O(1)
# Space	O(1)