import os, sys, subprocess

#!/bin/bash
#python neural_style.py --content bday-2020/p5.jpg --styles bday-2020/s10.PNG --initial bday-2020/p5.jpg --checkpoint-output output/test_%05d.png --checkpoint-iterations 100 --iterations 1000 --output output/test.png --overwrite --tv-weight 400 --content-weight-blend 0.75 --preserve-colors


python neural_style.py --content bday-2020/p5.jpg --styles bday-2020/s10.PNG --initial bday-2020/p5.jpg --checkpoint-output output/test_%05d.png --checkpoint-iterations 100 --iterations 1000 --output output/test.png --overwrite --tv-weight 400 --content-weight-blend 0.75 --preserve-colors

#
