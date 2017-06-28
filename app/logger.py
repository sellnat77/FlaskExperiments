import os


def log(text, level=2, outFile='log.txt'):
    text = str(text)
    if level == 0:
        return True

    if level == 3:
        with open(outFile, 'a') as logger:
            logger.write(text)
            logger.close()
        print(text)
        return True

    if level == 2:
        print(text)

    if level == 1:
        with open(outFile, 'a') as logger:
            logger.write(text)
            logger.close()

if __name__ == '__main__':
    log('hello world',2,'temp.txt')
