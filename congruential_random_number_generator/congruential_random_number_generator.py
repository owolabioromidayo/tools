import sys

def gen_number(seed, a, c, m): #a,c are less than m
    seed = (a*seed + c)%m
    
    with open('seed.txt','w') as f:
        f.write(str(seed))

    print(seed/m)

if __name__ == "__main__":
    seed = 0
    with open('seed.txt','r') as f:
        seed = int(f.readlines()[0])
    gen_number(seed,24539, 24938, 5539583)
    
