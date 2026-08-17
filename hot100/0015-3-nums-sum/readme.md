# 三数和(双指针)
为了避免我的O(n^^3)的超大时间复杂度，我这里运用双指针。
## 整体思路
我这里先进行排序，对i进行遍历，然后对left和right设为双指针，如果总和小于0，这里left+=1,总和大于0，right-=1。<br>
这样我的时间复杂度是O(n^^2).
## 去重思路
因为我需要去重的结构是列表，不能设为hash查找。<br>
那我应该怎么优化呢，这里用while,<br>
while left < right and nums[left] == nums[left+1]:<br>
    left += 1<br>
while left < right and nums[right] == nums[right-1]:<br>
    right -= 1<br>
跳过所有重复的数据，当我的sum_nums == 0。
  
