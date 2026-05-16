# Tugas VSM - Vector Space Model

Tugas Mata Kuliah Aljabar Linear  
Sistem pencarian dokumen sederhana menggunakan Python.

---

# Cara Menjalankan

## 1. Install Terlebih Dahulu

```bash
pip install -r requirements.txt
```

## 2. Menjalankan Program

```bash
python vsm.py base.txt query1.txt
```

Ganti `query1.txt` dengan query yang mau dicoba.  
Tersedia 3 file query:

- `query1.txt`
- `query2.txt`
- `query3.txt`

---

# Isi Folder

```text
vsm/
├── vsm.py            <- program utama
├── requirements.txt  <- library yang dibutuhkan (nltk)
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
```

---

# Cara Kerja

Program ini mencari dokumen yang paling mirip dengan query yang diberikan.

## 1. Preprocessing

Teks dipecah menjadi kata-kata, lalu kata yang dianggap kurang penting (seperti `"the"`, `"is"`, `"and"`) dihapus.

Contoh:

```python
"artificial intelligence systems technology"
→ ['artificial', 'intelligence', 'systems', 'technology']
```

---

## 2. TF-IDF

Setiap kata diberikan bobot.  
Kata yang sering muncul di satu dokumen tetapi jarang muncul di dokumen lain akan memiliki bobot lebih tinggi.

- **TF** = seberapa sering kata muncul di dokumen tersebut
- **IDF** = seberapa langka kata tersebut di semua dokumen
- **TF-IDF** = TF × IDF

---

## 3. Cosine Similarity

Dokumen dan query diubah menjadi vektor, lalu dihitung tingkat kemiripannya.

- Nilai `1.0` = sama persis
- Nilai `0` = tidak memiliki kemiripan sama sekali

---

# Contoh Output

## Di Terminal

```text
QUERY :
['artificial', 'intelligence', 'systems', 'technology']

HASIL RANKING DOKUMEN

doc4.txt = 0.0325
doc3.txt = 0.0257
doc1.txt = 0.0256
doc5.txt = 0.0218
doc2.txt = 0.0
```

## response.txt

```text
4
doc4.txt 0.0325
doc3.txt 0.0257
doc1.txt 0.0256
doc5.txt 0.0218
```

Baris pertama = jumlah dokumen yang relevan  
Baris berikutnya = nama file beserta nilai kemiripannya.

---

# Catatan

- File output (`index.txt`, `weights.txt`, `response.txt`) otomatis overwrite setiap kali program dijalankan
- Jika data NLTK belum terdownload, program akan mendownload otomatis saat pertama kali dijalankan
- Dokumen harus berbahasa Inggris karena stopwords yang digunakan menggunakan bahasa Inggris