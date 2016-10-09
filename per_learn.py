import glob, os, sys

modelFile = open("per_model.txt", "w", encoding="latin1")

filename = '/Users/shahdhaval/PycharmProjects/Perceptron/test'

features = {}
bias = 0

# This function will update the weights of the features present in the training file

def updateFeatureWeights(file, bias, features, check):

   words_in_file = []
   sum = 0
   with open(file, "r", encoding="latin1") as f1:
       for line in f1:
           for word in line.strip().split():
               words_in_file.append(word)
               if word not in features:
                   features[word] = 0
               sum = sum + features[word]

   alpha = sum + bias

   if 1 * alpha <= 0:
       if check == 1:                                               # spam file
           for word in words_in_file:
               features[word] = features[word] + 1
           bias = bias + 1

       if check == -1:                                              # ham file
           for word in words_in_file:
               features[word] = features[word] - 1
           bias = bias - 1

   return bias, features


spam_files = 0
ham_files = 0
first_iteration = True

# running through all the training data for the given number of iterations

for iteration in range (0, 20):

    for root, subdirs, files in os.walk(filename):
        if(os.path.basename(os.path.normpath(root)) == "spam"):

            os.chdir(root)
            for file in glob.glob("*.txt"):
                if first_iteration == True:
                    spam_files = spam_files + 1
                bias, features = updateFeatureWeights(file, bias, features, 1)  #this function will return the updated bias and weights

        elif(os.path.basename(os.path.normpath(root)) == "ham"):

            os.chdir(root)
            for file in glob.glob("*.txt"):
                if first_iteration == True:
                    ham_files = ham_files + 1
                bias, features = updateFeatureWeights(file, bias, features, -1)  #this function will return the updated bias and weights

    first_iteration = False

total_files = spam_files + ham_files

# printing the learned model to a text file

modelFile.write(str(bias))
modelFile.write('\n')

for feature in features:
    print_line = feature+" "+str(features[feature])
    modelFile.write(print_line)
    modelFile.write('\n')

modelFile.close()