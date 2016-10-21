import glob, os, sys, random

modelFile = open("per_model.txt", "w", encoding="latin1")

filename = ' '.join(sys.argv[1:])

bias = 0
avg_bias = 0
# This function will update the weights of the features present in the training file

def updateFeatureWeights(word_dict, bias, features, c, avg_weights, avg_bias, check):

    sum = 0
    for word in word_dict[0]:
        sum = sum + int(features[word])

    alpha = sum + bias

    if word_dict[2] == 1:                                             # spam file
        if 1 * alpha <= 0:
            for word in word_dict[1]:
                features[word] = features[word] + 1
                avg_weights[word] = avg_weights[word] + c
            bias = bias + 1
            avg_bias - avg_bias + c

    if word_dict[2] == 2:
        if -(1 * alpha) <= 0:                                              # ham file
            for word in word_dict[1]:
                features[word] = features[word] - 1
                avg_weights[word] = avg_weights[word] - c
            bias = bias - 1
            avg_bias = avg_bias - c

    c = c+1

    return bias, features, c, avg_weights, avg_bias

spam_dict = {}
ham_dict = {}
features = {}
avg_weights = {}
file_count = 1
c = 1

for root, subdirs, files in os.walk(filename):
    if(os.path.basename(os.path.normpath(root)) == "spam" or os.path.basename(os.path.normpath(root)) == "ham"):
        os.chdir(root)
        for file in glob.glob("*.txt"):
            words = []
            unique_words=[]
            with open(file, "r", encoding="latin1") as f1:
                contents = f1.readlines()
                for line in range(len(contents)):
                    for word in contents[line].strip().split():
                        if word not in unique_words:
                            unique_words.append(word)
                        words.append(word)
                        if word not in features:
                            features[word] = int(0)
                            avg_weights[word] = int(0)

            if(os.path.basename(os.path.normpath(root)) == "spam"):
                spam_dict[file_count] = words, unique_words, 1
                file_count = file_count + 1

            elif(os.path.basename(os.path.normpath(root)) == "ham"):
                spam_dict[file_count] = words, unique_words, 2
                file_count = file_count + 1

# running through all the training data for the given number of iterations

for iteration in range (0, 30):

    r = list(range(1, len(spam_dict)+1))
    random.shuffle(r)
    for i in r:
        bias, features, c, avg_weights, avg_bias = updateFeatureWeights(spam_dict[i], bias, features, c, avg_weights, avg_bias, 1)

# printing the learned model to a text file


avg_bias = bias - ((1/c)*avg_bias)

modelFile.write(str(avg_bias))
modelFile.write('\n')

for feature in avg_weights:
    avg_weights[feature] = features[feature] - ((1/c)*avg_weights[feature])
    print_line = feature+" "+str(avg_weights[feature])
    modelFile.write(print_line)
    modelFile.write('\n')

modelFile.close()