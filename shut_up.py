import os,sys

def main(arg):
    arg = int(arg)
    ids = ['48684d4a-8524-4093-8a63-ea7132b79c1c', 'c006d24e-fb7b-4bae-a2f7-80bd94a22f4d']
    command = 'powershell.exe powercfg /s ' + ids[arg]
    os.system(command)



if __name__=="__main__":
    main(sys.argv[1])