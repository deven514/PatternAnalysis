def getStringFromFile(path):
    file = open(path, "r")
    content = file.read()
    file.close()
    return content


def getPatternStringFromFile(path):
    file = open(path, "r")
    pattern = file.readline()
    genome = file.readline()
    file.close()
    return pattern, genome

def setToFile(path, content):
    file = open(path, "w")
    file.write(content)
    file.close()