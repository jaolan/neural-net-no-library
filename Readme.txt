neural-net-from-scratch takes 4 arguments at the command line:

-training file (flat file)
-test file (flat file)
-learning rate (alpha)
-number of iterations

This program uses the gradient descent algorithm for training a sigmoid unit and updating weights.

The program will train on the training file over the given number of training iterations. When finished, it will train the sigmoid unit on the testing file and display the accuracy of both training and testing instances.

Note -- Number of iterations can be greater than the number of training instances in a file. The program will simply just train from the beginning of the file keeping the learned sigmoid.
