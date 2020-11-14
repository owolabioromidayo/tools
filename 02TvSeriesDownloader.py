import requests, os, sys
from string import Template

def download_video_series(video_links):
  
    for link in video_links:

        #Filenaming
        file_name = link.split('/')[-1]
        file_name = file_name.replace('%20',' ')
  
        #File Download Initiation
        print(f"Downloading file:{file_name}")
          
        # create response object 
        r = requests.get(link, stream = True) 
          
        # download started 
        with open(file_name, 'wb') as f: 
            for chunk in r.iter_content(chunk_size = 1024*1024): 
                if chunk: 
                    f.write(chunk) 
          
        #File Download Completion        
        print(f"{file_name} downloaded!\n")
  
    print("All videos downloaded!")
    return


def videolist(link, end, start=1):
    link = Template(link)
    video_list = []

    #Number generation in the range of episode start to end
    ls = [str(item) for item in list(range(start,end+1))] 
    #Link generation
    for idx, item in enumerate(ls):
        if len(item) == 1:
            ls[idx] = '0'+ item
            
        #Templates episode numbers into link and addds to DL list
        video_list.append(link.substitute(num=ls[idx])) 
        print(video_list[idx])

    return video_list


def collect_requests():
    """ Collects all download requests made by user in loop_script func"""
    requests = []
    while True:

        link = input(' Link E(episode_num) with E$num: ')
        start = int(input('Start: '))
        end = int(input('End: '))

        requests.append((link, start, end)) #Adds new download request

        cont = input('Continue...(y/n) ')
        if cont == 'n':
            print(requests)
            return requests
            

def for_each_request(requests):
    for request in requests:
        #FOLDER GENERATION
        #Folder Naming
        folder_name = request[0].split('/')[-1]
        folder_name = folder_name.replace('%20',' ')
        folder_name = folder_name.split('-')[0].strip()

        #Folder Creation
        os.chdir(f"C:/Users/Hp/Videos")
        if not os.path.exists(folder_name):
            os.makedirs(folder_name)

        #Changes folder directory to created folder
        os.chdir(f"C:/Users/Hp/Videos/{folder_name}")

    #Videolist Creation
    video_links = videolist(request[0],request[2],request[1])
    #Download Into Folder
    download_video_series(video_links)
         

def loop_script():
    while True:
        requests = collect_requests()
        for_each_request(requests)

        x = input("Enter 'exit' to end program, anything else to continue...")
        if x=='exit':
            break


def collect_file_args(filepath):
    """Collects File Text and Converts to Requests."""
    requests = []

    with open(filepath,'r') as file:
        lines = file.readlines()
        
    for line in lines:
        #Converts line to request tuple and adds to requests list
        line = line.replace('\n','')
        line_reqs  = line.split(' ')
        line_reqs[1] = int(line_reqs[1])
        line_reqs[2] = int(line_reqs[2])
        line_reqs = tuple(line_reqs)

        requests.append(line_reqs)
            
    print(requests)
    #Handles request download.
    for_each_request(requests)
        

# collect_file_args('C:/Users/USER/Desktop/requirements.txt')


def use_functions():
    while True:
        print("""
        collect_file_args(filepath) -- To Input Arguments from a file 
        loop_script() -- To Input Arguments in Terminal
        """)
        
        exec(input('Function: '))
       
    

def exit():
    sys.exit()


if __name__ == "__main__":
    use_functions()

