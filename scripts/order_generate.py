import os, re, sys

def createList(numbers):
    return list(range(numbers+1))

def main(group = int(3), increment = int(3), max_pos_angle = int(54), min_neg_angle = int(-54), scheme = "pos"):
    path = os.getcwd()
    for filename in os.listdir(path):
        if filename.endswith(".tlt"):
           tiltname = filename.split(".")[0]
           extension = ".order"
           ordername = tiltname + extension
           tiltfile = open(filename, 'r').read().splitlines()
           num_angles = int(abs(max_pos_angle - min_neg_angle)/increment)
           num_group = int(num_angles/group)
           reorderlist = createList(num_angles)
            ## create an empty angle dictionary ##
           angle_dic = dict.fromkeys(reorderlist)
           zero_tilt = tiltfile[int(num_angles/2)]
           angle_dic[0] = zero_tilt

            ## assign value to key ##
           for cluster in range(num_group):
               if (cluster % 2) == 0:
                   for i in range(1,increment+1):
                       factor_1 = int((cluster/2)*(group+increment))
                       factor_2 = int((cluster/2)*group)
                       index = int(int(num_angles/2) + factor_2 + i)
                       angle_dic[factor_1 + i] = tiltfile[index]
               else:
                   for j in range(1,increment+1):
                       factor_1 = int(((cluster -1)/2)*(group+increment))
                       factor_2 = int(((cluster-1)/2)*group)
                       index = int(int(num_angles/2) - factor_2 -j)
                       angle_dic[factor_1 + group + j] = tiltfile[index]

           reorderline = []
           for key, value in angle_dic.items():
               reorderline.append(value)

           reorderfile = open(ordername, 'w') 
           for lines in reorderline:
               reorderfile.writelines(lines + "\n")
           reorderfile.close()
			
			
if __name__ == '__main__':
     
    # Calling main() function
    main()