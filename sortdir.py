import os, os.path
def main():
	path = os.getcwd()
	folder_name = []
	new_path = []
	for i in os.listdir(path):
		if i.endswith(".tif"):
			folder_name = i.split("_")[0]
    		new_path.append(os.path.join(path, folder_name))
    		for f in new_path:
    			if not os.path.exists(os.path.join(path, f)):
        			os.makedirs(f)


if __name__ == '__main__':
	main()