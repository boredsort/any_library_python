from dataclasses import dataclass, asdict, astuple
import inspect


@dataclass(frozen=True, order=True)
class Comment:
    id: int
    text: str


def main():
    comment = Comment(1, "I subscribed")
    print(comment)
    print(asdict(comment))
    print(inspect.getmembers(comment))


if __name__ == '__main__':
    main()