import glob, os, sys

modelFile = open("per_model.txt", "w", encoding="latin1")

filename = '/Users/shahdhaval/Desktop/CSCI544/Spam or Ham/train'

bias = 0

# This function will update the weights of the features present in the training file

def updateFeatureWeights(file, bias, features, check):

    sum = 0
    for word in file:
        sum = sum + int(features[word])

    alpha = sum + bias

    if check == 1:                                               # spam file
        if 1 * alpha <= 0:
            for word in file:
                features[word] = features[word] + 1
            bias = bias + 1

    if check == -1:
        if -(1 * alpha) <= 0:                                              # ham file
            for word in file:
                features[word] = features[word] - 1
            bias = bias - 1

    return bias, features

# running through all the training data for the given number of iterations

spam_dict = {}
ham_dict = {}
features = {}
spam_file_count = 1
ham_file_count = 1

for root, subdirs, files in os.walk(filename):
    if(os.path.basename(os.path.normpath(root)) == "spam"):
        os.chdir(root)
        for file in glob.glob("*.txt"):
            words = []
            with open(file, "r", encoding="latin1") as f1:
                for line in f1:
                    for word in line.strip().split():
                        words.append(word)
                        if word not in features:
                            features[word] = int(0)

            spam_dict[spam_file_count] = words
            spam_file_count = spam_file_count + 1

    if(os.path.basename(os.path.normpath(root)) == "ham"):
        os.chdir(root)
        for file in glob.glob("*.txt"):
            words = []
            with open(file, "r", encoding="latin1") as f1:
                for line in f1:
                    for word in line.strip().split():
                        words.append(word)
                        if word not in features:
                            features[word] = int(0)

            ham_dict[ham_file_count] = words
            ham_file_count = ham_file_count + 1
Reduced the time complexity of the code
for iteration in range (0, 20):
    for i in range (1, len(spam_dict)+1):
        bias, features = updateFeatureWeights(spam_dict[i], bias, features, 1)
    for i in range (1, len(ham_dict)+1):
        bias, features = updateFeatureWeights(ham_dict[i], bias, features, -1)

# printing the learned model to a text file

print(bias)

modelFile.write(str(bias))
modelFile.write('\n')

for feature in features:
    print_line = feature+" "+str(features[feature])
    modelFile.write(print_line)
    modelFile.write('\n')

modelFile.close()