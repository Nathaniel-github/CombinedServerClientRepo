import os
from threading import Thread
import random
import string
import ast


# With help from this post (https://stackoverflow.com/questions/2257441/random-string-generation-with-upper-case-letters-and-digits)
def gen_random_string(num: int) -> str:
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=num))


def make_addition(word: str) -> None:
    os.system(f'triecli add {word}')


def make_deletion(word: str) -> bool:
    if 'success' in os.popen(f'triecli delete {word}').read().lower():
        return True
    else:
        return False


def delete_all() -> None:
    os.system('triecli deleteall')


def view_trie() -> list:
    return ast.literal_eval(os.popen(f'triecli view').read())


def view_trie_fast() -> list:
    return ast.literal_eval(os.popen(f'triecli viewfast').read())


def add_list(arr: list) -> None:
    for i in arr:
        make_addition(i)


def delete_list(arr: list) -> bool:
    answer = True
    for i in arr:
        answer = answer and make_deletion(i)
    return answer


def search(val: str) -> bool:
    return 'does' not in os.popen(f'triecli search {val}').read()


def search_list(arr: list) -> bool:
    answer = True
    for i in arr:
        answer = answer and search(i)
    return answer


def test_addition_and_deletion() -> bool:
    words = []
    for _ in range(10):
        words.append(gen_random_string(int(random.random() * 100 + 1)))

    add_list(words)

    v = view_trie()
    vf = view_trie_fast()

    delete_list(words)

    return sorted(v) == sorted(vf) == sorted(words)


def test_delete_all() -> bool:
    words = []
    for _ in range(10):
        words.append(gen_random_string(int(random.random() * 100 + 1)))

    add_list(words)

    os.system('triecli deleteall')

    v = view_trie()
    vf = view_trie_fast()

    return [] == v == vf


def test_search() -> bool:
    words = []
    for _ in range(10):
        words.append(gen_random_string(int(random.random() * 100 + 1)))

    words2 = []
    for _ in range(10):
        wr = gen_random_string(int(random.random() * 100 + 1))
        if wr not in words:
            words2.append(wr)

    add_list(words)

    answer = True
    for i in words2:
        answer = answer and not search(i)

    return search_list(words) and answer


def test_threaded() -> bool:
    words_1 = []
    words_2 = []

    for _ in range(10):
        words_1.append(gen_random_string(int(random.random() * 100 + 1)))

    for _ in range(10):
        words_2.append(gen_random_string(int(random.random() * 100 + 1)))

    all_words = words_1 + words_2

    t1 = Thread(target=add_list, args=(words_1,))
    t2 = Thread(target=add_list, args=(words_2,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    v = view_trie()
    vf = view_trie_fast()

    return sorted(v) == sorted(vf) == sorted(all_words)


if __name__ == '__main__':
    delete_all()
    if test_threaded():
        print("Passed threaded test")
    else:
        print("Failed threaded test")

    delete_all()
    if test_addition_and_deletion():
        print("Passed addition and deletion test")
    else:
        print("Failed addition and deletion test")

    delete_all()
    if test_delete_all():
        print("Passed delete all test")
    else:
        print("Failed delete all test")

    delete_all()
    if test_search():
        print("Passed search test")
    else:
        print("Failed search test")

    delete_all()
