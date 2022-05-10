
apt-get update && upgrade -y
apt-get install vlc
clear
echo "Good Job :)"
sleep 3
clear

exe=`ls | grep downtube.py`
if [ $? == 0 ] ; then
    echo "Running DownTube..."
    sleep 3
    echo $exe
    python3 downtube.py
else
    clear
    echo "unexpected error"

fi