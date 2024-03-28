import sys
import argparse

printDebugs = True

def filterArgs():
    fields = []
    delimiter = "\t"
    fileName = sys.argv[-1]

    for arg in sys.argv:
        if('-f' in arg):
            fields = getFieldsToCut(arg)
        if('-d' in arg):
            delimiter = arg.split("-d")[1]
    return [fields,delimiter,fileName]

def main():
    fields,delimiter,fileName = filterArgs()
    if fields == [] or len(fields) == 1 and fields[0] == '':
        print("[ERROR] Invalid Arguments: Incorrect or missing fields argument")
        return
    if fileName == sys.argv[0] or '.' not in fileName:
        print("[ERROR] Invalid Arguments: Incorrect Filename provided")
        return
    for field in fields:
        print("Listing fields: " + str(field))
    print("Delimiter = " + delimiter)
    print("FileName = " + fileName)
    
            
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