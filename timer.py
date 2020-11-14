import os,sys,datetime,time
mins = int(sys.argv[1])
secs = int(sys.argv[2]) 

print("Timer has begun!")
time.sleep(1)

count = [0,0]
for i in range(60*mins + secs):
    os.system("clear")

    if count[1] < 10:
        print(f"{count[0]} : 0{count[1]}")
    else:
        print(f"{count[0]} : {count[1]}") 

    if count[1] == 59:
        count[0] += 1 ; count[1] = 0
    else:
        count[1] += 1

    time.sleep(1)
        
print(f"Time's Up")

