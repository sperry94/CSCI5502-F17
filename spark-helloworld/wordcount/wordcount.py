from pyspark import SparkContext

sc = SparkContext()

# read the loremipsum.txt file
loremipsum_lines = sc.textFile("/user/wordcount/loremipsum.txt")

# convert to words, map words to a tuple of (word, count), then reduce word
# mappings by matching the (word, count) tuples by word and summing the count
out = loremipsum_lines.flatMap(lambda line: line.split()) \
    .map(lambda word: (word.strip(".,"), 1)) \
    .reduceByKey(lambda word_count1, word_count2: word_count1 + word_count2) \
    .collect()

# print results
for (word, wordCount) in out:
    print("[" + word + "]: " + str(wordCount))
