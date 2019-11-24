import mido
import time
from mido import MidiFile
import os
import subprocess
import thread

from Midi_Queue import Midi_Queue
from Node import Node

checkpoint_list = os.listdir('./checkpoints')
del checkpoint_list[0]

#print checkpoint_list

port_out = mido.open_output('to Max 1')
port_in = mido.open_input('MPKmini2')

delay_time = 6

max_ind = len(checkpoint_list) - 1
midi_file_queue = Midi_Queue()
queue_lock = thread.allocate_lock()
delay_lock = thread.allocate_lock()

def callback(self):
    for msg in self.port_in:
        print(msg)


def create_midi_file(ind):
	call = "run_magenta.sh " + "./checkpoints/" + checkpoint_list[ind]
	subprocess.call(call, shell=True)

	midi_file = MidiFile("./checkpoints/" + checkpoint_list[ind] + "/curr.mid")

	return midi_file

def user_input():
	i = 0
	while(i < 140):
		ind = i
		if(ind >= 0 and ind <= max_ind):
			file = create_midi_file(ind)
			n = Node(file)
			with queue_lock:
				midi_file_queue.push(n)
			i = i + 8
		time.sleep(2)
	while(1):
		with queue_lock:
			if(midi_file_queue.check_empty()):
				file = create_midi_file(139)
				n = Node(file)
				midi_file_queue.push(n)		
		time.sleep(50)

def speed_change():
	global delay_time
	while True:
		for ctl_msg in port_in.iter_pending():
			if(ctl_msg != None):
				if(ctl_msg.type == 'control_change'):
					if(ctl_msg.control == 1 and ctl_msg.value > 0):
						speed_midi = ctl_msg.value
						scale = speed_midi / 127.0
						delay_time = max(3.0, 10.0 * scale)
		time.sleep(2)

def send_midi():
	global delay_time
	while(1):
		with queue_lock:
			midi_node = midi_file_queue.pop()
			midi_file_queue.print_size()
		if(midi_node != None):
			for midi_msg in midi_node:
				time.sleep(midi_msg.time * delay_time)
				if not midi_msg.is_meta:
					port_out.send(midi_msg)

		time.sleep(2)

def main():
	thread.start_new_thread(send_midi, ())
	thread.start_new_thread(speed_change, ())
	user_input()

main()
