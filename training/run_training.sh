source activate magenta

INPUT_DIRECTORY=./bach_xml
SEQUENCES_TFRECORD=./bach_seq.tfrecord
SEQUENCE_EXAMPLE_FOLDER=./bach_seq_ex
RUN_DIR=./bach_run_dir
TRAINING_RECORD=$SEQUENCE_EXAMPLE_FOLDER/training_poly_tracks.tfrecord

# Convert MusicXML files to NoteSequences
convert_dir_to_note_sequences \
  --input_dir=$INPUT_DIRECTORY \
  --output_file=$SEQUENCES_TFRECORD \
  --recursive

# Split NoteSequences into training and eval tfrecords
polyphony_rnn_create_dataset \
  --input=$SEQUENCES_TFRECORD \
  --output_dir=$SEQUENCE_EXAMPLE_FOLDER \
  --eval_ratio=0.10

# Kick off training
polyphony_rnn_train \
  --run_dir=$RUN_DIR \
  --sequence_example_file=$TRAINING_RECORD \
  --hparams="batch_size=128,rnn_layer_sizes=[256,256,256]" \
  --num_training_steps=20000