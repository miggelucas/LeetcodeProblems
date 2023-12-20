#
# @lc app=leetcode id=412 lang=python3
#
# [412] Fizz Buzz
#

# @lc code=start
class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        result: [str] = []
        
        for number in range(1, n + 1):
            if number % 3 == 0 and number % 5 == 0:
                result += ["FizzBuzz"]

            else:
                if number % 3 == 0:
                    result += ["Fizz"]
                
                elif number % 5 == 0:
                    result += ["Buzz"]
                
                else:
                    result += [str(number)]
        
        return result

        
        
        
# @lc code=end
