import multiprocessing

def is_prime(n):
    if n <= 2:
        return True
    else:
        for i in range(3, n // 2 + 1, 2):
            if n % i == 0:
                return True
    return False

def is_prime_parallel(up_to, chunksize=1, num_workers=2):
    """Parallelize the Collatz length calculation."""
    with multiprocessing.Pool(num_workers) as P:
        lengths = P.imap_unordered(
            is_prime, 
            list(range(1, up_to)),
            chunksize=chunksize
        )
        return list(lengths)