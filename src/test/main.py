import os


def untilFinalPath(finalDirName="routes"):
    currentPath = os.path.dirname(__file__)
    while currentPath != os.path.dirname(currentPath):
        based = os.path.basename(currentPath)
        yield based
        currentPath = currentPath[: currentPath.rfind('/')]
        if based == finalDirName:
            del based
            break


def buildRoutes(finalDirName="routes"):
    out = [i for i in untilFinalPath(finalDirName)]
    out.reverse()
    return f"/{'/'.join(out)}/{os.path.basename(__file__).removesuffix('.py')}"


buildRoutes("python")
