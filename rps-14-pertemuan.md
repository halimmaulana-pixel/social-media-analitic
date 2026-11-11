# RPS — Social Media Analytics (14 Pertemuan)

**Mata Kuliah:** Social Media Analytics · **Beban:** 3 SKS (150 menit/minggu tatap muka + tugas lab mandiri) · **Semester:** 5 · **Prasyarat:** Statistika Dasar, Pemrograman Dasar (Python/R)
**Fokus:** kurikulum era tren 2024–2026 (multimodal, LLM-annotation, short-video, social commerce, akses data berbayar)

---

## 1. CPMK & Peta 14 Pertemuan

| CPMK | Rumusan | Pertemuan |
|---|---|---|
| CPMK-1 | Menjelaskan ruang lingkup, jenis data, ekosistem platform, jalur akses data, serta etika/regulasi (UU PDP, ToS platform) dalam analitik media sosial | 1–5 |
| CPMK-2 | Mengumpulkan dan membersihkan data media sosial melalui API resmi dan sumber yang sah, dengan dokumentasi sampling frame dan bias | 4–6 |
| CPMK-3 | Menerapkan teknik analisis teks (text mining, sentiment/emosi, topic modeling, NLP berbasis transformer dan model Bahasa Indonesia) untuk menghasilkan temuan yang terukur | 8–11 |
| CPMK-4 | Menganalisis struktur jaringan, difusi, konten multimodal/short-video menggunakan metrik yang tepat | 12–13 |
| CPMK-5 | Mengevaluasi kualitas data, bias, dan reliabilitas label (termasuk label LLM), lalu menyajikan temuan sebagai capstone terintegrasi | 7, 14 |

| Mg | Materi | Bukti penilaian |
|---|---|---|
| 1 | Fondasi & ruang lingkup SMA | Kuis konsep + rencana analisis |
| 2 | Ekosistem platform & data affordance | Tabel komparabilitas platform |
| 3 | Jenis data & field dictionary | Kamus field dataset |
| 4 | Akuisisi data via API resmi | Dataset + collection log |
| 5 | Akses gated, biaya, scraping & legalitas | Catatan legal/etik + feasibility memo |
| 6 | Preprocessing data sosial | Dataset bersih + laporan cleaning |
| 7 | **Evaluasi Tengah Semester (UTS)** | Ujian tertulis/tugas terstruktur |
| 8 | Text mining dasar & lexicon | Notebook baseline + bake-off metode |
| 9 | Sentiment & emotion analysis | Laporan metrik + error analysis |
| 10 | Lokalisasi Bahasa Indonesia (IndoBERT/NusaBERT/InSet) | Notebook + error analysis |
| 11 | Topic modeling (LDA, BERTopic, STM) | Model + topik tervalidasi manusia |
| 12 | Social Network Analysis & visualisasi | Grafik + laporan interpretasi metrik |
| 13 | LLM sebagai annotator + agentic workflow + short-video/multimodal | Gold set + laporan κ + demo |
| 14 | **Evaluasi Akhir Semester + presentasi capstone** | Dashboard + laporan + presentasi + ethics note |

---

## 2. Rincian per Pertemuan

**Pertemuan 1 — Fondasi & Ruang Lingkup SMA** *(CPMK-1)*
- *Indikator:* dapat menjelaskan definisi, siklus data (akses→analisis→preservasi), ladder descriptive/predictive/prescriptive, unit analisis (post/user/percakapan), dan batasan SMA.
- *Materi:* posisi SMA antara riset pasar, computational social science, dan riset komunikasi; analytics maturity; reproducibility dan dokumentasi.
- *Metode:* kuliah interaktif (75') + demo dashboard komersial (Pulsar/Talkwalker trial) dibandingkan metrik dari data mentah (75').
- *Penilaian:* kuis konsep (5%) + rencana analisis 2 halaman.

**Pertemuan 2 — Ekosistem Platform & Data Affordance** *(CPMK-1)*
- *Indikator:* dapat membandingkan platform (X, TikTok, Instagram, YouTube, Reddit, Bluesky/AT Protocol, Threads) pada ketersediaan data, keterbukaan API, dan logika feed.
- *Materi:* affordance matrix; feed rekomendasi vs follow-graph; open protocol (AT Protocol) vs akses gated (Meta); Bluesky firehose.
- *Metode:* presentasi komparatif + diskusi kasus "platform apa untuk pertanyaan apa".
- *Penilaian:* tugas mini (10%) — 1.000 post di 3 platform, tabulasi field, catatan komparabilitas 1 halaman.

