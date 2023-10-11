import nltk
from nltk.corpus import stopwords
import re
from nltk.stem import RSLPStemmer
import os
import sys

def generate_inverted_index(file_path):
    inverted_index = {}

    nltk.download('rslp')
    nltk.download('stopwords')
    stop_words = set(stopwords.words('portuguese'))

    separators = ' ,.\n!?...'

    with open(file_path, 'r') as file:
        documents = [line.rstrip('\n') for line in file]

    stemmer = RSLPStemmer()
    for idx, document in enumerate(documents):
        document = 'base_samba/' + document
        with open(document, 'r') as document_file:
            terms = re.split(r"[{}]+".format(separators), document_file.read().split(separators)[0])

            word_count = {}
            for term in terms:
                if term != '' and term not in stop_words:
                    term = stemmer.stem(term)  # stem the term
                    word_count[term] = word_count.get(term, 0) + 1

            for word, count in word_count.items():
                inverted_index.setdefault(word, []).append((idx, count))

    with open('index.txt', 'w') as index_file:
        for word, count_list in inverted_index.items():
            indices = ', '.join([f"{idx},{count}" for idx, count in count_list])
            index_file.write(f"{word}: {indices}\n")

    return inverted_index

def boolean_search(query, inverted_index, base_path):
    result = set()
    query_terms = query.lower().split()
    logical_operator = None
    stemmer = RSLPStemmer()

    for term in query_terms:
        if term in {'&', '|', '!'}:
            logical_operator = term
        else:
            term = stemmer.stem(term)
            indexes = {item[0] for item in inverted_index.get(term, set())}

            if logical_operator is None:
                result.update(indexes)
            elif logical_operator == '&':
                result.intersection_update(set(indexes))
            elif logical_operator == '|':
                result.update(indexes)
            elif logical_operator == '!':
                result.difference_update(indexes)

            logical_operator = None

    # Convert the result set to a list of filenames
    filenames = set()
    with open(base_path, 'r') as f:
        documents = [line.rstrip('\n') for line in f]

        for index, filename in enumerate(documents):
            index = int(index)
            for answer in result:
                if index == answer:
                    filenames.add(filename.strip())

    return filenames

def main():
    file_path = sys.argv[1]
    query_path = sys.argv[2]
    output_path = 'answers.txt'

    inverted_index = generate_inverted_index(file_path)

    with open(query_path, 'r') as query_file, open(output_path, 'w') as output_file:
        query = query_file.read().strip()
        results = boolean_search(query, inverted_index, sys.argv[1])

        num_answers = len(results)
        filenames = [os.path.basename(document) for document in results]

        output_file.write(f"Number of Answers: {num_answers}\n")
        output_file.write("Files that solve the query:\n")
        output_file.write("\n".join(filenames))


if __name__ == "__main__":
    main()

