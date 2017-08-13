def convert_from_decimal_to_binary(number,base):
	multiplier,result =1,0
	while number>0:
		result += number%base*multiplier
		multiplier*=10
		number = number//base
	return result
def test_convert_from_decimal_to_binary(number,base):
	number,base = 9,2
	assert(convert_from_decimal_to_binary(number, base)==1001)
if __name__ == '__main__':
	test_convert_from_decimal_to_binary(9,2)