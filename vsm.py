import sys
import math
import string
from collections import Counter

import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords


# DOWNLOAD NLTK DATA

try:
    nltk.data.find('tokenizers/punkt')
except LookupError:
    nltk.download('punkt')

try:
    nltk.data.find('tokenizers/punkt_tab')
except LookupError:
    nltk.download('punkt_tab')

try:
    nltk.data.find('corpora/stopwords')
except LookupError:
    nltk.download('stopwords')


# STOPWORDS

stop_words = set(stopwords.words('english'))


# PREPROCESSING

def preprocess(text):

    # lowercase
    text = text.lower()

    # tokenisasi
    tokens = word_tokenize(text)

    hasil = []

    for word in tokens:

        # hapus tanda baca
        if word in string.punctuation:
            continue

        # hapus stopwords
        if word in stop_words:
            continue

        hasil.append(word)

    return hasil


# TF FUNCTION

def tf(freq):

    if freq > 0:
        return 1 + math.log10(freq)

    return 0


# COSINE SIMILARITY

def cosine_similarity(doc_vector, query_vector):

    # dot product
    dot = 0

    for term in query_vector:

        dot += doc_vector.get(term, 0) * query_vector[term]

    # panjang vector dokumen
    doc_length = math.sqrt(
        sum(value ** 2 for value in doc_vector.values())
    )

    # panjang vector query
    query_length = math.sqrt(
        sum(value ** 2 for value in query_vector.values())
    )

    # hindari pembagian nol
    if doc_length == 0 or query_length == 0:
        return 0

    return dot / (doc_length * query_length)


# ARGUMEN COMMAND LINE

if len(sys.argv) != 3:
    print("Usage: python vsm.py base.txt query.txt")
    sys.exit(1)

base_file  = sys.argv[1]
query_file = sys.argv[2]


# BACA BASE.TXT

documents = {}

with open(base_file, "r", encoding="utf-8") as f:

    files = f.read().splitlines()


# BACA DOKUMEN

for file in files:

    with open(file, "r", encoding="utf-8") as d:

        text = d.read()

    documents[file] = preprocess(text)


# BACA QUERY

with open(query_file, "r", encoding="utf-8") as q:

    query_text = q.read()

query = preprocess(query_text)


# DEBUG QUERY

print("\nQUERY :")
print(query)


# DEBUG DOKUMEN

print("\nDOCUMENTS :")

for file, words in documents.items():

    print(file, "=", words[:20])


# DOCUMENT FREQUENCY

df = {}

for doc_words in documents.values():

    unique_terms = set(doc_words)

    for term in unique_terms:

        df[term] = df.get(term, 0) + 1


# IDF

N = len(documents)

idf = {}

for term, n in df.items():

    idf[term] = math.log10(N / n)


# TF-IDF DOKUMEN

weights = {}

for file, words in documents.items():

    counter = Counter(words)

    weights[file] = {}

    for term, freq in counter.items():

        tfidf = tf(freq) * idf[term]

        weights[file][term] = tfidf


# TF-IDF QUERY

query_counter = Counter(query)

query_weights = {}

for term, freq in query_counter.items():

    if term in idf:

        query_weights[term] = tf(freq) * idf[term]


# DEBUG QUERY VECTOR

print("\nQUERY VECTOR :")
print(query_weights)


# COSINE SIMILARITY

results = {}

for file, vector in weights.items():

    similarity = cosine_similarity(vector, query_weights)

    results[file] = similarity


# SORT RANKING

ranking = sorted(
    results.items(),
    key=lambda x: x[1],
    reverse=True
)


# OUTPUT TERMINAL

print("\nHASIL RANKING DOKUMEN\n")

for file, score in ranking:

    print(file, "=", round(score, 4))


# SIMPAN INDEX.TXT

with open("index.txt", "w", encoding="utf-8") as idx:

    for term in sorted(df.keys()):

        idx.write(term + ": ")

        isi = []

        for i, (file, vector) in enumerate(weights.items(), start=1):

            if term in vector:

                isi.append(f"{i},{round(vector[term],4)}")

        idx.write(" ".join(isi))
        idx.write("\n")


# SIMPAN WEIGHTS.TXT

with open("weights.txt", "w", encoding="utf-8") as w:

    for file, vector in weights.items():

        w.write(file + ": ")

        isi = []

        for term, value in vector.items():

            isi.append(f"{term},{round(value,4)}")

        w.write(" ".join(isi))
        w.write("\n")


# SIMPAN RESPONSE.TXT

with open("response.txt", "w", encoding="utf-8") as r:

    valid_docs = [
        item for item in ranking if item[1] > 0.001
    ]

    r.write(str(len(valid_docs)) + "\n")

    for file, score in valid_docs:

        r.write(f"{file} {round(score,4)}\n")


# SELESAI

print("\nFile output berhasil dibuat:")
print("index.txt")
print("weights.txt")
print("response.txt")