import sys

printDebugs = True

def filterArgs():
    if(printDebugs): print("[filterArgs]")
    fields = []
    delimiter = "\t"
    fileName = sys.argv[-1]

    for arg in sys.argv:
        if('-f' in arg):
            fields = getFieldsToCut(arg)
        if('-d' in arg):
            delimiter = arg.split("-d")[1]
    # if fileName == fields or fileName == delimiter:
    #     fileName = ''
    return [fields,delimiter,fileName]

def getFieldsFromFile(fileName,fields,delimiter):
    if(printDebugs): print("[getFieldsFromFile]")
    
    res = ""

    with open(fileName) as file:
        for lines in file:
            line = lines.split(delimiter)
            for field in fields:
                res += line[int(field) - 1] + delimiter
            res += "\n"
    
    print(res)
    return

def getFieldsFromStdIn(fileName,fields,delimiter):
    if(printDebugs): print("[getFieldsFromStdIn]")

def main():
    fields,delimiter,fileName = filterArgs()
    fileNameProvided = True
    
    if fields == [] or len(fields) == 1 and fields[0] == '':
        print("[ERROR] Invalid Arguments: Incorrect or missing fields argument")
        return
    # if fileName == delimiter or fileName == fields or fileName == '' or fileName == '-':
    #     fileNameProvided = False
    #     print("fileName = empty")
    #     fileName = sys.stdin
    # elif fileName == sys.argv[0] or '.' not in fileName:
    #     print("[ERROR] Invalid Arguments: Incorrect Filename provided")
    #     return
    
    # for field in fields:
    #     print("Listing fields: " + str(field))
    # print("Delimiter = " + delimiter)
    # print("FileName = " + fileName)
    if(fileNameProvided): getFieldsFromFile(fileName,fields,delimiter)
    else: getFieldsFromStdIn(fileName,fields,delimiter)
    
            
def getFieldsToCut(x):
    if(printDebugs): print("[getFieldsToCut]")
    x = x.split("-f")
    x = x[1]
    if(" " in x):
        x = x.split(" ")
    else:
        x = x.split(",")
    return x        
    
if __name__ == "__main__":
    main()