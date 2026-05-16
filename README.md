# Tugas VSM - Vector Space Model

Tugas Mata kuliah Aljabar Linear 
sistem pencarian dokumen sederhana pake python.


# Cara Menjalankan

# 1. Install Terlebih dahulu


pip install -r requirements.txt


# 2. Menjalankan Program


python vsm.py base.txt query1.txt


ganti `query1.txt` dengan query yang mau dicoba, ada 3 file query (query1.txt, query2.txt, query3.txt).

# Isi Folder

vsm/
├── vsm.py            <- program utama
├── requirements.txt  <- library yang dibutuhin (nltk)
├── base.txt          <- daftar nama file dokumen
├── query1.txt        <- query 1
├── query2.txt        <- query 2
├── query3.txt        <- query 3
├── doc1.txt          <- dokumen 1 
├── doc2.txt          <- dokumen 2 
├── doc3.txt          <- dokumen 3 
├── doc4.txt          <- dokumen 4 
├── doc5.txt          <- dokumen 5 
├── index.txt         <- output: inverted index
├── weights.txt       <- output: bobot tiap term
└── response.txt      <- output: hasil ranking

# Cara Kerja

program ini mencari dokumen yang paling mirip dengan query yang diberikan. caranya:

*1. Preprocessing*
teks dipecah jadi kata-kata, terus kata yang dinggap kurang penting (seperti "the", "is", "and") dihapus.
contoh: "artificial intelligence systems technology" → ['artificial', 'intelligence', 'systems', 'technology']

*2. TF-IDF*
setiap kata dikasih bobot. kata yang sering muncul di satu dokumen tapi jarang di dokumen lain, bobotnya lebih tinggi.
- TF = seberapa sering kata muncul di dokumen itu
- IDF = seberapa langka kata itu di semua dokumen
- TF-IDF = TF × IDF

*3. Cosine Similarity*
dokumen dan query diubah jadi vektor, lalu dihitung kemiripannya. nilai 1.0 = sama persis, nilai 0 = tidak ada kemiripan sama sekali.

# Contoh Output

*di terminal:*
QUERY :
['artificial', 'intelligence', 'systems', 'technology']

HASIL RANKING DOKUMEN

doc4.txt = 0.0325
doc3.txt = 0.0257
doc1.txt = 0.0256
doc5.txt = 0.0218
doc2.txt = 0.0

*response.txt:*

4
doc4.txt 0.0325
doc3.txt 0.0257
doc1.txt 0.0256
doc5.txt 0.0218


baris pertama = jumlah dokumen yang relevan, baris berikutnya = nama file dengan nilai kemiripannya.


# Catatan

- file output (index.txt, weights.txt, response.txt) otomatis overwrite setiap kali program dijalankan
- jika NLTK belum terdownload data didalamnya, program akan mendownload otomatis pada saat program pertama kali jalan
- dokumen harus bebahasa inggris karena stopwords yang digunakan berbahasa inggris 