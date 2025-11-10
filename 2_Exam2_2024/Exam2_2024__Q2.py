def parse_boxing_match(match_result):
	
	numDigit = int(len(match_result[2::])/2)
	
	mode = match_result[0:2]
	match_result = match_result[2::]
	
	num1 = [int(e) for e in match_result[0:numDigit].split()]
	num2 = [int(e) for e in match_result[numDigit:].split()]
	
	if mode == "RB": return [num1, num2]
	else: pass
	
	return [num2, num1]

def calculate_round_points(r_knockdown, b_knockdown):
	r_point, b_point = [], []
	
	for e in r_knockdown: r_point.append(10-e)
	for e in b_knockdown: b_point.append(10-e)
	
	return r_point, b_point

def show_match_result(red_point, blue_point):
	output = ""
	result = ""
	
	for i in range(0, len(red_point)):
		if red_point[i] > blue_point[i]: output += "R"
		elif red_point[i] < blue_point[i]: output += "B"
		else: output += "T"
	
	redSumPoint = sum(red_point)
	blueSumPoint = sum(blue_point)
	
	if redSumPoint > blueSumPoint: result = "Red"
	if blueSumPoint > redSumPoint: result = "Blue"
	if redSumPoint == blueSumPoint: result = "Draw"
	
	print(output)
	print(f"{redSumPoint} {blueSumPoint}")
	print(result)
	
	return

exec(input().strip())