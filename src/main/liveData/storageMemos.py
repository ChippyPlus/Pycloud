class StorageMemos:
    def __init__(self):
        """
        format for liveData
        {
            "form" example - (), // operation in the simplest form
            "answer": example - 30 // result of the operation
        }
        """
        self.memos = dict()


StorageMemo = StorageMemos()