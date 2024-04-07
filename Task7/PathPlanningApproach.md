### PATH PLANNING APPROACH
The code first reads the image (image2.png) and applies a denoising filter (fastNlMeansDenoisingColored) to reduce noise in the image.
Next, it detects lines vertical and horizontal by taking average of rgb value of each row and column(All lines are single pixeled so all lines are detected once)
Then it takes average of all boxes bounded by squares and if it is blue value is above a threshold it is considered blue else yellow. 
Then it's apply BFS storing the parent cell. Then it prints the path using parent cells from the last cell that leads to the first cell.
