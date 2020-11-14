import os, sys



def run(playlist_id, path, del_order=False ):
    os.chdir(path)
    os.system(f" youtube-dl --get-filename {playlist_id} -o \"%(title)s.mp4\" > order.txt")
    print("order.txt done")

    with open('order.txt', 'r') as file_:
        f = [line.strip() for line in file_.readlines()]
        

    if del_order == True:
        os.remove("order.txt")  

    for _, filename in enumerate(os.listdir(".")): 
        try:
            idx = f.index(filename) + 1
            dst = str(idx) + '. ' + filename
            os.rename(filename, dst)
            print('Done ', idx)
        except Exception as e:
            continue
 


def remove_ids(path):
    os.chdir(path)

    for _, filename in enumerate(os.listdir(".")): 
        try:
            dst = filename.split('-')[0] + '.mp4'
            print(dst)

            # os.rename(filename, dst)
            print('Done ', idx)
        except Exception as e:
            continue




if __name__ == "__main__":
    # run('PLkDaE6sCZn6Ec-XTbcX1uRg2_u4xOEky0', '/mnt/c/Users/Oromidayo/Desktop/1') EXAMPLE
