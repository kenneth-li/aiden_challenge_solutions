import random


def rand_array(n, limit):
    result = []
    i = 0
    while i < n:
        new_int = random.randrange(limit)
        if new_int not in result:
            result.append(new_int)
            i += 1
    return result


def bucket_sum(buckets, target):
    bucket_matrix = [0] * (target + 1)
    for i in range(target + 1):
        for bucket in buckets:
            if i == bucket or (bucket <= i and bucket_matrix[i - bucket] == 1):
                bucket_matrix[i] = 1
    return bucket_matrix[target]

print(bucket_sum([3, 11, 21], 492))