**Pertemuan 3 — Jenis Data & Field Dictionary** *(CPMK-1)*
- *Indikator:* dapat mengklasifikasikan unit data (teks, gambar, video, interaksi/graph, metadata, engagement log) dan merancang kamus field.
- *Materi:* skema per platform; structured vs unstructured; data multimodal sebagai satu unit; implikasi tooling.
- *Metode:* inspeksi objek API (X v2 object, TikTok object, Reddit JSON) di lab.
- *Penilaian:* kamus field (field, tipe, contoh, arti, missingness).

**Pertemuan 4 — Akuisisi Data via API Resmi** *(CPMK-1, 2)*
- *Indikator:* dapat mengumpulkan data via ≥3 API dengan koleksi log yang dapat direproduksi.
- *Materi:* X API v2 tiers, TikTok Research API, YouTube Data API, Reddit API (praw), Bluesky; pagination, rate limit, query operator, quota budgeting; sampling frame (top vs recent, keyword, snowball); arsip + checksum.
- *Metode:* kuliah (60') + lab coding bertahap (90'). Tools: requests/httpx, tweepy, praw, google-api-python-client, atproto.
- *Penilaian:* tugas (10%) — topik sama di 3 platform + collection log (query, tanggal, jumlah, filter).

**Pertemuan 5 — Akses Gated, Biaya, Scraping & Legalitas** *(CPMK-1)*
- *Indikator:* dapat menilai rute akses, biaya, dan kepatuhan hukum/etik untuk sebuah studi.
- *Materi:* Meta Content Library (gated, gratis untuk institusi akademik) dan enclave riset yang mulai berbayar per tim (~USD 371/tim/bulan sejak Jan 2026 — verifikasi); ToS platform; UU PDP No. 27/2022; GDPR; hiQ v. LinkedIn; public ≠ permissible; scraping sopan (rate limit, playwright/trafilatura, yt-dlp) dan arsip.
- *Metode:* studi kasus "budget nol, butuh data Meta/X"; review kelayakan.
- *Penilaian:* feasibility/legal-ethics memo (10%).

**Pertemuan 6 — Preprocessing Data Sosial** *(CPMK-2)*
- *Indikator:* dapat membersihkan dataset mentah menjadi analysis-ready dengan laporan kuantitatif.
- *Materi:* normalisasi informal & code-mixing; hashtag segmentation, mention, URL, emoji; near-duplicate (MinHash/LSH); bot heuristics; language detection (fastText); anonymization; **sampling bias dari filter API**.
- *Metode:* lab pipeline + before/after (jumlah, duplikat, distribusi bahasa).
- *Penilaian:* dataset bersih + laporan cleaning (10%) + notebook reproduksi.

**Pertemuan 7 — Evaluasi Tengah Semester** *(CPMK-1, 2)*
- Bentuk: ujian tertulis/terstruktur (utama) + kumpulkan laporan task 1–3 untuk penilaian formatif.

