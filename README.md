# Tensorflow Classifier for Species of Leaves found in the Northeastern United States

There are over 185 species of trees in the Northeastern United States; the classification of these species via deep learning methods would entail composing a data set of images of these species. Because of how large trees are, making such a data set would be very difficult. Instead, one can rely on the leaves of the trees to designate which species it belongs to. This Tensorflow model uses a data set composed by Leafsnap [1], which consists of images of leaves taken from two different sources: the Lab and the Field. There are 23,147 images from the lab and 7,719 images from the field for a total of 30,866 images of leaves from 185 tree species. To train a model to classify the images of these leaves, this repository relies on transfer learning. 
Transfer learning entails taking knowledge gained by a model while training on a source task to improve the learning of a related target task. In this case, the knowledge gained by the Inception-v3 model [2] is used to help learn from the Leafsnap data set. Inception is a deep learning model that was trained on the ImageNet data set, which is composed of images belonging to one of 1,000 classes like “Zebra”, “Dalmatian”, or “Dishwasher” [3]. The reasons for using transfer learning are several: using knowledge from the Inception-v3 model does not entail retraining the model on the entire ImageNet data set. Only the last layer of the model must be retrained to repurpose it for the classification of the Leafsnap data set, which takes a fraction of the time it took to train the Inception-v3 on ImageNet. Furthermore, the images in the Leafsnap data set do not only consist of leaves. The images taken in the Field include several artifacts such as hands, background light, and rulers. Transferring knowledge from Inception-v3 minimizes the chances that “artifact” pixels are not mistaken for “leaf” pixels. 

To reduce the amount of artifacts in the images before training, the images from the field are cropped to exclude pixels from hands or rulers. This begins the process for training this model:

1.	Download tensorflow_leaves folder from repository
        These files were taken from the tensorflow repository. To download your own, go into cmd (Windows) or terminal (Mac) and input           the following code:
        
        git clone https://github.com/googlecodelabs/tensorflow-for-poets-2
        
      This will download the tensorflow-for-poets-2 folder onto your computer. This folder is renamed to tensorfow_leaves in this             repository.

2.	Download the tf_files folder, which contains subfolders of the images of leaves, and put that into the tensorflow_leaves folder.

3.	Use the Crop.py python script to crop the lab images into 600 x 650 pixels (will need to change path names to account for your folders)


4.	Install Python and Tensorflow (https://www.tensorflow.org/install/)

5.	Go into cmd (Windows) or Terminal (Mac) and go into the directory of the tensorflow folder


6.	Retrain the model on your images by entering the following:

         python scripts/retrain.py –
         output_graph=tf_files/retrained_graph.pb --output_labels=tf_files/retrained_labels.txt –
         image_dir=tf_files/leaves 

These steps will classify the images contained within the subfolders of /leaves. Steps 1-5 can be used with any folder in place of leaves that contains subfolders of the images you want to classify. 


7.	Once the model has finished training, it will generate a retrained_graph.pb and retrained_labels.txt file under tf_files. 

8.	To test a new image against the model, run the following code in the tensorflow directory:

    	    python scripts/label_image.py - - image image.jpg
          
    where “image.jpg” is the image you want to test



Thanks to the following sources for help with this project:

https://towardsdatascience.com/training-inception-with-tensorflow-on-custom-images-using-cpu-8ecd91595f26

https://codelabs.developers.google.com/codelabs/tensorflow-for-poets/?utm_campaign=chrome_series_machinelearning_063016&utm_source=gdev&utm_medium=yt-desc#0

References


[1] "Leafsnap: A Computer Vision System for Automatic Plant Species Identification,"
Neeraj Kumar, Peter N. Belhumeur, Arijit Biswas, David W. Jacobs, W. John Kress, Ida C. Lopez, João V. B. Soares,
Proceedings of the 12th European Conference on Computer Vision (ECCV),
October 2012 (http://leafsnap.com/dataset/)

[2] “Rethinking the Inception Architecture for Computer Vision,” Szegedy, Christian; Vanhoucke, Vincent; Ioffe, Sergey; Shlens, Jonathon; Wojna, Zbigniew. (https://arxiv.org/pdf/1512.00567.pdf)

[3] L. Fei-Fei, ImageNet: crowdsourcing, benchmarking & other cool things, CMU VASC Seminar, March, 2010 (http://www.image-net.org/papers/ImageNet_2010.pdf) 
