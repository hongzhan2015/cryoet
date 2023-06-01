import numpy as np 
import pandas as pd
import os,sys

def main():
    path =os.getcwd()
    for filename in os.listdir(path):
        if filename.endswith(".tlt"):
            df_var = filename.split('.')[0]

        ## create reading tilt file function ##
            df = pd.read_csv(filename, header=None)


        ## read tilt file ##

            def neg_angle(tiltfile):
                ## extract negative angle ##
                angle = tiltfile.iloc[0:18,]
                angle_neg = angle.iloc[::-1]
                return angle_neg

            df_neg = neg_angle(df)

            def pos_angle(tiltfile):
                ## extract postive angle ##
                angle_pos = tiltfile.iloc[18:37,]
                return angle_pos

            df_pos = pos_angle(df)
    
            def reorder_tlt(neg_angle, pos_angle):
                angle_init_pos = pos_angle.iloc[0:4,0]
                angle_init_neg = angle_init_pos.append(neg_angle.iloc[0:3,0])
                angle_pos1 = angle_init_neg.append(pos_angle.iloc[4:7,0])
                angle_neg1 = angle_pos1.append(neg_angle.iloc[3:6,0])
                angle_pos2 = angle_neg1.append(pos_angle.iloc[7:10,0])
                angle_neg2 = angle_pos2.append(neg_angle.iloc[6:9,0])
                angle_pos3 = angle_neg2.append(pos_angle.iloc[10:13,0])
                angle_neg3 = angle_pos3.append(neg_angle.iloc[9:12,0])
                angle_pos4 = angle_neg3.append(pos_angle.iloc[13:16,0])
                angle_neg4 = angle_pos4.append(neg_angle.iloc[12:15,0])
                angle_pos5 = angle_neg4.append(pos_angle.iloc[16:19,0])
                angle_reorder = angle_pos5.append(neg_angle.iloc[15:18,0])
                angle = angle_reorder.reset_index(drop=True)
                return angle

            df_order = reorder_tlt(df_neg, df_pos)
            df_order.to_csv(df_var + '.order',index = False, header = False)
            
            
if __name__ == '__main__':
     
    # Calling main() function
    main()