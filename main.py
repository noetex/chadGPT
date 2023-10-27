'''

class engine:
	def __init__(self, Value):
		pass

	def __repr__(self):
		print("Data = asdf\nThing = asdf\n")


	def __add__(self, Other):
		pass

CHUNK
BATCH # collection of chunks that can be processed at once

def get_batch(split):
	data = train_data if split == 'train' else valid_data
	ix = torch.randint(len(data) - block_size, (batch_size,))
	x = torch.stack([data[i:i+block_size] for i in ix])
	y = torch.stack([data[i+1:i+block_size+1] for i in ix])
	return x, y
'''

'''
BLOCK_SIZE = 8
TRAIN_DATA = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]

X = TRAIN_DATA[:BLOCK_SIZE]
Y = TRAIN_DATA[1 : BLOCK_SIZE + 1]

Chunk

for T in range(BLOCK_SIZE):
	Context = X[:T+1]
	Target = Y[T]
	print(f"Input = {Context} --> Target = {Target}")
'''


import time


THING = """
Welcome aboard, Agent.
Everything was clear an hour ago. Then, BOOM!
My orders are to hang back.
If I catch a sight of the NSF commander at the top of the Statue, I'm gonna take
a shot. Screw Manderley.
The thugs must be desperate to attack us here.
I don't like just standing around, but orders are orders.
Whatever was in that barge, the NSF sure wanted it bad.
Careful, Agent. Rebels are crawling all over the place.
I've got this area secured.
"""

'''
# input_layer  -> (Values, Weights)
# hidden_layer -> (Weights, Biases, Activation Function)
# output_layer -> (Values, Biases)

class input_data:


class neural_network:
	def __init__(Dataset, )
'''

def sigmoid(Value):
	Result = math.exp(-Value)
	return Result



def print_slowly():
	the_list = THING.split(' ')
	for word in the_list:
		print(word, end=' ', flush=True)
		time.sleep(0.05)


def main():
	while(True):
		print("chadGPT>", end='')
		thing = input()
		print_slowly()



if __name__ == "__main__":
	main()
