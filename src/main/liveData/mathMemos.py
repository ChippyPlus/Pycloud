class MathMemos:
    def __init__(self):
        """
        format for liveData
        {
            "name" example - "add", // name of an operation type
            "form" example - "10+20", // operation in the simplest form
            "answer": example - 30 // result of the operation
        }
        """
        self.memos = {}


MathMemo = MathMemos()
