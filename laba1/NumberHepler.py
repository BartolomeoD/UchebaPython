class NumberHelper:
    def GetOneByOne(number):
        numbers = []
        tempNumber = number
        while tempNumber > 0:
            numbers.append(tempNumber % 10)
            tempNumber = tempNumber // 10
        return numbers
