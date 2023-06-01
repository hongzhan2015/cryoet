import os, os.path, shutil
def main():
	path = os.getcwd()
	folder_name = []
	new_path = []
	src = []
	dst = []
	for files in os.listdir(path):
		if files.endswith(".mrc"):
				folder_name = files.split("_")[2]
				#print(folder_name)
				new_path = os.path.join(path, folder_name)
				#print(new_path)
				src = os.path.join(path, files)
				dst = os.path.join(new_path, files)
				if not os.path.exists(new_path):
					os.makedirs(new_path)
				shutil.move(src, dst)
        		#print(files)

if __name__ == '__main__':
	main()