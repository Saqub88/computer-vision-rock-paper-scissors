# Computer Vision RPS

## Milestone 2
Had to create a teachable-macine model using webcam. this would in turn allow the computer to take a visual input of rock, paper or scissors. excited to see how this will play out.
not used the platform before but seemed relatively straight forward. did initially attempt to create a model using 200 images per option using different hand positions to capture a wider variety of positions but this only confused the machine. on 2nd attempt stuck to a rigid hand position for 50 images and this seems to have worked well.

## Milestone 4
Basic game works. did create a working model of game at an earlier point in course but this version was formatted quite differently. Had to revise the code several times to allow the game to function the way the project required me too (wrapping 3 functions under the umbrella of a single functions). did struggle initially to get the game function to utilise the inputs but was unable to get the get_winner function to utilise the player functions. found two solutions. first was to make the the cpu and player choices into global variables but the 2nd option seemed the better which was to have the game code take the player inputs as parameters in the function. 