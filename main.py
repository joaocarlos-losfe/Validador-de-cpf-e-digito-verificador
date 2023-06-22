import re

CPF_REGEX = re.compile(r"\d{3}\.\d{3}\.\d{3}\-\d{2}")

def validate_cpf(cpf: str) -> bool:
    if not re.compile(CPF_REGEX).match(cpf):
        return False
    
    digits_numbers = [ int(digit) for digit in cpf if digit.isdigit() ]

    #verify first digit
    sum_of_digits = sum( a*b  for a,b in zip( digits_numbers[0:9], range(10, 1, -1) ) )
    expected = ( (sum_of_digits * 10) % 11 ) % 10
    if digits_numbers[9] != expected:
        return False
    
    #verify second digit
    sum_of_digits = sum( a*b  for a,b in zip( digits_numbers[0:10], range(11, 1, -1) ) )
    expected = ( (sum_of_digits * 10) % 11 ) % 10
    if digits_numbers[10] != expected:
        return False
    
    return True

if __name__=="__main__":
    CPF = "033.000.000-00"

    if not validate_cpf(CPF):
        print("cpf invalido")
    else:
        print("cpf valido")
