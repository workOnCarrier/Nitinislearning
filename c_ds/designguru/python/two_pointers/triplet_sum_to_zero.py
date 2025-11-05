class Solution:
  def searchTriplets(self, arr):
    triplets = []
    if len(arr) < 3:
      return triplets
    print(f"\t input:{arr}")
    sarr = sorted(arr)
    print(f"\t sorted:{sarr}")
    for base_index in range(0, len(sarr) - 2):
      if base_index > 0 and sarr[base_index -1] == sarr[base_index]:
        continue
      start = base_index + 1
      end = len(sarr) - 1
      print(f"\t trying {base_index}, start:{start}, end:{end}")
      while start < end:
        if (sarr[base_index] + sarr[start] + sarr[end]) == 0:
          triplets.append([sarr[base_index] , sarr[start] , sarr[end]])
          while start < end and sarr[start] == sarr[start + 1]:
            start += 1
          start += 1
          while start < end and sarr[end -1] == sarr[end]:
            end -= 1
          end -= 1
        elif (sarr[base_index] + sarr[start] + sarr[end]) > 0:
          end -= 1
        else:
          start += 1
    print(f"\t returning:{triplets}")
    return triplets

def run():
  arr = [-3, 0, 1, 2, -1, 1, -2]
  arr = [-1, 0, 1, 2, -1, -4]
  arr = [-1,0,1,2,-1,-4]
  s = Solution()
  result = s.searchTriplets(arr)
  print(f"result:{result}")

if __name__ == "__main__":
  run()