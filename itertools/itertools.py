import itertools


def main() -> None:

    # for i in itertools.count(10, 4):
    #     print(i)
    #     if i >= 15:
    #         break

    # for i in itertools.repeat(10, 5):
    #     print(i)

    # for i in itertools.accumulate(range(1, 10)):
    #     print(i)

    # items = ["a", "b", "c"]
    # perms = itertools.permutations(items)
    # for perm in perms:
    #     print(perm)

    items =  ["a", "b", "c"]
    more_items = ["d", "e", "f"]
    print(list(itertools.chain(items, more_items)))

    print(list(itertools.filterfalse(lambda x: x % 2 == 0, range(10))))

    print(list(itertools.takewhile(lambda x: x % 2 != 0, range(10))))

    print(list(itertools.starmap(lambda x, y: x * y, [(2, 6), (8, 4), (5, 3)])))
    
if __name__ == "__main__":
    main()