class Solution(object):
	def romanToInt(self, s):
		"""
		:type s: str
		:rtype: int
		"""
		result = 0
		roman_dict = {
			'I': 1, 'V': 5,
			'X': 10, 'L': 50,
			'C': 100, 'D': 500,
			'M': 1000}

		## implement by while loop  40ms/13.4MB
		#idx = 0
		#while idx < len(s):
		#	if idx < len(s) - 1 and\
		#		roman_dict[s[idx]] < roman_dict[s[idx+1]]:
		#		result = result + roman_dict[s[idx+1]] - roman_dict[s[idx]]
		#		idx = idx + 1
		#	else:
		#		result = result + roman_dict[s[idx]]
		#	idx = idx + 1
		#return result
		# implement by for loop   36ms/13.5MB
		is_skip = False		
		for idx, val in enumerate(s):
			if not is_skip:
				# if next digit larger than current digit
				# then add next digit and minus current digit
				if idx < len(s) - 1 and\
					roman_dict[s[idx]] < roman_dict[s[idx+1]]:
					result = result + roman_dict[s[idx+1]] - roman_dict[s[idx]]
					is_skip = True
				else:
					result = result + roman_dict[s[idx]]
			else:
				is_skip = False
		return result

assert Solution().romanToInt('III') == 3
assert Solution().romanToInt('LVIII') == 58
assert Solution().romanToInt('MCMXCIV') == 1994