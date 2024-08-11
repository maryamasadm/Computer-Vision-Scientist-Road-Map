*Basic Concept

	•	Neuron
	•	Cell Body : brain of neuron 
	•	Dendrites : it receives the messages from the other cells: receivers 
	•	Axon: it transmits messages or signal to other cells: Transformers
	•	Terminals: it passes signals to other neurons 
 
*Neural network 

	•	Input layer
	•	Hidden layer
	•	Output layer
	•	Weights: it gives the ability to neuros which signal is important or not, which one pass which one not
	•	Bias: A constant value to adjust output and fit the data for accurate output
	•	Activation function
	•	Cost function
	•	Gradient Decent optimization
	•	Learning rate
	•	Forwards and Backwards Backpropagation

*Activation function

It is used to determine the output of neural network like yes or no. 
It maps the resulting values in between 0 to 1 or -1 to 1 etc. (depending upon the function).

The Activation Functions can be basically divided into 2 types:

	•	Linear Activation Function
	•	Threshold function
	•	Non-linear Aktivation Funktion
	•	Sigmoid function 
 
It has non linearity, it has analog activation. The sigmoid is a mathematical function that maps input values to a value between 0 and 1, making it useful for binary classification and logistic regression problems.

	•	Hyperbolic Tangent function 
It is similar to sigmoid function, the value is between -1 and 1. It can be reformulated to sigmoid function. The slop of change in the middle part is stronger than sigmid
	•	ReLU
It is very famous function, if x is above 0 is x, otherwise it is 0. It prevents activation of neurons and the function actually help to not have a dense network of neurons, it is computationally cheaper. 
Which function we should use? It depends
Do we have a regression model or classification model? ReLU , you can use and training is faster, Sigmoid is good for classification, it depends to data , model etc

*Cost function

It is the difference between the predicted output and the Actual value. The result of cost function will be feedbacked to the neural network, it will be used to adjust the weights. The goal is changing the weights that minimizing the cost weight.

Gradient decent optimization
Gradient is how much the output changes, if the input changes
We have two type of gradient decent:
	•	Batch Gradient descent: we give the whole rows to the network and then update the weights. Redundant computation, high computational time, cannot deal with non-convex functions
	•	Stochastic Gradient Descent: we give rows by rows to the network, low computational time, can find the global optimum , it is better, we call it SGD as well. In SGD, instead of using the entire dataset for each iteration, only a single random training example (or a small batch) is selected to calculate the gradient and update the model parameters

*Learning rate
To find out the global minimum, it should not be too high and we don’t have convergence but divergence, if it is too low, it would be too slow

*Forwards and Backwards Backpropagation

We give our data as input layer, we give this to hidden layers and neurons, based on weights that initially are random initialized, the output will be created and will be compared to the actual values to compute the cost function, then we adjust the weights in backpropagation. The weights that are responsible for those errors are being updated. This process will be repeated to compute the minimum the cost function.   This is the simplest network that we call it Feedforward backward network. 
Convolutional layer

*What is image filter(kernel)?

In image processing, a kernel, convolution matrix, or mask is a small matrix used for blurring, sharpening, embossing, edge detection, and more. This is accomplished by doing a convolution between the kernel and an image.
Typically filters are 3*3, it can be 5*5 or more, but mostly are 3*3.

ref
if we apply 3*3 filters on image and do convolutional operation, we will have feature map. Rule of thump:
if we have 7*7 image and we apply 3*3 filters, we will have 5*5 feature map. 
Feature map size = [(W−K)/S]+1
Padding
Add pixels to the image to increase chance of some pixels to be chosen in the feature maps, the pixels in the border of image has less chance to be in feature maps. Another reason for having padding is having the same size of feature map as size of the original image. Value of these padding are 0 , around of the image. We can have 1 or 2 etc layers of padding. 
you can use this formula [(W−K+2P)/S]+1.
	•	W is the input volume - in your case 128
	•	K is the Kernel size - in your case 5
	•	P is the padding - in your case 0 i believe
	•	S is the stride - which you have not provided.
Image 7*7 , filter 3*3 , feature map 7*7
Pooling layer
We have different approach for pooling. 
Maxpooling: in a window we choose the max value in the pixels of image, we can not only reduce the dimension of input layer ,but also we extract important features.
(M-p/s )+ 1
Min pool compute the average of the values inside of the window.
Flattening layer
After pooling layer we will have many polled feature maps, but to give it to fully connected layer we need to flatten them to 1 D, we use flattening layer
Input layer, convolutional layer, pooling layer, ReLu activation layer (to introduce non linearity), convolutional layer, pooling layer, .., flattening layer to make it one dimension to give it to fully connected layer. 

*Stride 

Stride determines how many squares or pixels our filters skip when they move across the image, from left to right and from top to bottom. 
Stride is a Convolution Neural Network technique which has two main features. The first is to reduce the size of the output feature map. This is because the filter only overlaps with a subset of the input feature map so that the output feature map will be small, and it helps reduce the computational complexity.
The second is the overlap of the receptive field. The receptive field is the area of the input feature map that is used to calculate the output of a neuron. 
For example, a stride of 2 reduces the overlap of receptive fields by half because the filter will overlap with half of the receptive fields in the previous layer. It helps prevent the CNN from learning redundant features.
ref

