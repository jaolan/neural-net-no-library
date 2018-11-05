# Neural-Net-No-Library

**This program uses the gradient descent algorithm for training a sigmoid unit and updating weights.**

The program will train on the training file over the given number of training iterations. When finished, it will test the sigmoid unit on the testing file and display the accuracy of both training and testing file instances.

Note -- Number of iterations can be greater than the number of training instances in a file. The program will simply just train from the beginning of the file keeping the learned sigmoid. Program designed for flat .txt files, but may work with other format flat files delimited by white space.

**neural-net-from-scratch takes 4 arguments at the command line:**
* training file (flat file)
* test file (flat file)
* learning rate (alpha) (typically between 0-1)
* number of iterations

*(in the order presented)*

**Example usage:**

   `<python nn_from_scratch.py training_file.txt testing_file.txt 0.9 300>`
