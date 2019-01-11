from IndexSet import IndexSet


def create_unique_index_set(size, dim):
    s = []
    x = IndexSet(size, dim)
    s.append(x.get_sorted_tuple())
    while True:
        if x.next():
            s.append(x.get_sorted_tuple())
        else:
            break
    return list(set(s))


def sum_given_size(x, size):
    r = []
    dim = len(x)
    s = create_unique_index_set(size, dim)
    for e in s:
        r.append(sum([x[i] for i in e]))
    return r


def sum_all_sizes(x):
    r = []
    for size in range(1, len(x) + 1):
        r += sum_given_size(x, size)
    return r


def sum_all_sizes_no_duplicates_sorted(x):
    r = sum_all_sizes(x)
    r = list(set(r))
    r.sort()
    return r


y = [1, 3, 5]
print(sum_all_sizes_no_duplicates_sorted(y))





