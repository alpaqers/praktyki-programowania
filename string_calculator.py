def Add(nums):
    if nums == "":
        return 0

    if ",\n" in nums or "\n," in nums:
        raise ValueError("blad w uzyciu newline")

    format_nums = nums.replace("\n", ",")
    parts = format_nums.split(",")

    try:
        return sum(int(part) for part in parts)
    except ValueError:
        raise ValueError("niepoprawne dane")
    