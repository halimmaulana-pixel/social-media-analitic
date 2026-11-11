# Mata Kuliah Social Media Analytics — Kurikulum Era Tren 2024–2026

Disusun dari riset 29 modul (`results/*.json`, validasi 29/29, coverage 100%) + web search tren 2024–2026.
Cocok dipakai sebagai basis RPS (Merdeka Belajar / OBE) program studi Ilmu Komunikasi, Sistem Informasi, Data Science, atau Informatika.

---

## 1. Identitas Mata Kuliah

| Item | Nilai |
|---|---|
| Nama | Social Media Analytics (SMA) |
| Beban | 3 SKS (2 SKS kuliah + 1 SKS praktikum/lab) |
| Semester | 5–7 (prasyarat: Statistika Dasar, Pemrograman Dasar/Python atau R, Teori Komunikasi Dasar) |
| Sifat | Wajib inti + electife lanjutan |
| Bentuk | Kuliah + lab + capstone mini |

## 2. Konteks "Era Tren Saat Ini" — 7 perubahan yang menentukan isi kuliah

1. **Konten multimodal jadi default** — analisis tidak lagi hanya teks: short video, audio (ASR), kredit on-screen (OCR), dan gambar wajib masuk kurikulum.
2. **LLM jadi standar sebagai annotator/koder** — penelitian sosial kini memakai LLM untuk labeling masif, dengan wajib validasi: gold set manusia, Cohen's kappa, bias check, dan distillation (Törnberg 2024; Gilardi et al. 2024).
3. **Short-video jadi satuan konten utama** — metrik yang relevan bergeser dari like ke *watch time, completion rate, saves/shares* (TikTok, Reels, Shorts).
4. **Social commerce & creator economy** — TikTok Shop/live commerce, pengukuran influencer, deteksi fake follower (pasar creator economy ~USD 250B, 2025–2026).
5. **Konten sintetis & AI-generated misinformation** — deteksi teks/gambar/audio sintetis, provenance/watermarking, dan "share of synthetic posts" sebagai metrik baru.
6. **Agentic AI masuk workflow social listening** — produk Pulsar/Talkwalker/Meta dan riset pasar memakai agent + MCP connector; peran analis bergeser dari "menjalankan tool" ke "mendesain, mengevaluasi, dan mengaudit agent".
7. **Akses data mengetat & berbayar** — X hapus akses akademik gratis, Meta Content Library gated ke institusi akademik, enclave riset mulai berbayar per tim (~USD 371/tim/bulan sejak Jan 2026), sementara Bluesky/AT Protocol relatif terbuka → kurikulum wajib mengajarkan "quota literacy" dan perancangan studi yang tetap feasible.

## 3. Struktur Kurikulum 2 Tahap + Capstone (total 29 modul)

### A. Mata Kuliah Inti — *Social Media Analytics* (3 SKS, 16 minggu)

| Mg | Modul | Isi inti |
|---|---|---|
| 1 | Fondasi & Ruang Lingkup | definisi, siklus data, ladder descriptive→predictive→prescriptive |
| 2–3 | Ekosistem Platform | X, TikTok, Instagram, YouTube, Reddit, Bluesky/AT Protocol; data affordance & feed logic |
| 4 | Jenis Data | teks, gambar, video, interaksi/graph, metadata, engagement log; field dictionary |
| 5–6 | Akuisisi via API | X API v2, TikTok Research API, YouTube Data, Reddit, Bluesky; pagination, rate limit, sampling frame |
| 7 | Akses Gated & Biaya + Scraping/Legalitas | Meta Content Library, enclave berbayar, ToS, UU PDP, scraping yang sah |
| 8 | Preprocessing | normalisasi, dedup, bot filter, emoji/hashtag/slang, language detection, code-mixing, sampling bias |
| 9 | Text Mining Dasar | TF-IDF, n-gram, RAKE/TextRank, lexicon (VADER/InSet), k-means baseline |
| 10–11 | Sentiment & Emotion | lexicon → SVM → BERT/RoBERTa fine-tuning, ABSA, emosi, sarkasme, kelas imbalance |
| 12 | Lokalisasi Bahasa Indonesia | IndoBERT/IndoRoBERTa/NusaBERT, InSet, dataset SmSA/hoaks, IndoNLU, error analysis |
| 13–14 | Topic Modeling | LDA, NMF, BERTopic (UMAP/HDBSCAN + c-TF-IDF), STM/dinamik, coherence + validasi manusia |
| 15 | Social Network Analysis | centrality (degree/betweenness/eigenvector/PageRank), komunitas (Louvain/Leiden), brokerage |
| 16 | Visualisasi & Insight | Gephi/igraph, small multiples, honest charts, dashboard (Streamlit/Shiny), insight memo |

### B. Electife/Spesialisasi — *Social Media Analytics Lanjut* (3 SKS, 16 minggu)