**Pertemuan 8 — Text Mining Dasar & Lexicon Baseline** *(CPMK-3)*
- *Indikator:* dapat membangun baseline yang dapat dijelaskan dan membandingkan pendekatan lexicon vs supervised vs transformer.
- *Materi:* bag-of-words, n-gram, TF-IDF; keyphrase (RAKE, TextRank); lexicon (VADER, InSet); co-occurrence; k-means baseline; bake-off metode.
- *Metode:* lab (90'). Tools: scikit-learn, nltk, vaderSentiment, InSet.
- *Penilaian:* notebook + tabel metrik baseline (10%).

**Pertemuan 9 — Sentiment & Emotion Analysis** *(CPMK-3)*
- *Indikator:* dapat melatih dan mengevaluasi model sentimen/emosi secara adil pada kelas tidak seimbang.
- *Materi:* lexicon → TF-IDF+SVM → fine-tune BERT/RoBERTa; ABSA; emosi (GoEmotions); sarkasme/negasi; macro-F1, Cohen's κ vs human coder, per-class PR, kalibrasi.
- *Metode:* kuliah (45') + lab fine-tuning (105'). Tools: transformers, datasets, accelerate.
- *Penilai:* tugas analisis (10%) — sentimen kampanye brand di X+TikTok + ABSA + error analysis.

**Pertemuan 10 — Lokalisasi Bahasa Indonesia** *(CPMK-3)*
- *Indikator:* dapat memilih model Indonesia yang tepat dan menganalisis kesalahan model pada data lokal.
- *Materi:* IndoBERT/IndoRoBERTa/NusaBERT, InSet, dataset SmSA/cASA/hoaks, IndoNLU; colloquial spelling, code-mixing, bahasa daerah; zero-shot LLM untuk teks Indonesia dan validasinya.
- *Metode:* lab + error analysis 50 sampel salah klasifikasi.
- *Penilaian:* laporan error analysis (10%).

**Pertemuan 11 — Topic Modeling** *(CPMK-3)*
- *Indikator:* dapat menjalankan dan memvalidasi topik secara kuantitatif dan manusia.
- *Materi:* LDA (Gensim/MALLET), NMF, BERTopic (embeddings + UMAP/HDBSCAN + c-TF-IDF), dynamic/STM, coherence (C_v, NPMI), stabilita antar-seed; framing/agenda analysis.
- *Metode:* lab dua model + validasi manusia 30 dokumen/topik.
- *Penilaian:* notebook + topik tervalidasi (10%). Tools: gensim, bertopic, umap-learn; R: stm.

**Pertemuan 12 — Social Network Analysis & Visualisasi** *(CPMK-4)*
- *Indikator:* dapat membangun jaringan dari data interaksi, menghitung dan menginterpretasikan metrik.
- *Materi:* konstruksi graf (mention/reply/follow/co-hashtag), centrality (degree, betweenness, eigenvector/PageRank), komunitas (Louvain/Leiden), brokerage; honest charts; Gephi/ForceAtlas.
- *Metode:* lab + interpretasi substantif (siapa jembatan antar-kubu).
- *Penilaian:* objek graf + tabel metrik + figure + interpretasi (10%).

**Pertemuan 13 — LLM sebagai Annotator + Agentic Workflow + Short-Video/Multimodal** *(CPMK-4, 5)*
- *Indikator:* dapat memakai LLM untuk coding terstruktur dengan validasi reliabilitas, mengaudit keluaran agent, dan menganalisis konten video pendek.
- *Materi:* codebook→prompt, zero-shot, self-consistency, batch API, Cohen's κ vs gold set, bias, distillation; agent pipeline (retrieve→summarize→chart) + audit angka; Whisper/OCR/CLIP; metrik short-video (watch time, completion, saves) & retention curve.
- *Metode:* kuliah (30') + lab 3 bagian (120').
- *Penilai:* gold set 200 item + laporan κ + demo agent + catatan audit (15%).

**Pertemuan 14 — Evaluasi Akhir Semester + Presentasi Capstone** *(semua CPMK)*
- *Bentuk:* presentasi tim (4–5 orang) proyek end-to-end pada isu/data Indonesia (wacana isu publik X/Bluesky, brand sentiment TikTok, hoax, koordinasi, short-video campaign).
- *Luaran wajib:* kode + dokumentasi dataset, dashboard (1 view jaringan + 1 view temporal), laporan dengan bagian keterbatasan, dan ethics/DPIA note.
- *Penilaian:* ujian akhir tertulis (30%) + capstone rubrik (35%) + ethics note (10%).

---

## 3. Rancangan Penilaian Akhir

| Komponen | Bobot | Catatan |
|---|---|---|
| UTS (P7) | 20% | Soal terstruktur: konsep, API, preprocessing, legalitas |
| UAS tertulis (P14) | 30% | Metode, metrik evaluasi, interpretasi, etika |
| Tugas/lab mingguan (P1–P6, P8–P13) | 35% | 12 tugas bernilai rata-rata; rubrik: kebenaran, interpretasi, dokumentasi |
| Capstone (lintas pertemuan, presentasi P14) | 15% | Data 20% · metode 25% · insight 25% · etika 10% · komunikasi 20% |

## 4. Modul yang Pindah ke Elective (opsi 1 SKS/elective lanjut)

Agar 14 pertemuan tetap realistis, modul berikut masuk *Social Media Analytics Lanjut* atau open-elective: NLP modern/embeddings & dense retrieval (paruh dari P13), agentic AI penuh, analitik multimodal mendalam, difusi informasi & viralitas (SIR/IC-LT/Hawkes), influence maximization & coordinated inauthentic behavior, misinformation/stance detection penuh, deteksi konten sintetis & watermarking, audience profiling & reach/dedup, short-video analytics penuh, creator economy & social commerce.

## 5. Pustaka

1. Zafarani, Abbasi & Liu — *Social Media Mining* (Cambridge, 2014)
2. Russell — *Mining the Social Web* (O'Reilly, 2019)
3. Silge & Robinson — *Text Mining with R* (O'Reilly, 2017)
4. Wasserman & Faust — *Social Network Analysis* (1994); Barabási — *Network Science* (2016)
5. Jurafsky & Martin — *Speech and Language Processing* (3rd ed.)
6. Grootendorst (2022) BERTopic; Törnberg (2024) *Best practices for text annotation with LLMs*; Gilardi et al. (2024) *LLMs outperform expert coders*; arXiv:2505.09877 (2025) *Studying Digital Platforms in Scant Data Access Times*; dokumentasi Meta Content Library, X API v2, YouTube Data API, AT Protocol.
