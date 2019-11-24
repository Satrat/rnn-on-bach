# Recurrent Neural Networks on Bach

An algorithmic composition that generates polyphonic phrases during the training of an LSTM neural network. Uses performer-controlled time stretching to accent the gradual transition from chaotic noise to tonal harmony.

## Dependencies
* Google's [Magenta](https://github.com/tensorflow/magenta) development environement installed in a virtual env
* Folder of MusicXML or MIDI files to train on. I used this [archive of Bach Chorales](http://sporadic.stanford.edu/Chorales/)
* Python MIDO package(`pip install mido`)

## Repo Layout
### training/
Scripts for converting input music files to tfrecords, training model, and saving checkpoints
### performance/
Script for generating new phrases and Python code for maintaining phrase queue, interpretting control changes and sending MIDI output to Logic
### rnn_logic_project.logicx
Logic project for piece, set up to control effects from MIDI controller

## How to Use
You'll first need to train up a model to generate the checkpoints for the piece by running `run_magenta.sh`. You'll also need to set up `save_checkpoint.sh` to run at a regularly scheduled interval(I chose half an hour) using [Cron](https://linuxconfig.org/linux-crontab-reference-guide) on Linux. At the end of training, you should have a folder of checkpoint folders representing the network at various stages during training.

For a performance, you'll need a MIDI controller hooked up to your machine. Open the logic project `rnn_logicproject.logicx`, which has control change messages mapped to various effects. Then, start the piece by running `performance/send_midi.py`. You should see the MIDI output of the algorithm showing up in Logic. In addition to controlling effects, you can use the MIDI controller to control how fast the piece moves through the checkpoints
