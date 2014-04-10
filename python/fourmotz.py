# Fourmotz PYTHON
import numpy as N


def sort_value(value):
	if value>0:
		return -2
	elif value<0:
		return -1
	else:
		return 0

def row_divide(row):
	if row[0]!=0:
		return row/N.abs(row[0])
	else:
		return row

def rearrange_matrix(A, el_var):
	r, s = A.shape
	I = N.identity(s)
	I[:, el_var-1] = N.zeros(s)
	I[0, el_var-1] = 1;
	I[:, 0] = N.zeros(s)
	I[el_var-1, 0] = 1
	return N.dot(A,I)

def four_motz(A, c, el_var):
	
	"""
	Eliminating first column variable
	"""
	assert type(A) is N.ndarray
	assert type(c) is N.ndarray
	
	# ---- Prepare and sort ---- #

	# Put elimination varible in first column
	A = rearrange_matrix(A, 1)
	print A	

	# Stack
	T = N.hstack([A, c])

	# Sort w.r.t. first column -> [pos, neg, zero]
	T = N.array(sorted(T, key=lambda x: sort_value(x[0])))

	# ---- Set constants ---- #
	s, r = T.shape
	
	n_pos = (T[:,0]>0).nonzero()[0].size
	n_neg = n_pos + (T[:,0]<0).nonzero()[0].size
	#n_zer = n_neg + (T[:,0]==0).nonzero()[0].size

	# ---- Normalize on first column ---- #
	T = N.array(map(row_divide, T))
	
	print T

	# s - inequalities after elimination
	s = s - n_neg + n_pos*(n_neg - n_pos)
	r = r - 1

	A = N.zeros((s, r))

	for i in xrange(n_pos):
		A[i*(n_neg - n_pos):(i+1)*(n_neg - n_pos), :] = T[i,1:]*N.ones([n_neg-n_pos, r])+T[n_pos:n_neg,1:]

	A[n_pos*(n_neg - n_pos):, :] = T[n_neg:, 1:]

	A = N.array(sorted(A, key=lambda x: sort_value(x[0])))


if __name__ == '__main__':
	A = N.array([[2.0, -11.0], [-3.0, 2.0], [1.0, 2.0], [-2.0, 1.0],[-4.0, 3.0], [0.0, 1.0], [0.0, 2.0]])

	b = N.array([[1.0],[1.0],[1.0],[1.0], [1.0], [1.0], [1.0]])


	four_motz(A, b, 2)# Fourmotz PYTHON


	#A = N.array([[2.0, -11.0, 1.0], [-3.0, 2.0, 2.0], [1.0, 3.0, 3.0], [-2.0, 0.0, 4.0]])
	#b = N.array([[3.0],[-5.0],[4.0],[-3.0], [1.0]])
