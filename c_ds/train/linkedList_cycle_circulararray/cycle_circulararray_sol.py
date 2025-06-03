class Solution:
  def loopExists(self, arr):
    for i in range(len(arr)):
      is_forward = arr[i] >= 0  # if we are moving forward or not
      slow, fast = i, i

      # if slow or fast becomes '-1' this means we can't find cycle for this number
      while True:
        # move one step for slow pointer
        slow = self.find_next_index(arr, is_forward, slow, 'slow')
        # move one step for fast pointer
        fast = self.find_next_index(arr, is_forward, fast, 'fast')
        if (fast != -1):
          # move another step for fast pointer
          fast = self.find_next_index(arr, is_forward, fast, 'fast 2')
        if slow == -1 or fast == -1 or slow == fast:
          break

      if slow != -1 and slow == fast:
        return True

    return False


  def find_next_index(self, arr, is_forward, current_index, tag = ''):
    direction = arr[current_index] >= 0

    if is_forward != direction:
      return -1  # change in direction, return -1

    next_index = (current_index + arr[current_index]) % len(arr)
    print(f" {tag} {direction} new offset -- old offset {next_index}: {current_index} ({arr[current_index]})")

    # one element cycle, return -1
    if next_index == current_index:
      next_index = -1

    return next_index


def main():
  sol = Solution()
  # print(sol.loopExists([1, 2, -1, 2, 2]))
  print(sol.loopExists([2, 2, -1, 2]))
  # print(sol.loopExists([2, 1, -1, -2]))


main()
