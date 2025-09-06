
class calculators:
    def __init__(self):
        self.calculator = []
    
    def add_cal(self, number):

        self.calculator.append(number)

    def sum_cal(self):
        i = sum(self.calculator)
        return i 
    
    def minus_cal(self):
        result = self.calculator[0]
        for num in self.calculator[1:]:
            result -= num
        return result


    def multi_cal(self):
        i = 1
        for j in self.calculator:
            i *= j
        return i
    
    def div_cal(self):
        result = self.calculator[0]
        for num in self.calculator[1:]:
            if num == 0:
                return "Division by zero!"
            result /= num
        return result

