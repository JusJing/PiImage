SOURCE_DIR=/home/pi/servers/pidocs/piimages/pi
TARGET_DIR=/home/pi/servers/pidocs/piimages/compressed

for file in $SOURCE_DIR/*.jpg
do 
    echo $file
    jpegoptim --size=50% -o $file --dest=$TARGET_DIR
done