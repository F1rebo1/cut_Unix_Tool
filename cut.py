import sys

printDebugs = True

def filterArgs():
    if(printDebugs): print("[filterArgs]")
    fields = []
    delimiter = "\t"
    fileName = ''
    fieldsFound,delimiterFound = False,False

    for arg in sys.argv:
        if('-f' in arg and not fieldsFound):
            fields = getFieldsToCut(arg)
            fieldsFound = True
        elif('-d' in arg and not delimiterFound):
            delimiter = arg.split("-d")[1]
            delimiterFound = True
        elif(fieldsFound and delimiterFound):
            fileName = arg
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

    res = ""

    for lines in sys.stdin:
        line = lines.split(delimiter)
        for field in fields:
            res += line[int(field) - 1] + delimiter
        res += "\n"

    print(res)
    return

def main():
    fields,delimiter,fileName = filterArgs()
    fileNameProvided = True
    
    if fields == [] or len(fields) == 1 and fields[0] == '':
        print("[ERROR] Invalid Arguments: Incorrect or missing fields argument")
        return
    if fileName == '' or fileName == '-':
        fileNameProvided = False
        print("fileName = empty")
        fileName = '-'
    elif fileName == sys.argv[0] or '.' not in fileName:
        print("[ERROR] Invalid Arguments: Incorrect Filename provided")
        return
    
    for field in fields:
        print("Listing fields: " + str(field))
    print("Delimiter = " + delimiter)
    print("FileName = " + fileName)
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