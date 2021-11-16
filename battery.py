import os,sys

def main(arg):
        arg = int(arg)
        ids = ['381b4222-f694-41f0-9685-ff5bb260df2e', '92c14ebc-c2e6-4871-bcf2-02db52777fac']
        command = 'powershell.exe powercfg /s ' + ids[arg]
        os.system(command)


if __name__=="__main__":
    try:
            main(sys.argv[1])
    except:
        print("No args passed")
