import argparse

__author__ = 'doctorru - github@'

def main():
    parser = argparse.ArgumentParser(description='Sort and remove duplicated words from a file and write it to a new '
                                                 'file (append mode)')
    parser.add_argument('fileInput', metavar = '<source file>', help = 'Original file')
    parser.add_argument('fileOutput', metavar = '<output file>', help = 'Destination file')

    args = parser.parse_args()
    fileInput =  args.fileInput
    fileOutput = args.fileOutput

    words = []

    try:
        fileName = open(fileInput,'r')

        for line in fileName:
            words.append(line.strip('\n').strip())

        fileName.close()

        totalWordsBefore =  str(len(words))
        words = list(set(words))
        totalWordsAfter = str(len(words))

        print "[*] Original words: " + totalWordsBefore
        print "[*] Unique words: " + totalWordsAfter

    except Exception, e:
        print e
        exit(0)


    print "[*] Sorting... "
    words.sort()
    print "[*] Writing file: " + fileOutput

    try:
        fileName = open(fileOutput,'a')

        for each in words:
            fileName.write("%s\n" % each)

        fileName.close()

        print "[*] Done"
        exit(0)

    except Exception, e:
        print e
        exit(0)


if __name__ == "__main__":
    main()
