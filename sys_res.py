# PROGRAMMER: Angel
# DATE CREATED: 24.04.2020
# REVISED DATE: 11.05.2020

from get_input_args import get_input_args


def get_arg():
    in_arg = get_input_args()
    return in_arg.dir


def sys_res(dir_arg):
    """
    Prints the final results frоm the "Use a Pre-trained Image Classifier to Identify Dog Breeds"
    systematized in a table
       Parameters:
         tuple_files_dic - Tuple with the names of the .txt output files from the run_models_batch.sh script
       Returns:
              None - prints the results as above mentioned.
       """

    # dictionary with key, the name of the output file for the respective cnn, and the value is a list with following results:
    # % dogs-correct, % match-labels, % breeds-correct, % not-a-dog-correct
    final_res = dict()

    tuple_files_res = tuple()

    # check which is the images directory
    if dir_arg == 'pet_images/':
        tuple_files_res = ("resnet_pet-images.txt", "alexnet_pet-images.txt", "vgg_pet-images.txt")
    elif dir_arg == 'uploaded_images/':
        tuple_files_res = ("resnet_uploaded-images.txt", "alexnet_uploaded-images.txt", "vgg_uploaded-images.txt")

    # loop to read through each files and assign the correct values in the final_res dictionary
    for file in tuple_files_res:
        res = []
        with open(file, 'r') as res_file:
            line = res_file.readline()
            while line != "":
                line = line.strip("\n")
                if "pct_correct_dogs" in line:
                    line = line.split(": ")
                    res.append(line[1].strip(" "))

                if "pct_match" in line:
                    line = line.split(": ")
                    res.append(line[1].strip(" "))

                if "pct_correct_breed" in line:
                    line = line.split(": ")
                    res.append(line[1].strip(" "))

                if "pct_correct_notdogs" in line:
                    line = line.split(": ")
                    res.append(line[1].strip(" "))

                line = res_file.readline()

        final_res[file] = res
    # printing the systematized results in a table
    print()
    print(10*"-" + "***systematized results***" + 10*"-")
    print()
    print(120*"-")
    print("|cnn model architecture: |{:25} {:25} {:25} {:25}".format("|% not-a-dog-correct|", "|% dogs-correct|", "|% breeds-correct|", "|% match-labels|" ))
    print(120 * "-")
    for key in final_res:
        pct_dogs_correct = final_res[key][0]
        pct_match_labels = final_res[key][1]
        pct_breeds_correct = final_res[key][2]
        pct_not_a_dog_correct = final_res[key][3]
        cnn = key.split("_")[0]
        empty = ''
        print("{:25} {:25} {:25} {:.1f} {:20} {:25}".format(cnn, pct_not_a_dog_correct, pct_dogs_correct, float(pct_breeds_correct),
                                                            empty, pct_match_labels))
    print(120 * "-")


sys_res(get_arg())
