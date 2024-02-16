from random import choice


class Rand_operation:
    def __init__(self, num_1, num_2):
        self.__num1 = num_1
        self.__num2 = num_2

    def __rand_oper(self):
        symb = ["*", "-", "+"]
        oper = choice(symb)
        if oper == "*":
            return self.__num1 * self.__num2
        elif oper == "-":
            return self.__num1 - self.__num2
        elif oper == "+":
            return self.__num1 + self.__num2

    def result(self):
        return self.__rand_oper()


num_1 = 23
num_2 = 14
random = Rand_operation(num_1, num_2)
print(random.result())