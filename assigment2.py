def classify(value):
    if value < 998:
        return "Below range"
    elif value <= 1002:
        return "In range"
    else:
        return "Above range"

def calculate_average(total, count):
    number = total / count
    number_1=number
    return number_1

packet=int(input("enter the number of packets: "))
total=0
below_count=0
in_count=0
above_count=0
for i in range(packet):
    weight=int(input("Enter the coffee packet weight"))
    result=classify(weight)
    print(result)
    total=total+weight
    if result == "Below range":
        below_count=below_count+1
    elif result == "In range":
        in_count=in_count+1
    else:
        above_count=above_count+1
average=calculate_average(total, packet)
print(f"Total weight: {total} g")
print(f"Average wieght: {average} g")
print(f"Below range: {below_count}")
print(f"In range: {in_count}")
print(f"Above range: {above_count}")