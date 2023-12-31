# PiImage

These documents encompass the capture and prediction of images using a Raspberry Pi, along with image processing tasks such as duplicate removal, resizing, and a document server for convenient file access.

### Process Overview
![Flowcharts (1)](https://github.com/JusJing/PiImage/assets/124528112/d3544bc9-2ce0-4de6-b3cc-b198f9cd2363)



### Components Overview
![FlowChart](https://github.com/JusJing/PiImage/assets/124528112/e0917915-4d61-40a7-89dd-98b949c331e1)



# Pi Image Web Server
Start Web Server In Backend: 
```
start by command: nohup python ImageServer.py &
or run init.sh
```
```
ps -ef |grep ImageServer # Check Backend Process
Console Output:
pi          1983       1  0 01:48 ?        00:00:00 python ImageServer.py
pi          1995    1983 42 01:48 ?        00:01:22 /usr/bin/python /home/pi/ImageServer.py
```
### Set/Get Resolution
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
### Image Capture
```
http://192.168.1.2:5000/imageCapture
Sample Response:
{
    "status": "success"
}
```
### List Image
```
http://192.168.1.2:5000/listImages
Sample Response:
{
    "files": [
        "pi_2023_12_30_01:27:32.jpg",
        "pi_2023_12_30_01:04:24.jpg",
        "pi_2023_12_30_01:12:33.jpg",
        "pi_2023_12_30_01:14:10.jpg",
        "pi_2023_12_30_01:27:30.jpg",
        "pi_2023_12_30_01:30:17.jpg",
        "pi_2023_12_30_01:27:31.jpg"
    ]
}
```
### Download Image
```
http://192.168.1.2:5000/downloadImage?filename=pi_2023_12_30_01:27:32.jpg
```

# Apache HTTPD Document Server
Setup Apache Document Server Through The [Apache Official Guide](https://httpd.apache.org/docs/)
### How To Start Apache Server
```
sudo ./httpd -k start 
```
### My Apache Server URL/Config
```
http://192.168.1.2:90/piimages/
Alias /piimages/ "/home/pi/servers/pidocs/piimages/"
```
### My Apache Document Server Folder Structure
<img width="292" alt="屏幕截图 2023-12-16 165048" src="https://github.com/JusJing/PiImage/assets/124528112/8715cb18-f13d-4614-9416-2fd3b8729880">


 - Folder **pi**: Images Captured By the Orignal Raspberry Pi Camera
 - Folder **duplicate**: Duplicated Pictures That are Removed From The **pi** Folder After Being Detected From [Root-Mean-Square Difference](https://www.thedigitalpictureframe.com/how-to-automatically-remove-duplicate-images-from-your-digital-frame-photo-library/)
 - Folder **compressed**: Resized pictures of what is remained from Folder **pi** through [Jpegoptim](https://linuxhint.com/compress-raspberry-pi-images-size-using-jpegoptim/)

# Pi Image Capture/Predict
### Image Capture
Image is captured by pi camera with a designated resolution that can be adjusted through web server api.
### Image Predict
Captured images are saved to **pi** Folder and will undergo the process of prediction on the abundance of placstic by a pre trained AI model using sklearn.
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
compressImg.sh # Compress all .jpg files under pi Folder.
```

