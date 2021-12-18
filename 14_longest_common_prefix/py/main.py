class Solution(object):
	def longestCommonPrefix(self, strs):
		"""
		:type strs: List[str]
		:rtype: str
		"""
		# second idea to compare min and max str 16ms/13.6MB
		sorted_strs = sorted(strs) 
		min_str, max_str = sorted_strs[0], sorted_strs[-1]
		min_length = len(min_str)
		idx = 0
		result_str = ''
		while idx < min_length:
			if min_str[idx] == max_str[idx]:
				idx = idx + 1
			else:
				break
		result_str = min_str[:idx]
		return result_str
		## second idea to compare min and max str 24ms/13.9MB 
		#min_str, max_str = min(strs), max(strs)
		#min_length = len(min_str)
		#idx = 0
		#result_str = ''
		#while idx < min_length:
		#	if min_str[idx] == max_str[idx]:
		#		idx = idx + 1
		#	else:
		#		break
		#result_str = min_str[:idx]
		#return result_str
		## first idea to compare all strs         28ms/13.6MB
		#first_str = strs[0]
		#result_str = ''
		#for idx, val in enumerate(first_str):
		#	if all([ s.startswith(first_str[:idx+1]) for s in strs]):
		#		result_str = first_str[:idx+1]
		#	else:
		#		break
		#return result_str

#assert Solution().longestCommonPrefix(['flower','flow','flight']) == 'fl'
#assert Solution().longestCommonPrefix(['dog','racecar','car']) == ''
assert Solution().longestCommonPrefix(['c','acc','ccc']) == ''
assert Solution().longestCommonPrefix(['a']) == 'a'