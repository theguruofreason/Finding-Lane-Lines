#**Finding Lane Lines on the Road** 

---

**Finding Lane Lines on the Road**

The goals / steps of this project are the following:
* Make a pipeline that finds lane lines on the road
* Reflect on your work in a written report




---

### Reflection

My pipeline consists of 6 steps. First, the image is converted to grayscale, though this was not done for the video processing pipeline. Second, the image is smoothed using gaussian_blur. Third, thresholds for the canny transform are established the transform is applied. Fourth, a section of the image where the lane lines are most likely to be is masked. Fifth, the masked section is hough transformed to pick out continuous lines and two subsections of lines which pass respective slope tests are chosen and converted into a single line each representing their average. Finally, these two lines are drawn on the original image.

The draw_lines function was heavily modified to create a single lane line for each lane line in the image. I first created a nested for loop to loop over the lines and grab their coordinates. Then I calculed the slope using the coordinates and filtered the lines into "left" and "right" categories based on their slopes. At the same time I started accumulating their x and y values to be averaged later. Then the slopes and coordinates of each of the categories were averaged and the endpoints of the lane lines were extrapolated using the average coordinate and the slope for each. Finally, the function then draws the lines on the original image.

One potential shortcoming of this method is that it doesn't function if the lane lines are a very similar color to the road, or if the road is very reflective. Another is that it likely will lose a lot of precision in tight turns because there will be far fewer lines which satisfy the slope test. Finally, the processing is quite slow, sometimes taking twice as long as the video it's working from. Whether this is as a result of FFMPEG or the pipeline itself is unclear. Regardless, it predicts lane lines to a good distance.

One possible improvement is to convert all of the yellow in the masked area to white before doing canny and hough transforms to maximize contrast and thus maximize the number of lines. Another would be to allow for it to determine significant curves in order to predict upcoming turns. 

Overall though, this pipeline is very successful at the task set for it. It even compitantly completes the optional challenge task which is on a more curved road and with changes in the asphalt.