class Solution:
  def splitNum(self, num: int) -> int:
    num_arr = sorted(list(str(num)))
    print(num_arr)
    num_arr1 = []
    num_arr2 = []
    for i in range(len(num_arr)):
      if i % 2 == 0:
        num_arr1.append(num_arr[i])
      else:
        num_arr2.append(num_arr[i])
    num1 = 0
    num2 = 0
    for i in range(len(num_arr1)):
      num1 = num1 * 10 + int(num_arr1[i])
    for i in range(len(num_arr2)):
      num2 = num2 * 10 + int(num_arr2[i])
    print(num1, num2)
    return num1 + num2

s = Solution()
print(s.splitNum(5748632))
