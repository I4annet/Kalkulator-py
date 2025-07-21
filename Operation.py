class operation:
    def sum(self, number_list):
        return sum(number_list)
    
    def minus(self, number_list):
        if not number_list:
            return 0
        result = number_list[0]
        for num in number_list[1:]:
            result -= num
        return result
    
    def multiply(self, number_list):
        result = 1
        for num in number_list:
            result *= num
        return result        
    
    def divide(self, number_list):
        if not number_list or 0 in number_list[1:]:
            return "Error: Division by Zero"
        result = number_list[0]
        for num in number_list[1:]:
            result /= num
        return result
