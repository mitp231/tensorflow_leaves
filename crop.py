#Mit Patel
#05/17/18
#Crop image

from PIL import Image
import os, sys

source = 'Insert path of folder containing the subfolders of leaves here'                  #source folder
target = 'Insert path of folder that will contain the subfolders of the cropped images'    #target folder

track_names=[]   #use to track names of leaves to rename after iterating through last leaf of a subfolder
i=0              #use to rename cropped image according to type of leaf and number of file

for subdir, dirs, files in os.walk(source):

    #loop through all files in rootdir
    for file in files:

        #retrieve name of leaf from name of folder
        leaf_type = os.path.basename(os.path.normpath(subdir))

        #put name of current leaf into track_names
        track_names.append(leaf_type)

        #if size of track_names permits and the current leaf type is not the last one in the folder
        if len(track_names) > 2 and  leaf_type != track_names[-2]:

            #then restart counting for new folder
            i = 0

        img=Image.open(subdir+'\\'+file)     #open image
        img2 = img.crop((0,0, 600, 650))     #crop image to 600 x 650 pixels

        #if subfolder exists
        if os.path.exists(target + leaf_type):

            #save the cropped image in that folder
            img2.save(target + leaf_type+ '\\'+ leaf_type + str(i) + '.jpg')

        #if subfolder does not exist
        if not os.path.exists(target + leaf_type):

            #make subfolder
            os.mkdir(target + leaf_type)

            #save the cropped image in that folder
            img2.save(target + leaf_type+ '\\' + leaf_type + str(i) + '.jpg')

        i = i+1
