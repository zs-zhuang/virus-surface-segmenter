virus-surface-segmenter
===========

<img src="https://github.com/zs-zhuang/virus-surface-segmenter/blob/main/images/original.JPG"> <img src="https://github.com/zs-zhuang/virus-surface-segmenter/blob/main/images/result3.JPG">

# Summary

This repository contains scripts that segment images of stem cell colonies on petri dishes (see example original and result images).

# Detailed Instruction

1. open original image in gimp and manually bucket fill surface protein in red color (255, 0, 0) and background in green (0, 255, 0), save as colorLabel_ring_virus_image.jpeg

2. run Select_training_data.py on colorLabel_ring_virus_image.jpeg to write out a list of pixel positions corresponding to good and bad pixels by selecting for either green or red color. It will generate position_train_bad and position_train_good

3. Take the original image, run lowpass30, morph5, hist_clahe20, highpass1. Will use original image, clahe20 and highpass1 to calculate 15 features, 5 for each image. 
 
4. use extract_train_features.py to extract features of pixels in the position_train_bad and position_train_good from original image, clahe20 and highpass1

5. usually I have way too many data points for training, just want to use half of it. run split_train_half.py to divide training data into part1 and part 2

6. just train mlp on part1 of the training data and predict as usual

7. run visualize_prediction_2class.py to visualize perdition in color as usual, save as final_prediction.jpeg

8. run binary_prediction_2class.py, which colors all +1 pixel in white and -1 in black to produce a binary black/white image, save as binary.jpeg

9. Move binary.jpeg to post_process_prediction directory, run denoise.py on binary.jpeg to get denoise_binary.jpeg

10. run get_protein_position.py on get denoise_binary.jpeg to generate a refined list of pixel position corresponding to predicted protein, save as protein_position_denoise_binary. This file can be used to re-color predicted protein back into yellow color on the original image for visualization purpose. Run_back_to_color.py and save as denoise_final_prediction.jpeg

11. If I want to trace the edge of each protein, go back to denoise_binary.jpeg, run Gradient.py on it, save output as Gradient_denoise_binary.jpeg, this will be a black white image where each protein is traced out with a white line (if I want, the white pixels, i.e., the line that traces the protein can be fed back into the original image so that it looks like Ludo's picture where the proteins just have their edge traced and not color filled

12. An alternative to running denoise.jpeg is to run Closing.py with parameter = 2 followed by Opening.py with parameter = 3. Can't say the result is that different