| Mg | Modul |
|---|---|
| 1 | NLP Modern: transformer, embeddings (SBERT/KataBERT/BGE), dense retrieval, zero-shot |
| 2–3 | LLM sebagai Annotator: codebook→prompt, kappa gate, bias, human-in-the-loop, distillation |
| 4 | Agentic AI untuk Social Listening (agent pipeline, MCP connector, audit + logging) |
| 5–6 | Analitik Multimodal: CLIP/SigLIP, OCR, Whisper, video LLM, fusion modalitas |
| 7–8 | Difusi Informasi & Viralitas: cascade, SIS/SIR, IC/LT, Hawkes, trending prediction |
| 9 | Influence & Coordinated Behavior: bot/troll, koordinasi (co-tweet/timing), influence maximization |
| 10 | Misinformation & Trust/Safety: stance detection, claim matching, koreksi vs klaim |
| 11 | Deteksi Konten Sintetis: AI-text detector, deepfake, watermarking/provenance, FPR/FNR |
| 12 | Perilaku & Engagement: prediksi engagement, temporal patterns, watch time, churn |
| 13 | Audience Profiling & Measurement: inferensi demografi, reach/dedup, consented first-party data |
| 14 | Short-Video Analytics: retention curve, hook 1–3 detik, normalisasi audiens |
| 15 | Creator Economy & Social Commerce: CPE, engagement quality, live commerce GMV, fake follower |
| 16 | Data Access Governance + Tools Stack + Etika/Legal (integrasi refleksi) |

### C. Capstone (2–4 SKS, lintas 6–8 minggu)

Tim 4–5 mahasiswa mengerjakan proyek nyata end-to-end: **collect → clean → model (teks/jaringan/video) → dashboard → interpretasi → presentasi**, dengan ethics/DPIA note. Skenario default: wacana isu publik di X/Bluesky, brand sentiment TikTok, deteksi hoaks, analisis koordinasi, short-video campaign.

## 4. Capaian Pembelajaran (OBE)

- **C2 (Memahami)** menjelaskan ruang lingkup, jenis data, keterbatasan akses & etika SMA.
- **C3 (Menerapkan)** mengumpulkan dan membersihkan data via API/scraping sah; menjalankan baseline teks (TF-IDF/lexicon) dan model transformer sesuai bahasa.
- **C4 (Menganalisis)** melakukan topic modeling, SNA, difusi, engagement/prediksi, dan analitik multimodal/multibahasa; mengevaluasi model dengan metrik yang tepat.
- **C5 (Mengevaluasi)** menguji validitas klaim, bias, keterbatasan sampel, dan reliabilitas label (κ); mengaudit keluaran LLM/agent.
- **C6 (Menciptakan** menghasilkan pipeline lengkap + dashboard + rekomendasi + laporan etika dan keterbatasan.

## 5. Tools & Praktikum

- **Python:** pandas, scikit-learn, transformers, datasets, accelerate, bertopic, umap-learn, hdbscan, networkx, igraph, leidenalg, gensim, praw, atproto, openai-whisper, faiss, sentence-transformers (KataBERT/IndoBERT), streamlit.
- **R (alternatif):** rtweet, tidytext, quanteda, ggraph, stm, igraph.
- **Visualisasi:** matplotlib/seaborn, plotly, Gephi, igraph, Streamlit/Shiny, Tableau Public.
- **Komersial (demo read-only):** Brandwatch, Meltwater, Talkwalker, Sprout Social, Pulsar; native analytics (TikTok Studio, YouTube Studio, Instagram Insights).
- **Praktikum tiap modul** ada di field `lab_activities` setiap file `results/`.

## 6. Referensi Inti

- Zafarani, Abbasi & Liu, *Social Media Mining* (Cambridge, 2014).
- Russell, *Mining the Social Web* (O'Reilly, 2019).
- Silge & Robinson, *Text Mining with R* (O'Reilly, 2017).
- Wasserman & Faust, *Social Network Analysis* (1994); Barabási, *Network Science* (2016).
- Jurafsky & Martin, *Speech and Language Processing* (linguistik/NLP).
- Grootendorst (2022) BERTopic; Törnberg (2024) *Best practices for text annotation with LLMs*; Gilardi et al. (2024) *LLMs outperform expert coders*; arXiv 2505.09877 (2025) *Studying Digital Platforms in Scant Data Access Times*; We Are Social/DataReportal Digital 2026; dokumentasi Meta Content Library, X API, AT Protocol.

## 7. Asesmen

| Komponen | Bobot |
|---|---|
| Lab/praktikum mingguan (notebook + interpretasi) | 25% |
| Tugas analisis (sentimen/topik/jaringan/multimodal) | 20% |
| Kuis + bake-off metode (lexicon vs klassik vs transformer vs LLM) | 10% |
| Capstone (data 20% · metode 25% · insight 25% · etika 10% · komunikasi 20%) | 35% |
| Ethics/DPIA note & data-management note | 10% |

---

*Catatan field-level per modul: `~/social-media-analytics/results/<id>.json` (23 field: isi, konsep, CP, metode, metrik, pitfalls, tools, platform komersial, biaya akses, lab, dataset, workflow, asesmen, pustaka, paper, tren, relevansi industri, konteks Indonesia, etika, studi kasus, luaran).*
