import os,sys,time, datetime



def main():
    word_count = 0
    lines = []
    output_file = sys.argv[1]
    start = datetime.datetime.now()

    while True:
        os.system("clear")

        curr = datetime.datetime.now()
        print(f"{word_count} words \t\t\t\t Time:{str(curr-start)[2:-7]}")
        for line in lines: print(line)
        user_input = input()

        if len(user_input) == 0:
                continue
        elif user_input[0] == ":":
            if user_input[1] == "q":
                time_str = str(curr-start)[2:-7]
                time_min = int(time_str[:2]) + int(time_str[3:])/60 #time in minutes
                print(f" Wordcount: {word_count}, Time: {str(curr-start)[2:-7]}, Avg Speed : {(word_count/time_min)} wpm")
                with open(output_file, 'w') as f:
                    title = input("Title? ")
                    f.write(f"{str(datetime.datetime.now())[:10]} \t\t\t {title} \n\n")
                    for line in lines:
                        f.write(line+"\n")
                input("Ready to Leave?")
                return

        else:
            lines.append(user_input)
            for idx in range(len(user_input) - 1):
                if user_input[idx] not in ' .' and user_input[idx+1] in ' .':
                    word_count += 1
            word_count += 1    
            


if __name__ == "__main__":
    main()
