import numpy as np

GrafoPos = [
	[0.8, -0.028, 0.8],
	[-0.4, -0.028, 0.8],
	[0.0, -0.028, 0.8],
	[0.4, -0.028, 0.8],
	[-0.8, -0.028, 0.8],
	[0.8, -0.028, 0.4],
	[-0.4, -0.028, 0.4],
	[0.0, -0.028, 0.4],
	[0.4, -0.028, 0.4],
	[-0.8, -0.028, 0.4],
	[0.8, -0.028, -0.0],
	[-0.4, -0.028, -0.0],
	[0.0, 0.372, -0.0],
	[0.4, -0.028, -0.0],
	[-0.8, -0.028, -0.0],
	[0.8, -0.028, -0.4],
	[-0.4, -0.028, -0.4],
	[0.0, 0.172, -0.4],
	[0.4, 0.372, -0.4],
	[-0.8, -0.028, -0.4],
	[0.8, 0.172, -0.8],
	[-0.4, -0.028, -0.8],
	[0.0, -0.028, -0.8],
	[0.4, 0.172, -0.8],
	[-0.8, -0.028, -0.8],
]

GrafoLen = 25

GrafoMesh = np.array([
	-0.4, -0.028, 0.4, 
	-0.8, -0.028, 0.4, 
	-0.4, -0.028, 0.8, 
	-0.8, -0.028, 0.8, 
	0.0, -0.028, 0.8, 
	-0.4, -0.028, 0.8, 
	0.4, -0.028, 0.8, 
	0.0, -0.028, 0.8, 
	0.8, -0.028, 0.8, 
	0.4, -0.028, 0.8, 
	0.0, -0.028, 0.4, 
	-0.4, -0.028, 0.4, 
	0.4, -0.028, 0.4, 
	0.0, -0.028, 0.4, 
	0.8, -0.028, 0.4, 
	0.4, -0.028, 0.4, 
	0.4, -0.028, 0.8, 
	0.4, -0.028, 0.4, 
	0.8, -0.028, 0.4, 
	0.8, -0.028, 0.8, 
	-0.4, -0.028, 0.8, 
	-0.4, -0.028, 0.4, 
	0.0, -0.028, 0.4, 
	0.0, -0.028, 0.8, 
	-0.8, -0.028, 0.8, 
	-0.8, -0.028, 0.4, 
	-0.4, -0.028, -0.0, 
	-0.8, -0.028, -0.0, 
	0.0, 0.372, -0.0, 
	-0.4, -0.028, -0.0, 
	0.4, -0.028, -0.0, 
	0.0, 0.372, -0.0, 
	0.8, -0.028, -0.0, 
	0.4, -0.028, -0.0, 
	0.0, -0.028, 0.4, 
	0.0, 0.372, -0.0, 
	0.4, -0.028, -0.0, 
	0.4, -0.028, 0.4, 
	-0.8, -0.028, 0.4, 
	-0.8, -0.028, -0.0, 
	-0.4, -0.028, -0.0, 
	-0.4, -0.028, 0.4, 
	0.8, -0.028, -0.0, 
	0.8, -0.028, 0.4, 
	-0.4, -0.028, -0.4, 
	-0.8, -0.028, -0.4, 
	0.0, 0.172, -0.4, 
	-0.4, -0.028, -0.4, 
	0.4, 0.372, -0.4, 
	0.0, 0.172, -0.4, 
	0.8, -0.028, -0.4, 
	0.4, 0.372, -0.4, 
	0.0, 0.372, -0.0, 
	0.0, 0.172, -0.4, 
	0.4, 0.372, -0.4, 
	0.4, -0.028, -0.0, 
	-0.8, -0.028, -0.0, 
	-0.8, -0.028, -0.4, 
	-0.4, -0.028, -0.4, 
	-0.4, -0.028, -0.0, 
	0.8, -0.028, -0.4, 
	0.8, -0.028, -0.0, 
	-0.4, -0.028, -0.8, 
	-0.8, -0.028, -0.8, 
	0.0, -0.028, -0.8, 
	-0.4, -0.028, -0.8, 
	0.4, 0.172, -0.8, 
	0.0, -0.028, -0.8, 
	0.8, 0.172, -0.8, 
	0.4, 0.172, -0.8, 
	0.0, 0.172, -0.4, 
	0.0, -0.028, -0.8, 
	0.4, 0.172, -0.8, 
	0.4, 0.372, -0.4, 
	-0.8, -0.028, -0.4, 
	-0.8, -0.028, -0.8, 
	-0.4, -0.028, -0.8, 
	-0.4, -0.028, -0.4, 
	0.8, 0.172, -0.8, 
	0.8, -0.028, -0.4, 
	0.0, -0.028, 0.4, 
	-0.4, -0.028, 0.8, 
	0.8, -0.028, 0.4, 
	0.4, -0.028, 0.8, 
	0.4, -0.028, 0.4, 
	0.0, -0.028, 0.8, 
	-0.4, -0.028, 0.4, 
	-0.8, -0.028, 0.8, 
	0.4, -0.028, -0.0, 
	0.0, -0.028, 0.4, 
	-0.4, -0.028, -0.0, 
	-0.8, -0.028, 0.4, 
	0.8, -0.028, -0.0, 
	0.4, -0.028, 0.4, 
	-0.4, -0.028, -0.0, 
	0.0, -0.028, 0.4, 
	0.0, 0.172, -0.4, 
	0.4, -0.028, -0.0, 
	-0.4, -0.028, -0.4, 
	-0.8, -0.028, -0.0, 
	0.8, -0.028, -0.4, 
	0.4, -0.028, -0.0, 
	0.0, 0.172, -0.4, 
	-0.4, -0.028, -0.0, 
	0.4, 0.172, -0.8, 
	0.0, 0.172, -0.4, 
	-0.4, -0.028, -0.8, 
	-0.8, -0.028, -0.4, 
	0.8, 0.172, -0.8, 
	0.4, 0.372, -0.4, 
	0.0, -0.028, -0.8, 
	-0.4, -0.028, -0.4, 
], dtype='float32')

