# RPS Teori–Implementasi Terpadu — Social Media Analytics (14 Pertemuan)

**Prinsip:** teori data science (ML & NLP) tetap jangkar, tetapi setiap konsep dimunculkan tepat saat data social media membutuhkannya (just-in-time), lalu langsung diterapkan ke data nyata. Tidak ada teori tanpa implementasi di minggu yang sama; tidak ada implementasi tanpa nama teorinya.

## Tiga lapis penyampaian per pertemuan (150 menit)

1. **Lapis teori (60')** — konsep data science yang dijarkan formal: sampling, TF-IDF, klasifikasi, embedding, topic model, graph metric, LLM reliability.
2. **Lapis implementasi (70')** — terjemahan konsep ke data social media: tokenisasi slang, class imbalance, label codebook, API ke API.
3. **Lapis artefak & validasi (20')** — mahasiswa menghasilkan sesuatu yang diukur (notebook, dataset, memo, dashboard).

## Peta 14 Pertemuan — Teori → Implementasi → Contoh/Luaran

| Mg | Teori DS (jangkar formal) | Implementasi ke data social media | Contoh kasus | Luaran mahasiswa |
|----|----------------------------|-----------------------------------|--------------|------------------|
| 1 | Siklus data, unit analisis, tingkat maturitas deskriptif→preskriptif | Membaca metrik platform sebagai kuantitas terukur vs klaim interpretif | Video viral UMKM snack TikTok (4,2% engagement) | Rencana analisis 2 halaman |
| 2 | Sampling frame & jenis struktur data (histori relasi-api) | Affordance matrix; kenapa feed rekomendasi → sampel "pengguna yang direkomendasikan", bukan populasi | Topik sama di 3 platform (harga BBM / “Pemilu2024”) | Memo komparabilitas 1 halaman |
| 3 | Struktur data formal: JSON relasional, structured vs unstructured, multimodal unit | Field dictionary dari objek API nyata (X, TikTok, YouTube); missingness | 1 post X + 1 video TikTok JSON asli | Kamus field platform |
| 4 | Data engineering: pagination, rate limit, checksum, reproducibility | Kolektor 3 API (tweepy/praw/google-api/atproto) dengan collection log | Arsip topik banjir Jakarta 7 hari | Dataset + collection log |
| 5 | Etika & regulasi sebagai metode: basis hukum, minimasi, retensi | Feasibility memo jalur akses: API, enclave Meta, scraping; ToS vs UU PDP | Kebutuhan data Meta budget nol | Legal-ethics memo |
| 6 | Preprocessing teori: normalisasi, MinHash/LSH dedup, bot heuristics, language ID | Pipeline cleaning pada code-mixing Jawa–Indonesia, emoji, slang "bjb/gws" | Komentar produk UMKM | Dataset bersih + laporan before/after |
| 7 | **UTS** — penguatan integrasi teori: sampling, preprocessing, legalitas | Bedah laporan analis fiktif dengan 5 penyimpangan (mengapa salah secara metode) | Laporan bocor yang disusun dosen | Ujian terstruktur |
| 8 | ML supervised: bag-of-words, TF-IDF, keyphrase, baseline model, overfitting | Tokenisasi slang + emoji; lexicon InSet; bake-off pada komentar TikTok | Komentar skincare lokal | Notebook baseline |
| 9 | Klasifikasi, class imbalance, macro-F1, kalibrasi; NLP: fine-tune BERT, ABSA | Sentimen/emosi dua platform; error analysis; lexicon vs SVM vs transformer | Brand minuman viral X vs TikTok | Laporan metrik + error analysis |
| 10 | Transfer learning & multilingual; zero-shot LLM | IndoBERT/IndoRoBERTa/NusaBERT vs multilingual; 50 sampel salah dikaji | Slang Jakarta/Jawa vs dataset SmSA | Laporan error analysis |
| 11 | Unsupervised: topic modeling, coherence, stabilitas seed; multidimensional framing | LDA vs BERTopic pada diskursus RUU; validasi manual 30 dokumen | Isu RUU / tagar solidaritas internasional | Topik tervalidasi manusia |
| 12 | Graph theory: centrality (degree/betweenness/pageRank), komunitas Louvain/Leiden | Graf reply/mention politik; brokerage antar kubu; Gephi | Konflik opini politik 2024 | Graf + interpretasi |
| 13 | LLM reliability: codebook, agreement statistic (Cohen's κ), bias; agent & tool use; multimodal pipeline | Codebook → prompt → gold set 200 → κ gate; demo agent ringkasan harian + audit angka; Retention curve video pendek | Berita kesehatan hoax vs valid | Laporan κ + demo agent |
| 14 | **UAS + capstone**: integrasi teori ke eksekusi | Data (1) → preprocessing (2) → model (3) → insight (4) → ethical note (5) | Satu isu nyata tim | UAS 30% + capstone 35% + ethics note 10% |

## Peta struktur penyampaian ke mahasiswa (learning path)

```
                    ┌─ minggu ke- ─┐        jalur TEORI (formal DS)
  Siklus data ──▶  1  2  3  4  5  6 │
                    └──────────────┘
                     Jalur A: Foundations
                     (apa itu data SMD, struktur, akuisisi, hukum)

                    ┌──────────────┐        jalur IMPLEMENTASI
                    8  9  10 11    │
                    └──────────────┘
                     Jalur B: Text/NLP ML (kurva naik: lexicon → transformer → topic)

                    ┌─────────┐             jalur TEORI lanjut
                         12  13│
                         └────┘
                     Jalur C: Logika cuối graph & LLM

                    ┌──────────────┐
                          14      │
                    └──────────────┘
                     Jalur D: CAPSTONE — semua teori diterapkan satu isu
```

Pengalaman mahasiswa per sesi (pattern tetap):
```
PRE-READ (mandiri)      : 2 halaman teks formal tentang konsep minggu ini
     ↓
LANGSUNG-LAB (70')      : pakai data social media nyata dulu, sebelum teori diberikan penuh
     ↓
TEORI DISAMPAIKAN (60') : dosen menamai istilah formal dari apa yang baru dilakukan
     ↓
VALIDASI & LAURAN (20') : mahasiswa menghasilkan artefak yang metriknya jelas
     ↓
RAPOR TUGAS [rubrik]    : kebenaran metodologi (40%) · interpretasi (30%) · dokumentasi (30%)
```

## Jejak capstone (semua tugas menjahi satu arah)

| Turun tugas | P2–P3 | P4 | P6 | P8 | P9–P11 | P12 | P13 | P14 |
|---|---|---|---|---|---|---|---|---|
| Kompon capstone | Desain sampling | Dataset | Cleaned data | Baseline | Model utama | Analisis jaringan | Label LLM tervalidasi | Dashboard & presentasi |

## Kenapa struktur ini cocok untuk mahasiswa

1. **Teori tetap teruji:** semua konsep DS formal (TF-IDF, fine-tune, coherence, centrality, κ) disampaikan eksplisit, tidak dilunakkan.
2. **Tidak ada konsep "melayang":** setiap teori harus punya pasangan implementasi di minggu yang sama — paksaan ini membuat mahasiswa selalu melihat guna konsep.
3. **Artefak di tiap ujung minggu:** rapat kelas menghasilkan file nyata; penilaian berbasis rubrik, bukan hafalan.
4. **Capstone tumpang tindih:** tugas tidak terbuang — semuanya menyusun proyek akhir.
