# Struktur Data Queue & Stack (Python)

Repositori ini berisi dua contoh implementasi struktur data dasar menggunakan Python:

* **Queue (Antrian)** — bekerja dengan prinsip **FIFO** (*First In First Out*)
* **Stack (Tumpukan)** — bekerja dengan prinsip **LIFO** (*Last In First Out*)

Setiap file berisi implementasi dasar menggunakan list Python, beserta contoh operasi umum seperti **enqueue**, **dequeue**, **push**, **pop**, **peek**, **isEmpty**, dan **size**.

---

## 1. Queue — FIFO (First In First Out)

### File: `queue.py`

### Penjelasan Kode

```python
# Membuat list kosong sebagai antrian
queue = []

# Menambahkan elemen ke dalam antrian menggunakan append()
queue.append('A')
queue.append('B')
queue.append('C')
print("Queue:", queue)
```

**Penjelasan sintaks:**

* `queue = []` → membuat list kosong yang bertindak sebagai antrian.
* `append()` → menambah elemen ke **belakang** antrian.
* Setelah tiga kali append, isi queue: `['A', 'B', 'C']`.

---

```python
# Menghapus elemen paling depan menggunakan pop(0)
element = queue.pop(0)
print("Dequeue:", element)
```

**Penjelasan sintaks:**

* `pop(0)` → mengambil dan menghapus elemen indeks ke‐0 (paling depan).
* Karena FIFO, yang keluar adalah `'A'`.

---

```python
# Melihat elemen paling depan tanpa menghapusnya
frontElement = queue[0]
print("Peek:", frontElement)
```

**Penjelasan sintaks:**

* `queue[0]` → mengakses elemen pertama.
* Tidak menghapus elemen tersebut.

---

```python
# Mengecek apakah queue kosong
empty = not bool(queue)
print("isEmpty:", empty)
```

**Penjelasan sintaks:**

* `bool(queue)` bernilai True jika queue berisi elemen.
* `not` membalik hasilnya.
* Jika queue berisi `['B','C']` → hasil `False`.

---

```python
# Menghitung ukuran antrian
print("Size:", len(queue))
```

**Penjelasan sintaks:**

* `len(queue)` → menghitung total elemen dalam antrian.

---

### Ringkasan Output

```
Queue: ['A', 'B', 'C']
Dequeue: A
Peek: B
isEmpty: False
Size: 2
```

---

## 2. Stack — LIFO (Last In First Out)

### File: `stack.py`

### Penjelasan Kode

```python
# Membuat list kosong sebagai stack
stack = []

# Menambahkan elemen ke puncak stack
stack.append('A')
stack.append('B')
stack.append('C')
print("Stack:", stack)
```

**Penjelasan sintaks:**

* `stack = []` → membuat list kosong.
* `append()` → menambah elemen ke **puncak** stack.
* Isi stack: `['A','B','C']`.

---

```python
# Menghapus elemen paling atas
element = stack.pop()
print("Pop:", element)
```

**Penjelasan sintaks:**

* `pop()` tanpa indeks → mengambil elemen terakhir (paling atas).
* Karena LIFO, elemen yang keluar adalah `'C'`.

---

```python
# Melihat elemen paling atas tanpa menghapusnya
topElement = stack[-1]
print("Peek:", topElement)
```

**Penjelasan sintaks:**

* `stack[-1]` → mengakses elemen indeks terakhir.
* Tidak menghapus elemen tersebut.

---

```python
# Mengecek apakah stack kosong
empty = not bool(stack)
print("isEmpty:", empty)
```

**Penjelasan sintaks:**

* Stack masih berisi `['A','B']` → hasil `False`.

---

```python
# Menampilkan ukuran stack
print("Size:", len(stack))
```

**Penjelasan sintaks:**

* `len(stack)` → menghitung jumlah elemen saat ini.

---

### Ringkasan Output

```
Stack: ['A', 'B', 'C']
Pop: C
Peek: B
isEmpty: False
Size: 2
```

---

## Perbedaan Utama Queue vs Stack

| Operasi        | Queue (FIFO)          | Stack (LIFO)      |
| -------------- | --------------------- | ----------------- |
| Menambah       | `append()` → belakang | `append()` → atas |
| Menghapus      | `pop(0)` → depan      | `pop()` → atas    |
| Melihat elemen | `queue[0]`            | `stack[-1]`       |

---

Jika ingin, saya bisa membuatkan versi README dengan **gambar arsitektur Queue/Stack**, atau menambahkan **diagram alur (flowchart)**.
