# Computer Vision RPS

## Milestone 2
Had to create a teachable-macine model using webcam. this would in turn allow the computer to take a visual input of rock, paper or scissors. excited to see how this will play out.
not used the platform before but seemed relatively straight forward. did initially attempt to create a model using 200 images per option using different hand positions to capture a wider variety of positions but this only confused the machine. on 2nd attempt stuck to a rigid hand position for 50 images and this seems to have worked well.

## Milestone 3
Basic game works. did create a working model of game at an earlier point in course but this version was formatted quite differently. Had to revise the code several times to allow the game to function the way the project required me too (wrapping 3 functions under the umbrella of a single functions). did struggle initially to get the game function to utilise the inputs but was unable to get the get_winner function to utilise the player functions. found two solutions. first was to make the the cpu and player choices into global variables but the 2nd option seemed the better which was to have the game code take the player inputs as parameters in the function. 

## Milestone 4
Such a nightmare of a tast. A lot of learning took place on this task and a lot of attempts here to try and make the game work with the camera. I wanted to keep some restrictions on myself such as keeping the code spread across the two files (one to run the camera and one to code the game).
The code for running the camera had inherent problems. it performed poorly because the keras component was quite taxing and it was being applied to every single frame. I modified the code to run the video as normal but only perform the analysis on command. it was also printing far too much irrelevant stats into the terminal so then coded that out also. lastly had to change the camera running code into a function to work with the game. I did also study the openCV module which did help me to achieve this. With all this done i just now needed to make sure the user experience was smoother and instructions were being given to the user to see them start to end.

## Milestone 5
This was a quick one to complete. The learning at Milestone 4 allowed me to complete this task pretty simply and helped to add a countdown onto the video feed. Then was just a matter of cleaning up the files that were no longer required and also to clean up the lines of code.
There is still lots that can be done here and will look to implement these at a later stage. I really want to move on with the course :)

1 - Intro and outro to the game.
2 - Option to choose which type of game you want to play included into the code.
3 - Allow the game to offer switching to manual entry if struggling to get the correct reads.
4 - All text and instructions to be displayed in the video.
5 - To improve accuracy, take a reading of multiple frames in sequence instead of a single frame and then return the most frequenty occuring hand. 

For now i think i will stop here.

Files
camera_auto.py and auto_rps.py run the video version
camera_manual.py and manual_rps.py run manual version
Keras_model.h5 and labels.txt are related to computer vision system
requirements.txt was made in accordance with task.
i made RPS_env.yml by saving the conda environment to a file. thought it might be helpful incase i need to switch between computers.
RPS-Template.py was original file given by AiCore.