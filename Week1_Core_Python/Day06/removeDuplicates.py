


def removeDuplicates(nums: list) -> list:
    setNums = set()
    for n in nums:
        setNums.add(n)
    return list(setNums)


if __name__ == "__main__":
    nums = [1, 2, 3, 4, 4, 5, 5, 5, 6, 6, 9]
    print(f"Initial list: {nums}")

    ans = removeDuplicates(nums)
    print(f"After removing duplicates: {ans}")

