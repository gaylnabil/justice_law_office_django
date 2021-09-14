from hashlib import sha256
import time
MAX_NONCE = 10_000_000_000


def hash256(text):
    return sha256(text.encode("ascii")).hexdigest()


def mine(block_number, transactions, preview_hash, prefix_zeros):
    prefix_str = '0' * prefix_zeros
    for nonce in range(MAX_NONCE):
        text = str(block_number) + transactions + \
            preview_hash + str(nonce)
        new_hash = hash256(text)
        if new_hash.startswith(prefix_str):
            print(f"number of loop: {nonce}")
            return new_hash
    raise Exception(
        f"Couldn't find correct hash after trying {MAX_NONCE} times")


if __name__ == "__main__":
    transactions = '''
    Nabil->Hicham->30,
    Meriem->Soukaina->60,
    '''
    difficulty = 20
    print('Start Mining ...')
    start = time.time()
    print('New Hash:', mine(5, transactions, '', difficulty))

    time = str(time.time() - start)
    print(f"Time : {time}")
