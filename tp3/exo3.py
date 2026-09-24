import argparse


parser = argparse.ArgumentParser(description="Giving back tail/head of a file")

parser.add_argument("-m", "--mode", choices=["head", "tail"], help="Choose wether to show header or footer")
parser.add_argument("-s", "--size", type=int, help="Size of the head/tail to output")
parser.add_argument("-d", "--directory", help="Select the file wanted")

args = parser.parse_args()

try:
    with open(args.directory, "r") as f:
        lines = f.readlines() #list of lines of the whole file
except FileNotFoundError:
    print("Wrong File")
    exit()

if args.mode == "head":
    result = lines[:args.size] #head so it start from top file and goes until the size specified
elif args.mode == "tail":
    result = lines[-args.size:] # -args... bc so it start from the bottom at a said line before the end which is the end ( [-X: ] the start is backward )
else:
    print("No correct argument entered, processed without head/tail")
    
for line in result:
    print(line,end="") #since lines is a list of all lines in the file, it then print them one by one
    