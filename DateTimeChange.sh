#! /bin/bash

wget "http://worldtimeapi.org/api/timezone/Asia/Kolkata.txt";
sleep 1s; #wget is synchronous but anyways ;P
dtime="$(grep -w "datetime" Kolkata.txt)";
y=${dtime[@]:10:4};
m=${dtime[@]:15:2};
d=${dtime[@]:18:2};
h=${dtime[@]:21:2};
min=${dtime[@]:24:2};
sec=${dtime[@]:27:2};
#sudo date +%T -s $neram;
sudo date $m$d$h$min$y.$sec;
rm Kolkata.txt;
