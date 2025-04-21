import Third
import time

s = time.perf_counter()

def main():
    emp1 = Third.Employee('name', 'id', 'department')
    emp2 = Third.Employee('name', 'id', 'department')
    emp3 = Third.Employee('name', 'id', 'department')

    emp1.set_name("Virat")
    emp1.set_id('18')
    emp1.set_department('RCB')

    emp2.set_name("Rohit")
    emp2.set_id('45')
    emp2.set_department('MI')

    emp1.__str__()
    emp2.__str__()

main()
e = time.perf_counter()
print()
print("Time:", e-s)