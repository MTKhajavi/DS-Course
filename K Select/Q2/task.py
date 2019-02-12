def find_kth(array, k, subset_size=7):
    if len(array) <= 10:
        array.sort()
        return array[k]
    subsets = []
    num_medians = len(array) // subset_size
    if (len(array) % subset_size) > 0:
        num_medians += 1
    for i in range(num_medians):
        beg = i * subset_size
        end = min(len(array), beg + subset_size)
        subset = array[beg:end]
        subsets.append(subset)
    medians = []
    for subset in subsets:
        median = find_kth(subset, len(subset) // 2)
        medians.append(median)
    median_of_medians = find_kth(medians, len(medians) // 2)
    pivot = median_of_medians  # pivot point value (not index)
    array_lt = []
    array_gt = []
    array_eq = []
    for item in array:
        if item < pivot:
            array_lt.append(item)
        elif item > pivot:
            array_gt.append(item)
        else:
            array_eq.append(item)
    if k < len(array_lt):
        return find_kth(array_lt, k)
    elif k < len(array_lt) + len(array_eq):
        return array_eq[0]
    else:
        normalized_k = k - (len(array_lt) + len(array_eq))
        return find_kth(array_gt, normalized_k)
