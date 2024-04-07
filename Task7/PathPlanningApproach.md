### PATH PLANNING APPROACH
The code first reads the image (image2.png) and applies a denoising filter (fastNlMeansDenoisingColored) to reduce noise in the image.
Next, the rules determine thresholds (black_threshhold and blue_threshhold) to separate black areas from blue areas
The pathfinding algorithm consists of several steps:
identify the lines and line in the image as the starting point, mark it as the starting point . area of ​​interest of the plan.
The image will be placed in a grid and the color of each grid cell will be checked to determine if it is below the blue threshold.
Based on color analysis, it (finally) creates a binary matrix representing the navigable path (0 means blue, 1 means black).
Uses the full field search method (BFS) to find the shortest path from the right corner to the left corner of a binary matrix. The BFS algorithm uses the reference matrix and the main matrix to track the path.
When the shortest path is found, the number shows it as a red line on the graph.