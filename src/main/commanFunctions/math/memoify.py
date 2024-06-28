from src.main.liveData.mathMemos import MathMemo
from time import ctime


def memoize(func):
    def wrapper(*args):
        MemoArgs = (args[0], args[1]["arg1"], args[1]["arg2"],args[2])  # Keeps it as a hashed type. If it wasn't hashed it
        # couldn't be used as a key, then to convert it into a usable format.
        if MemoArgs not in MathMemo.memos:
            with open("logs/memos.log", "a") as f:
                f.write(f"{ctime()} [MATH] created, | {args[:2]}\n")
            out = func(*args)  # Only run the func if not memo
            MathMemo.memos[MemoArgs] = out
            return out  # acts as an if, else statement without the else.
        with open("logs/memos.log", "a") as f:
            f.write(f"{ctime()} [MATH] read, | {args[:2]}\n")
        return MathMemo.memos[MemoArgs]

    return wrapper
