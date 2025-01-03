import unittest

class Layer:
	def __init__(self, weight, forward_function, cost_function):
		self.weight = weight
		self.forward_function = forward_function
		self.cost_function = cost_function

class Cluster:
	def __init__(self, num_nodes, nodes):
		self.nodes = nodes
		self.num_nodes = num_nodes

class TrainingDataset:
	def __init__(self, data):
		self.data = data

	def generate_minibatches():
		return

class MiniBatch:
	# Subset of training data
	def __init__(self, data):
		self.data = data

	def generate_microbatches():
		return

def gPipe(K, M, L):
	'''
	Approach:
	(1) schedule multiple microbatches
	(2) synchronize gradient updated with minibatch

	Constraints:
	Forward pass of layer n + 1 cannot be computed, until layer n completed
	Backward pass of layer n cannot be computed, until layer n+1 completed

	network = f_2(f_1(f_0(x)))

	Inputs:
	K - number of model partitions
	M - number of micro-batches
	L - layers (sequence and definitions) - basically the model
	'''
	c = Cluster(K, None)
	b = MiniBatch()
	k_paritions = parition_network(c, K, L)

	iterations = 0
	while iterations < 0:
		b_microbatches = b.generate_microbatches()
		pipeline(b_microbatches, c)
		forward_pass()
		backward_pass()
		iteration += 1
	return

def forward_pass():
	return

def backward_pass():
	return

def pipeline(data, cluster):
	# schedule data to cluster
	return

def parition_network(cluster, model, partitions):
	# split graph into chunks
	chunk_size = len(model)//partitions
	for i, layer in enumerate(model):
		cluster.nodes[(i//chunk_size) % partitions].append(layer)
	return
	sett
def pipeDream():
	return 

class TestMethods(unittest.TestCase):
	def test_pipeDream(self):
		pipeDream()
		return False

	def test_gPipe(self):
		gPipe(None, None, None)
		return False

	def test_partition_network():
		parition_network(None, None, None)
		return False

	def test_pipeline():
		pipeline(None, None)
		return False

	def test_backward_pass():
		backward_pass()
		return False

	def test_forward_pass():
		forward_pass()
		return False

	def test_generate_microbatches():
		mb = MiniBatch(None)
		mb.generate_microbatches()
		return False

	def test_generate_minibatches():
		td = TrainingDataset(None)
		td.generate_minibatches()
		return False

if __name__ == '__main__':
    unittest.main()