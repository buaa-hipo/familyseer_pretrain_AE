#!/bin/bash
strB=".json"
for file in ./dataset_dataset_new/*
do 
    #echo $dir/
    
    #/home/zsj/python3.8/bin/python3.8 make_dataset_split.py --logs $dir/*.json --target cuda
    python train_model_split.py --models xgb --dataset $file
done
