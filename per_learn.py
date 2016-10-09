import glob, os, sys

filename = '/Users/shahdhaval/PycharmProjects/Perceptron/test'

features = {}
bias = 0



for root, subdirs, files in os.walk(filename):
    if(os.path.basename(os.path.normpath(root)) == "spam"):


        print('hello')
        os.chdir(root)
        for file in glob.glob("*.txt"):
            words_in_file = []
            sum = 0

            with open(file, "r", encoding="latin1") as f1:
                for line in f1:
                    for word in line.strip().split():
                        words_in_file.append(word)

                        if word not in features:
                            features[word] = 0

                        sum = sum + features[word]              #get the sum of weights of all the words present in the file

                alpha = sum + bias

        if 1 * alpha <= 0:

            for word in words_in_file:
                features[word] = features[word] + 1

            bias = bias + 1

    elif(os.path.basename(os.path.normpath(root)) == "ham"):

        print('hello')


        os.chdir(root)

        for file in glob.glob("*.txt"):

            words_in_file = []
            sum = 0

            with open(file, "r", encoding="latin1") as f1:
                for line in f1:
                    for word in line.strip().split():

                        words_in_file.append(word)

                        if word not in features:
                            features[word] = 0

                        sum = sum + features[word]              #get the sum of weights of all the words present in the file

                alpha = sum + bias

        if 1 * alpha <= 0:
            for word in words_in_file:
                features[word] = features[word] - 1

            bias = bias - 1

print(features)
