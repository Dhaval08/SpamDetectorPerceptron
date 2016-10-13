import glob, os, sys, random

modelFile = open("per_model.txt", "w", encoding="latin1")

filename = '/Users/shahdhaval/Desktop/CSCI544/Spam or Ham/train'

bias = 0
# This function will update the weights of the features present in the training file

def updateFeatureWeights(word_dict, bias, features, check):

    sum = 0
    for word in word_dict[0]:
        sum = sum + int(features[word])

    alpha = sum + bias

    if word_dict[1] == 1:                                             # spam file
        if 1 * alpha <= 0:
            for word in word_dict[0]:
                features[word] = features[word] + 1
            bias = bias + 1

    if word_dict[1] == 2:
        if -(1 * alpha) <= 0:                                              # ham file
            for word in word_dict[0]:
                features[word] = features[word] - 1
            bias = bias - 1

    return bias, features

# running through all the training data for the given number of iterations

spam_dict = {}
ham_dict = {}
features = {}
file_count = 1

for root, subdirs, files in os.walk(filename):
    if(os.path.basename(os.path.normpath(root)) == "spam" or os.path.basename(os.path.normpath(root)) == "ham"):
        os.chdir(root)
        for file in glob.glob("*.txt"):
            words = []
            with open(file, "r", encoding="latin1") as f1:
                contents = f1.readlines()
                for line in range(len(contents)):
                    for word in contents[line].strip().split():
                        words.append(word)
                        if word not in features:
                            features[word] = int(0)

            if(os.path.basename(os.path.normpath(root)) == "spam"):
                spam_dict[file_count] = words, 1
                file_count = file_count + 1

            elif(os.path.basename(os.path.normpath(root)) == "ham"):
                spam_dict[file_count] = words, 2
                file_count = file_count + 1

r = list(range(1, len(spam_dict)+1))
random.shuffle(r)

for iteration in range (0, 20):
    for i in r:
        bias, features = updateFeatureWeights(spam_dict[i], bias, features, 1)

# printing the learned model to a text file

modelFile.write(str(bias))
modelFile.write('\n')

for feature in features:
    print_line = feature+" "+str(features[feature])
    modelFile.write(print_line)
    modelFile.write('\n')

modelFile.close()