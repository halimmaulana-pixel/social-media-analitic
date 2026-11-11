# Social Media Analytics

Repositori materi mata kuliah **Social Media Analytics (3 SKS)**: silabus, RPS 14 pertemuan, riset kurikulum 29 modul, buku ajar per pertemuan, dan tugas mandiri.

## Isi repositori

| Folder | Isi |
|---|---|
| `syllabus.md` | Kurigram inti, lanjutan, dan capstone plus tujuh tren 2024-2026 |
| `rps-14-pertemuan.md` | RPS standar 14 pertemuan dengan CPMK dan bobot |
| `rps-14-action.md` | Varian lab-first: artefak dulu, konsep menyusul |
| `rps-14-teori-implementasi.md` | Varian tiga lapis: teori data science, implementasi, artefak |
| `tugas-mandiri-m1-6.md` | Tugas mandiri "Satu Medsos, Banyak Temuan" dan ketentuannya |
| `results/` | 29 berkas JSON riset modul, tiap modul 23 field |
| `buku-ajar/` | Buku ajar per materi (HTML untuk dibaca, MD untuk disunting) |
| `buku-ajar/figures/` | Gambar vektor SVG untuk masing-masing materi |
| `buku-ajar/*.py` | Skrip pembangun: HTML, konversi MD, generator gambar |

## Buku ajar yang tersedia

| Materi | Judul |
|---|---|
| 1 | Pengantar dan Fondasi Social Media Analytics |
| 2 | Ekosistem Platform dan Data Affordance |
| 3 | Jenis Data dan Field Dictionary |
| 4 | Akuisisi Data via API Resmi |
| 5 | Akses Gated, Biaya, Scraping dan Legalitas |
| 6 | Preprocessing dan Kualitas Data |
| 7 | Rangkuman Materi 1-6 dan Kisi-Kisi UTS |

Setiap berkas HTML dapat dibuka langsung di peramban HP maupun komputer. Gambar sudah tertanam di dalam satu berkas, jadi tidak perlu folder pendamping.

## Cara membangun ulang buku ajar

```bash
cd buku-ajar
python3 gen_figures_m5.py   # dan seterusnya, hanya bila gambar perlu dibuat ulang
python3 build_html.py 5     # angka 5 berarti materi ke-5
python3 html_to_md.py 5     # menghasilkan versi Markdown dari HTML
```

Skrip diuji pada Termux (Android) dengan Python 3 dan pustaka standar saja.

## Catatan angka

Semua angka kuota, biaya, dan kebijakan platform disebutkan sebagai kondisi per 2026 dan perlu diperiksa ulang setiap semester di halaman resmi platform.

## Lisensi

Materi bebas dipakai untuk kegiatan belajar mengajar. Sebutkan sumbernya jika digunakan ulang.
