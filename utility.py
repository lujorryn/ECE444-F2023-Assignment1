class utils:
    def reversed(num) -> int:
        if type(num) is not int:
            return "Error. Input is not an integer."
        
        r_num = 0
        negative = 1
        if num < 0:
            negative = -1
            num = abs(num)
        
        while(num != 0):
            r_num *= 10
            r_num += num % 10
            num = num // 10
        
        return r_num * negative

    def formatter(num) -> str:
        # Output string format to account for both positive and negative integers
        if type(num) is not int:
            return "Error. Input is not an integer."
        
        negative = "+"
        if num < 0:
            negative = "-"
            num = abs(num)

        if num == 0:
            return "0", "0"

        # calculate binary
        tmp = num
        binary = str()
        while(tmp != 0):
            binary = str(tmp % 2) + binary
            tmp = tmp // 2
        
        # calculate octal
        tmp = num
        octal = str()
        while(tmp != 0):
            octal = str(tmp % 8) + octal
            tmp = tmp // 8

        return negative + binary, negative + octal