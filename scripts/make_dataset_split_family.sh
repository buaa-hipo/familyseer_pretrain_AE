#!/bin/bash
strB=".json"
for dir in ./flit_file/*
do 
    echo $dir/
    
    /home/zsj/python3.8/bin/python3.8 make_dataset_split.py --logs $dir/*.json --target cuda --mode 0

done