import argparse
import os 


os.system('python milestone_1.py --file input_1.txt')


def runTask(t):
    os.system('python milestone_1.py --file input_'+t+'.txt')
    lines1My = []
    lines1Test = []
    with open("milestone_1_result.txt", "r") as f:
        for line in f:
            lines1My.append(line)

    with open("input_"+t+"_result.txt", "r") as f:
        for line in f:
            lines1Test.append(line)
    clearN(lines1My)
    clearN(lines1Test)
    output_file = open("test/"+t+"_result.txt", "w+", encoding="utf-8")
    for u in range(len(lines1My)):
        if u < len(lines1Test):
            if lines1My[u] != lines1Test[u]:
                output_file.write(str(u+1)+lines1My[u]+"  ,   "+lines1Test[u]+"\n")
        else:
            output_file.write(lines1My[u]+"  ,   EXTRA\n")


def clearN(f):
    for i in f:
        i = i.replace("\n", "")

for i in range(1,7):
    runTask(str(i))
    


