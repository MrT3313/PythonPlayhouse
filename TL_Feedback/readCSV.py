import csv

def open_and_read_CSV(userFilePath):
    # print('INSIDE: open&read csv')
    with open(userFilePath, 'r') as userCSV:
        reader = csv.reader(userCSV)
        # print('reader from function: ', reader, type(reader))

        userFile = []
        for row in reader:
            userFile.append(row)
        # print(userFile)
        # print('EXAMPLE ROW',userFile[len(userFile)-1])
        # print(type(userFile))

    return userFile