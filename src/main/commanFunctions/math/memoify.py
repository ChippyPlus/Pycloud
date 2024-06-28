from src.main.liveData.mathMemos import MathMemo
from time import localtime
from time import ctime
def memoize(func):
    def wrapper(*args):

        MemoArgs = (args[0], args[1]["arg1"], args[1]["arg2"])
        if MemoArgs not in MathMemo.memos:
            with open("logs/memos.log", "a") as f:
                f.write(f"{ctime()} [MATH] created, | {args}\n")
            out = func(*args)
            MathMemo.memos[MemoArgs] = out
            return out
        with open("logs/memos.log", "a") as f:
            f.write(f"{ctime()} [MATH] read, | {args}\n")
        return MathMemo.memos[MemoArgs]

    return wrapper
