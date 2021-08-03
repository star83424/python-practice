import sys

"""
A word chain is a sequence of words in which every word except the first one starts with the last letter of the previous word. You are given a sequence of words. Output the length of the longest prefix of the sequence which forms a valid word chain. One-word chain is always valid.

The first line of the input contains an integer N - the number of words in the sequence. 1 <= N <= 10.
The following N lines contain the words of the sequence, one word per line. Each word is between 1 and 10 characters long and consists of lowercase letters of English alphabet.

Example

input

4
the
eagle
eats
snakes

output

4

input

7
snakes
seldom
munch
on
north
highland
ducks

output

3

In the first example, the whole sequence is a valid word chain.
In the second example, the longest prefix which is a word chain is "snakeS SeldoM Munch". The last four words of the sequence are a longer word chain but they are not a prefix of the sequence.
"""
def find_prefix_word_chain():
    word_count = int(sys.stdin.readline())

    # start with the last letter of the first one
    prev_end = sys.stdin.readline().strip('\n')[-1]

    for i in range(1, word_count):
        word = sys.stdin.readline().strip('\n')
        if word[0] != prev_end:
            # word chain stops!
            # And the rests are not going to be prefix chain, so return.
            return i

        prev_end = word[-1]
    # the whole word sequence is the answer
    return word_count


"""
You need to transfer some information through a slow datalink as fast as possible. You consider using a file archiver to compress data before sending.

The first line of input contains an integer dataSize - the size of data you need to transfer in bytes. 1 <= dataSize <= 10000.
The second line of input contains an integer transferSpeed - the speed of data transfer through the link, in bytes per second. 1 <= transferSpeed <= 10.
The third line of input contains an integer N - the number of archivers you are considering. 1 <= N <= 2.
The following N lines contain information about archivers, each line describing one archiver with two space-separated integers: processingSpeed - the speed of data processing (both compression and extraction) in bytes per second, and compressionRate - the rate of compression achieved by the archiver (i.e. the size of compressed data divided by the size of original data), in percent. 1 <= processingSpeed <= 100, 1 <= compressionRate <= 99.

Output the minimal time you'll need to send the data through the datalink, including compression and extraction time, rounded up to the nearest integer. Round up only the final answer, not intermediary calculations results.

Example

input

1000
10
2
100 50
60 20

output

40

Sending the data uncompressed will take 1000/10 = 100 seconds.
Using first archiver will take 1000/100 + 1000*0.5/10 + 1000*0.5/100 = 65 seconds.
Using second archiver will take 1000/60 + 1000*0.2/10 + 1000*0.2/60 = 39 1/3 seconds, rounding up to 40 seconds.
"""
def line_1():
    import sys

    # dataSize - the size of data you need to transfer in bytes.
    #             1 <= dataSize <= 10000.
    dataSize = float(sys.stdin.readline())

    # transferSpeed - the speed of data transfer through the link, in bytes per second.
    #             1 <= transferSpeed <= 10.
    transferSpeed = float(sys.stdin.readline())

    # integer N - the number of archivers you are considering.
    #             1 <= N <= 2.  (1 or 2)
    num = int(sys.stdin.readline())

    def getProcessingTime():
        arch = sys.stdin.readline().split(" ")
        # 1 <= processingSpeed <= 100
        processingSpeed = float(arch[0])
        # 1 <= compressionRate <= 99
        compressionRate = float(arch[1]) / 100

        compressedDataSize = dataSize * compressionRate

        return round(
            dataSize / processingSpeed + compressedDataSize / transferSpeed + compressedDataSize / processingSpeed)

    minProcessingTime = getProcessingTime()

    for i in range(1, num):
        minProcessingTime = min(minProcessingTime, getProcessingTime())

    # the answer should be
    print(minProcessingTime)



def archiever_2():
    import sys
    import math
    from decimal import *

    # dataSize - the size of data you need to transfer in bytes.
    #             1 <= dataSize <= 10000.
    dataSize = Decimal(sys.stdin.readline())

    # transferSpeed - the speed of data transfer through the link, in bytes per second.
    #             1 <= transferSpeed <= 10.
    transferSpeed = Decimal(sys.stdin.readline())

    # integer N - the number of archivers you are considering.
    #             1 <= N <= 2.  (1 or 2)
    num = int(sys.stdin.readline())

    def getProcessingTime():
        arch = sys.stdin.readline().split(" ")

        # 1 <= processingSpeed <= 100
        processingSpeed = Decimal(arch[0])

        # 1 <= compressionRate <= 99
        compressionRate = Decimal(arch[1]) / 100
        compressedDataSize = dataSize * compressionRate

        # Round up to the nearest integer
        return math.ceil(
            dataSize / processingSpeed + compressedDataSize / transferSpeed + compressedDataSize / processingSpeed)

    minProcessingTime = getProcessingTime()

    # If more than one archiver
    for i in range(1, num):
        minProcessingTime = min(minProcessingTime, getProcessingTime())

    # the answer should be the minimum processing time
    print(minProcessingTime)

"""
A Fibonacci-like sequence is a sequence of integers a1, a2, ... for which an = an-1+an-2 for all n > 2. You are given the first two elements of the sequence a1 and a2, and the 1-based index n. Output the n-th element of the sequence.

The input data consists of a single line which contains integers a1, a2 and n separated by single spaces. 0 < a1, a2, n <= 10.

Example

input

1 2 3

output

3
"""
def line_fibo():
    import sys

    """
    Get n-th fibo num from a1, a2 
    0 < a1, a2, n <= 10
    """

    def get_fibo_num(a1, a2, n):
        if n == 1:
            return a1

        # if n >= 2, calculate the nth num.
        for i in range(2, n):
            a1, a2 = a2, a1 + a2

        return a2

    # Get the input & turn into integer list
    input = [int(i) for i in sys.stdin.readline().split(" ")]
    # print result
    print(get_fibo_num(input[0], input[1], input[2]))


class LineCommonPlatform:

    @staticmethod
    def main():
        # print(find_prefix_word_chain())

        print("Hi")