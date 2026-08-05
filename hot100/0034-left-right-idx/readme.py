二分查找，找第一个大于等于target元素的idx模板
要点1：左边不用变，右边的话+1搜索以后-1
要点2：if left_idx > right_idx:
          return [-1,-1]
这个是准确判断这个找不到的情况（left_idx = right_idx-1）
