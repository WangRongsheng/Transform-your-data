import os
def ListFilesToTxt(dir,file,wildcard,recursion):
    exts = wildcard.split(" ")
    files = os.listdir(dir)
    for name in files:
        fullname=os.path.join(dir,name)
        if(os.path.isdir(fullname) & recursion):
            ListFilesToTxt(fullname,file,wildcard,recursion)
        else:
            for ext in exts:
                if(name.endswith(ext)):
                    file.write(name + "\n")
                    break
def Test():
    dir="train/annotation"
    outfile="file_list.txt"
    wildcard = ".xml"

    file = open(outfile,"w")
    if not file:
        print ("cannot open the file %s for writing" % outfile)
    ListFilesToTxt(dir,file,wildcard, 1)
    file.close()
Test()
