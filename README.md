# PiImage

These documents encompass the capture and prediction of images using a Raspberry Pi, along with image processing tasks such as duplicate removal, resizing, and a document server for convenient file access.

# Resolution Settings Through Web Server 
Start Web Server In Back End: nohup python ImgResolution.py &
Set Resolution Through API: http://192.168.1.2:5000/setResolution?resolution=800*600
    
    Sample Response: 
        {
        "resolutionValue": "800 * 600"
        }
        
Get Resolution Through API: http://192.168.1.2:5000/getResolution
    
    Sample Response:
        {
        "resolutionValue": "800 * 600"
        }
        

# Apache HTTPD Document Server
Setup Apache Document Server Through The Official Guide: https://httpd.apache.org/docs/
### How To Start Apache Server
```
~/servers/pidocs/bin $ sudo ./httpd -k start 
```
### My Apache Document Server Folder Structure

 - Folder Pi: Images Captured By the Orignal Raspberry Pi Camera
 - Folder Duplicate: Duplicated Pictures That are Removed From The Pi Folder After Being Detected From Root-Mean-Square Difference - https://www.thedigitalpictureframe.com/how-to-automatically-remove-duplicate-images-from-your-digital-frame-photo-library/
 - Folder Compressed: Resized pictures of what is remained from Folder Pi through Jpegoptim - https://linuxhint.com/compress-raspberry-pi-images-size-using-jpegoptim/

# Pi Image Capture/Predict
### Image Capture
Image is captured by pi camera with a designated resolution that can be adjusted through web server api.
### Image Predict
Captured images are saved to Pi Folder and will undergo the process of prediction on the abundance of placstic by a pre trained AI model using sklearn.
After the process of prediction, a .json file with the same file name of the image will be generated alongside with its prediction result through the binary numbers 1 and 0.

# Duplication Removal With Cron Job
### Cron Job Details
Starts the duplication removal program
```
crontab cronjob.txt
```
Cron Job Frequency: Excutes Every 10 Seconds
### Other Useful Cron Job Commands:
```
crontab -l - # Check Current Running Cron Jobs
crontab -r - # Remove Current Running Cron Jobs
```
# Image Optimization
### Single File Optimization
```
jpegoptim --size=50% -o /home/pi/servers/pidocs/piimages/pi/test10.jpg --dest=/home/pi/servers/pidocs/piimages/compressed
```
### Batch Optimization 
```
compressImg.sh # Compress all .jpg files under Pi Folder.
```