GrafoMeshLen = 112

GrafoWeights = [
	[0, 0, 0, 0.4, 0, 0.4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
	[0, 0, 0.4, 0, 0.4, 0, 0.4, 0.5656854249492381, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
	[0, 0.4, 0, 0.4, 0, 0, 0, 0.4, 0.5656854249492381, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
	[0.4, 0, 0.4, 0, 0, 0.5656854249492381, 0, 0, 0.4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
	[0, 0.4, 0, 0, 0, 0, 0.5656854249492381, 0, 0, 0.4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
	[0.4, 0, 0, 0.5656854249492381, 0, 0, 0, 0, 0.4, 0, 0.4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
	[0, 0.4, 0, 0, 0.5656854249492381, 0, 0, 0.4, 0, 0.4, 0, 0.4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
	[0, 0.5656854249492381, 0.4, 0, 0, 0, 0.4, 0, 0.4, 0, 0, 0.5656854249492381, 0.5656854249492381, 0.5656854249492381, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
	[0, 0, 0.5656854249492381, 0.4, 0, 0.4, 0, 0.4, 0, 0, 0.5656854249492381, 0, 0, 0.4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
	[0, 0, 0, 0, 0.4, 0, 0.4, 0, 0, 0, 0, 0.5656854249492381, 0, 0, 0.4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
	[0, 0, 0, 0, 0, 0.4, 0, 0, 0.5656854249492381, 0, 0, 0, 0, 0.4, 0, 0.4, 0, 0, 0, 0, 0, 0, 0, 0, 0],
	[0, 0, 0, 0, 0, 0, 0.4, 0.5656854249492381, 0, 0.5656854249492381, 0, 0, 0.5656854249492381, 0, 0.4, 0, 0.4, 0.6000000000000001, 0, 0, 0, 0, 0, 0, 0],
	[0, 0, 0, 0, 0, 0, 0, 0.5656854249492381, 0, 0, 0, 0.5656854249492381, 0, 0.5656854249492381, 0, 0, 0, 0.447213595499958, 0, 0, 0, 0, 0, 0, 0],
	[0, 0, 0, 0, 0, 0, 0, 0.5656854249492381, 0.4, 0, 0.4, 0, 0.5656854249492381, 0, 0, 0.5656854249492381, 0, 0.6000000000000001, 0.5656854249492381, 0, 0, 0, 0, 0, 0],
	[0, 0, 0, 0, 0, 0, 0, 0, 0, 0.4, 0, 0.4, 0, 0, 0, 0, 0.5656854249492381, 0, 0, 0.4, 0, 0, 0, 0, 0],
	[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.4, 0, 0, 0.5656854249492381, 0, 0, 0, 0, 0.5656854249492381, 0, 0.4472135954999579, 0, 0, 0, 0],
	[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.4, 0, 0, 0.5656854249492381, 0, 0, 0.4472135954999579, 0, 0.4, 0, 0.4, 0.5656854249492381, 0, 0],
	[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.6000000000000001, 0.447213595499958, 0.6000000000000001, 0, 0, 0.4472135954999579, 0, 0.447213595499958, 0, 0, 0, 0.4472135954999579, 0.5656854249492381, 0],
	[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.5656854249492381, 0, 0.5656854249492381, 0, 0.447213595499958, 0, 0, 0.6000000000000001, 0, 0, 0.447213595499958, 0],
	[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.4, 0, 0.4, 0, 0, 0, 0, 0.5656854249492381, 0, 0, 0.4],
	[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.4472135954999579, 0, 0, 0.6000000000000001, 0, 0, 0, 0, 0.4, 0],
	[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.4, 0, 0, 0.5656854249492381, 0, 0, 0.4, 0, 0.4],
	[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.5656854249492381, 0.4472135954999579, 0, 0, 0, 0.4, 0, 0.4472135954999579, 0],
	[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.5656854249492381, 0.447213595499958, 0, 0.4, 0, 0.4472135954999579, 0, 0],
	[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.4, 0, 0.4, 0, 0, 0],
]
