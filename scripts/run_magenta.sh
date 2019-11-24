source activate magenta

echo "Generating MIDI track at" $1

polyphony_rnn_generate \
--run_dir=$1 --output_dir=$1 \
--num_outputs=1 --num_steps=128 \
--primer_pitches="[67,63,60]" \
--condition_on_primer=true \
--inject_primer_during_generation=false

mv $1/*.mid $1/curr.mid 
