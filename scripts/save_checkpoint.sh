#!/bin/bash

echo "saving checkpoint"
TIME=$(date +"%d%H%M")
mkdir ./bach_run_dir/checkpoints/$TIME
cp -r ./bach_run_dir/train ./bach_run_dir/checkpoints/$TIME
cp -r ./bach_run_dir/eval ./bach_run_dir/checkpoints/$TIME
