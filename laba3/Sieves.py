class Sieves:
    @staticmethod
    def aliquot(sequence, number):
        newSequence = []
        for element in sequence:
            if element % number == 0:
                newSequence.append(element)
        return newSequence

    @staticmethod
    def Eratosfen(sequence):
        newSequence = sequence
        subtractionParameter = 0
        checked = []
        while True:
            found = False
            for item in newSequence:
                if item > subtractionParameter:
                    subtractionParameter = item
                    found = True
                    break
            if not found:
                break
            substractSequence = Sieves.aliquot(newSequence, subtractionParameter)
            newSequence = list(set(newSequence) - set(substractSequence))
            newSequence.append(subtractionParameter)
            checked.append(subtractionParameter)
        return newSequence


