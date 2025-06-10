from collections import defaultdict

def longest_equal_frequency_subarray(arr):
    n = len(arr)
    low, high = 1, n
    answer = 1

    while low <= high:
        mid = (low + high) // 2
        freq = defaultdict(int)
        count = defaultdict(int)
        valid = False

        # Initialize the first window
        for i in range(mid):
            elem = arr[i]
            if freq[elem] > 0:
                count[freq[elem]] -= 1
                if count[freq[elem]] == 0:
                    del count[freq[elem]]
            freq[elem] += 1
            count[freq[elem]] += 1

        # Check if the first window is valid
        if len(count) == 1:
            key = next(iter(count))
            if key * count[key] == mid:
                valid = True

        # Slide the window
        for i in range(1, n - mid + 1):
            # Remove the outgoing element (left end)
            left_elem = arr[i - 1]
            count[freq[left_elem]] -= 1
            if count[freq[left_elem]] == 0:
                del count[freq[left_elem]]
            freq[left_elem] -= 1
            if freq[left_elem] > 0:
                count[freq[left_elem]] += 1

            # Add the incoming element (right end)
            right_elem = arr[i + mid - 1]
            if freq[right_elem] > 0:
                count[freq[right_elem]] -= 1
                if count[freq[right_elem]] == 0:
                    del count[freq[right_elem]]
            freq[right_elem] += 1
            count[freq[right_elem]] += 1

            # Check validity
            if len(count) == 1:
                key = next(iter(count))
                if key * count[key] == mid:
                    valid = True
                    break

        if valid:
            answer = mid
            low = mid + 1
        else:
            high = mid - 1

    return answer


def max_equal_freq_subarray(arr):
    n = len(arr)
    freq = defaultdict(int)        # element -> frequency
    freq_count = defaultdict(int)  # frequency -> count of elements with this frequency

    left = 0
    max_len = 0
    best_range = (0, 0)

    for right in range(n):
        elem = arr[right]

        # Decrease old frequency count
        if freq[elem] > 0:
            freq_count[freq[elem]] -= 1
            if freq_count[freq[elem]] == 0:
                del freq_count[freq[elem]]

        # Increase new frequency
        freq[elem] += 1
        freq_count[freq[elem]] += 1

        # Try shrinking left if needed to restore valid state
        while left <= right:
            window_len = right - left + 1
            if len(freq_count) == 1:
                # All frequencies are the same
                freq_val = next(iter(freq_count))
                if freq_val * len(freq) == window_len:
                    if window_len > max_len:
                        max_len = window_len
                        best_range = (left, right)
                    break
            else:
                # Not valid, shrink from the left
                le = arr[left]
                freq_count[freq[le]] -= 1
                if freq_count[freq[le]] == 0:
                    del freq_count[freq[le]]

                freq[le] -= 1
                if freq[le] > 0:
                    freq_count[freq[le]] += 1
                else:
                    del freq[le]
                left += 1

    return max_len, best_range


def run_tests():
    test_cases = [
        ([1, 2, 2, 1, 2, 1, 3, 3, 3], "Mix of balanced and unbalanced"),
        ([1, 1, 1, 1], "All same elements"),
        ([1, 2, 3, 4], "All unique elements"),
        ([1, 2, 1, 2, 3, 3], "Balanced at end"),
        ([1, 2, 2, 1, 3, 3, 3, 4, 4, 4], "Triples of 3s and 4s"),
        ([1], "Single element"),
        ([1, 2, 1, 3, 3, 2], "Scattered equal frequencies")
    ]

    for i, (arr, desc) in enumerate(test_cases):
        length, (start, end) = max_equal_freq_subarray(arr)
        print(f"Test {i+1}: {desc}", end = "||")
        print(f"  Input: {arr}", end = " ||")
        print(f"  Max Equal Freq Subarray: Length = {length}, Indices = [{start}, {end}], Subarray = {arr[start:end+1]}")
        length = longest_equal_frequency_subarray(arr)
        print(f"Test {i+1}: {desc}", end = "||")
        print(f"  Input: {arr}", end = " ||")
        print(f"  Max Equal Freq Subarray: Length = {length} \n")

run_tests()
