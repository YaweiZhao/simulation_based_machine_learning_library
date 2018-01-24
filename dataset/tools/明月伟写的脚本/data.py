import numpy as np
from scipy.sparse import csc_matrix, csr_matrix, coo_matrix
from scipy.io import savemat

data = []
row = []
col = []
def convert(data_file_name):
	"""
	convert the libsvm format data file (without label) 
	into sparse and dense form matrix
	"""
	global data, row, col
	# Create the appropriate format for the COO format.
	r = 0
	data = []
	row = []
	col = []
	for line in open(data_file_name):
		line = line.rstrip()
		for e in line.split(' '):
			ind, val = e.split(":")
			row.append(r)
			col.append(int(ind)-1)
			try:
				data.append(float(val))
			except ValueError as err:
				print("error",err,"on line",r)
		r=r+1
	# Create the COO-matrix
	coo = coo_matrix((data,(row,col)))
	# Let Scipy convert COO to CSR format and return
	return csr_matrix(coo)
	# Let Scipy convert COO to CSC format and return
	#return csc_matrix(coo)

num_files = 1
path = '/vol6/home/kd_yjp/myw/DMTK/datasets/covtype/16_processes/'

for i in range(num_files):
	filename = path + str(i) +'/raw_trn_x' 
	sparse_form = convert(filename) # Here is the path of the libsvm format sample file(without labels).
	#dense_form = sparse_form.todense()

	#--- save dense and sparse data as mat file
	#savemat('data/sparse.mat', {'sparse_form': sparse_form})
	#savemat('data/dense.mat', {'dense_form': dense_form})

	#--- save dense and sparse data as raw ASCII file
	#raw_sparse_txt = np.vstack([row, col, data]).T
	#np.savetxt('data/raw_sparse.txt', raw_sparse_txt, fmt="%.9g")
	#np.savetxt('data/raw_dense.txt', dense_form, fmt="%.9g")

	#--- save dense and sparse data as raw binary file
	#raw_sparse_bin = np.vstack([row, col, data]).T
	#raw_sparse_bin.tofile('data/raw_sparse.bin')
	#dense_form.transpose().tofile('data/raw_dense.bin')

	#--- save sparse data as CSC Matrix binary file
	#sparse_form = sparse_form.transpose() # Transpose is time consuming. we make transpose here so that it need not be made in our C++ program, i.e. logistic_regression.cpp. 
	sparse_form.data.tofile(path + str(i) + '/data.bin')
	sparse_form.indices.astype(np.uint64).tofile(path + str(i) + '/indices.bin')
	sparse_form.indptr.astype(np.uint64).tofile(path + str(i) + '/indptr.bin')
	shape = np.array([sparse_form.shape[1], sparse_form.shape[0]])
	shape.astype(np.uint64).tofile(path + str(i) + '/shape.bin')
	#sparse_form.indices.tofile('data/indices.bin')
	#sparse_form.indptr.tofile('data/indptr.bin')

	#print sparse_form.dtype
	#print sparse_form.shape
	#print sparse_form.data
	#print type(sparse_form.indices.astype(np.uint64)[1])
	#print sparse_form.indptr

	#print(sparse_form)
	#print(dense_form)
