import cv2
import numpy as np
import os

def create_pos_n_neg():
    for file_type in ['new_pos']:

        for img in os.listdir(file_type):
	
            if file_type == 'pos':
                line = file_type+'/'+img+' 1 0 0 50 50\n'
                with open('info.dat', 'a') as f:
                    f.write(line)
            elif file_type == 'new_pos':
                line = img+' 1 0 0 50 50\n'
                with open('info.lst', 'a') as f:
                    f.write(line)
                    
create_pos_n_neg()
