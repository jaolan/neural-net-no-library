import math
import sys

def sigmoid( val ):
   return( 1 / (1+math.exp(-val)) )

def initialize_weights(w):
    for i in range(len(train_data)-1):
        w[i] = 0
    return w

#passed 3 arrays, since dot[i] = w[i] * x[i] and total_dot += dot[i]
def dot_product(dot, weight, attribute):
    total_dot = 0
    for i in range(len(headers) - 1):
        dot[i] = weight[i] * attribute[i]
        total_dot += (weight[i] * attribute[i])
        #print total_dot
    return total_dot

def error_function(correct, total_dot):
    return correct - sigmoid(total_dot)

#return for every weight in row, passed weight array, check calcd err what does it do
def update_weight(learn_rate, weight, calculated_error, derived_sigmoid):
    return weight + ( (learn_rate * weight) * calculated_error * derived_sigmoid )

#need to pass dot[i] NO???, do for each column
def sigmoid_derivative(dot):
    return sigmoid(dot) * (1 - sigmoid(dot))

def line_output(iteration):
    print "For iteration %s: " % iteration,
    for i in range((len(headers)-1)):
        print " w(%s): %s, " % ( headers[i], w[i]) ,
    print " output=", total_dot

#Use 0.5 as the classification threshold (i.e., classify the instance as 1 if the outputs a value that is at least 0.5; otherwise classify the instance as 0).
#somewhere, if classify == 1, correct += 1
def classify(total_dot):
    if total_dot >= 0.5:
        return 1
    else:
        return 0

def get_num_instances(num_instances):
   for line in open(train_file):
      num_instances += 1
   return num_instances


def get_num_columns():
   for line in open(train_file):
      columns = line.split()
      return len(columns)

def initialize_weights(w):
   for i in range(len(train_data)):
      w[i] = 0
   return w

def print_accuracy(correct, num_iterations):
    accuracy = correct / num_iterations
    if in_training is True:
        print ("Accuracy on training set (%s instances):  %s %%" % (num_iterations, accuracy))
    else:
        print ("Accuracy on testing set (%s instances):  %s %%" % ( num_iterations, accuracy))

#getting cmdline args
train_file = sys.argv[1]
test_file = open(sys.argv[2])
learn_rate = int(sys.argv[3])
num_iterations = int(sys.argv[4])

num_instances = 0
dot = [None]
w = [None]
train_data = [None]
headers = [None]
total_dot = 0
lines_to_train = 0
num_correct = 0
num_cols = 0
iteration = 0
leftover_lines = 0
get_num_instances(num_instances)
num_cols = get_num_columns()
dot = [None] * (num_cols - 1 )
w = [None] * (num_cols - 1 )
train_data = [None] * (num_cols - 1)
headers = [None] * (num_cols - 1)
derived_sigmoid = [None] * (num_cols - 1)
initialize_weights(w)

#get the header close file
for line in open(train_file):
    headers = line.split()
    break
in_training = True

######### training ##########
if num_iterations > num_instances:
    leftover_lines = num_iterations - num_instances
    #train for num instances(), then train for leftover
    with open(train_file) as train_file:
        next(train_file)
        for line in train_file:
            iteration += 1
            train_data = list((int(x) for x in line.split()))
            total_dot = dot_product(dot, w, train_data)
            derived_sigmoid = sigmoid_derivative(total_dot)
            calculated_error = error_function(train_data[num_cols - 1], total_dot)
            # update weights for i in len
            for i in range(len(train_data) - 1):
                update_weight(learn_rate, w[i], calculated_error, derived_sigmoid)
            if classify(total_dot) == train_data[num_cols - 1]:
                num_correct += 1
            line_output(iteration)
    iteration = 0
    with open(sys.argv[1]) as train_file:
        next(train_file)
        for line in train_file:
            iteration += 1
            train_data = list((int(x) for x in line.split()))
            total_dot = dot_product(dot, w, train_data)
            derived_sigmoid = sigmoid_derivative(total_dot)
            calculated_error = error_function(train_data[num_cols - 1], total_dot)
            # update weights for i in len
            for i in range(len(train_data) - 1):
                # print w[i]
                update_weight(learn_rate, w[i], calculated_error, derived_sigmoid)
            if classify(total_dot) == train_data[num_cols - 1]:
                num_correct += 1
            line_output(iteration)
            #exit loop when total iterations done
            if iteration > leftover_lines:
                break
else:
    # train for num instances(), then train for leftover
    with open(train_file) as train_file:
        next(train_file)
        for line in train_file:
            iteration += 1
            train_data = list((int(x) for x in line.split()))
            total_dot = dot_product(dot, w, train_data)
            derived_sigmoid = sigmoid_derivative(total_dot)
            calculated_error = error_function(train_data[num_cols - 1], total_dot)
            # update weights for i in len
            for i in range(len(train_data) - 1):
                update_weight(learn_rate, w[i], calculated_error, derived_sigmoid)
            if classify(total_dot) == train_data[num_cols - 1]:
                num_correct += 1
            line_output(iteration)

            # exit loop when total iterations done
            if iteration > num_iterations:
                break


# training/testing over, check accuracy
print_accuracy(num_correct, num_iterations)

########### test time ###############
for line in open(sys.argv[2]):
    headers = line.split()
    break
in_training = False
#need to skip first line in training
with open(sys.argv[2]) as train_file:
    next(train_file)
    for line in train_file:
        iteration += 1
        train_data = list((int(x) for x in line.split()))
        total_dot = dot_product(dot, w, train_data)
        derived_sigmoid = sigmoid_derivative(total_dot)
        calculated_error = error_function(train_data[num_cols-1], total_dot)
        #update weights for i in len
        for i in range(len(train_data)-1):
            update_weight(learn_rate, w[i], calculated_error, derived_sigmoid)
        if classify(total_dot) == train_data[num_cols-1]:
            num_correct += 1
        line_output(iteration)

#training/testing over, check accuracy
print_accuracy(num_correct, num_iterations)

#problems: weights always 0, even if init to 1, calculations returning 0s, fix asap

