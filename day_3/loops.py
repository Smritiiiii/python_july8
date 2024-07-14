age = 22 

height = 5.5 

complex = 3 + 4j

base = float(input("enter the base"))
height = float(input("enter the height"))
area = 0.5 * base * height
print(f"the height is {area}")

side_a = int (input("enter side A "))
side_b =  int (input ("enter side B"))
side_c = int (input("enter side C"))
perimeter = side_a + side_b + side_c
print(f"thr perimeter of the triangle is {perimeter}")

lenght = int (input("enter the length"))
width = int (input("enter te=he width"))
area = lenght * width
print(f"the area is{area}")
perimeter = 2*(lenght+width)
print(f"perimeter is {perimeter}")

# number 8 9 10 11 

len_1 =len("python")
len_2 = len("dragon")
falsy_comparison = len_1 > len_2
print(f"the lenght of python is {len_1}")
print(f"the lenght of dragon is {len_2}")
print(f"is the length of python greater than dragon ?{falsy_comparison}")

st_1 = "python"
st_2 = "dragon"
substring = "on"
check= substring in st_1 and substring in st_2 
print(f"Is '{substring}' found in both '{st_1}' and '{st_2}' {check}")

str = " i hope this course is not full of jagron"
substring = "jagron"
check = substring in str
print(f"is there {substring} in the sentence ? {check}")

word= len("python")
value = float(word)
print(f"the value in float is {value}")
value_1 = str (word)
print(f"the value in string is {value_1}")

n= int(input("enter a number"))
if n % 2 == 0: 
    print(f"{n} is even number")
else:
    print(f"{n} is not even number")

n = 7 // 3
print (f"the floor divison of 7 by 3 is {n}")
n_1 = 2.7 
n_2 = int (n_1)
print(f"the int converted value of 2.7 is {n_2}")
if n == n_2:
    print("the value is same")
else:
    print("the value is not same")

n = "10"
n_1 = 10
if type(n)== type(n_1):
    print(f"same type")
else:
    print(f"different type")

n = int (9.8)
if n == 10:
    print("equal")
else:
    print("not equal")

hrs = int (input("enter the hours"))
rate = int (input ("enter the rate per hour"))
pay = hrs * rate
print(f"the weekly earning id {pay}")

yrs = int (input("enter the yrs you have lived"))
live = yrs * 12 * 30 *60 * 60 * 60
print(f"you have lived for {live}")



