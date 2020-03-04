import os, sys, subprocess

#!/bin/bash
#python neural_style.py --content bday-2020/p5.jpg --styles bday-2020/s10.PNG --initial bday-2020/p5.jpg --checkpoint-output output/test_%05d.png --checkpoint-iterations 100 --iterations 1000 --output output/test.png --overwrite --tv-weight 400 --content-weight-blend 0.75 --preserve-colors

#################################################
output_dir  = 'output-8'
content_dir = 'bday-2020/contents'
style_dir   = 'bday-2020/styles-all'
TV_W        = 700 # 250
CONT_W_B    = 0.5 # 1.0
NUM_ITERS   = 1000
PRES_COL    = False # True
STYLE_W     = 6000 # 500
#################################################

contents = [ os.path.join(content_dir, f) for f in os.listdir(content_dir) ]
styles   = [ os.path.join(style_dir, f)   for f in os.listdir(style_dir)   ]
NC       = len(contents)
NS       = len(styles)

print('Content targets\n', contents)
print('Style targets\n', styles)
print('Total number of outputs (not incl. intermeds)\n', NC * NS)

CMD = 'python neural_style.py --content %s --styles %s --initial %s --checkpoint-output %s --checkpoint-iterations 350 --iterations %d --output %s --overwrite --tv-weight %d --content-weight-blend %f --style-weight %f'

pc   = ' --preserve-colors'
send = '_%05d.png'
oend = '.png'
begn = 'f-'

jn = lambda s: os.path.join(output_dir, s)

T = 0
for i, c in enumerate(contents):
    for j, s in enumerate(styles):
        print("-------------------")
        print('ON', i, j)
        print("-------------------")
        
        # Assemble command
        cnamae = ('st-p-%d-%d' if PRES_COL else 'st-%d-%d') % (i, j)
        final_out_name = jn(begn + cnamae + oend)
        if os.path.exists(final_out_name): 
            print("\tAlready exists. Skipping.")
            continue
        curr_cmd = CMD % ( c, s, c, jn(cnamae + send), NUM_ITERS, final_out_name, TV_W, CONT_W_B, STYLE_W )
        if PRES_COL: curr_cmd += pc
        print('Running', curr_cmd)

        # Run command
        #try:
        subprocess.run(curr_cmd, shell=True, check=True)
        #except:
            
        
        # Counter
        T += 1
        print('Done', T, '/', NC * NS)

#
