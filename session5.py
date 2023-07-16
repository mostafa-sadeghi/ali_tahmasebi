# a = 4
# b = 4
#
# if a == b:
#     print("a and b are equal")
#
# if a != b:
#     print("a and b are not equal")
#
# if a > b:
#     print("a is greater than b")
#
# if a < b:
#     print("a is less than b")
#
# if a >= b:
#     print("a is greater than or equal to b")
#
# if a <= b:
#     print("a is less than or equal to b")



number1 = int(input("enter first number: "))
number2 = int(input("enter second number: "))

if number1 == number2:
    print("number1 and number2 are equal")
    print(f"{number1} = {number2}")
elif number1 > number2:
    print("number1 is greater than number2")
    print(f"{number1} > {number2}")
else:
    print("number2 is greater than number1")
    print(f"{number2} > {number1}")

# TODO   برنامه ای بنویسی که نمرات سه درس یک دانش آموز را از ورودی دریافت نماید
# و معدل او را محاسبه کند
# معدل یعنی جمع سه نمره تقسیم بر سه
# اگر معدل از 19 بیشتر بود، A را پرینت نماید
# اگر معدل از 18 بیشتر بود B را پرینت نماید
# اگر معدل از 17 بیشتر بود C را پرینت نماید
# در غیر اینصورت D را پرینت نماید