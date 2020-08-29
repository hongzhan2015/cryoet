import os, re
def main():
	angledict = {
	"-60.0": "01", 
	"-57.0": "02", 
	"-54.0": "03", 
	"-51.0": "04", 
	"-48.0": "05", 
	"-45.0": "06", 
	"-42.0": "07",
	"-39.0": "08",
	"-36.0": "09",
	"-33.0": "10",
	"-30.0": "11",
	"-27.0": "12",
	"-24.0": "13",
	"-21.0": "14",
	"-18.0": "15",
	"-15.0": "16",
	"-12.0": "17",
	"-9.0": "18",
	"-6.0": "19",
	"-3.0": "20",
	"-0.0": "21",
	"0.0": "21",
	"60.0": "41",
	"57.0": "40",
	"54.0": "39",
	"51.0": "38",
	"48.0": "37",
	"45.0": "36",
	"42.0": "35",
	"39.0": "34",
	"36.0": "33",
	"33.0": "32",
	"30.0": "31",
	"27.0": "30",
	"24.0": "29",
	"21.0": "28",
	"18.0": "27",
	"15.0": "26",
	"12.0": "25",
	"9.0": "24",
	"6.0": "23",
	"3.0": "22"}
	path = os.getcwd()
	dst=[]
	for filename in os.listdir(path):
		if filename.endswith("_0.mrc"):
			tilt = re.search("[-+]?\d*\.\d+\w", filename)
			angle = tilt.group(0)[:-1]
			angular = angledict[angle]
			dst = angular + ".mrc"
			os.rename(filename, dst)

if __name__ == '__main__':
     
    # Calling main() function
    main()