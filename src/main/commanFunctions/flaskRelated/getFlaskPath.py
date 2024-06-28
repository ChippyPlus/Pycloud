import os


def untilFinalPath(file, finalDirName="routes"):
    currentPath = os.path.dirname(file)
    while currentPath != os.path.dirname(currentPath):
        based = os.path.basename(currentPath)
        yield based
        currentPath = currentPath[: currentPath.rfind('/')]
        if based == finalDirName:
            del based
            break


def buildRoutes(finalDirName="routes", file=__file__):
    out = [i for i in untilFinalPath(file, finalDirName=finalDirName)][:-1]
    out.reverse()
    return f"/{'/'.join(out)}/{os.path.basename(file).removesuffix('.py')}"
