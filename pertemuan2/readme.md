## # Deskripsi Proyek

Proyek ini berisi implementasi struktur data **Linked List** sederhana menggunakan bahasa Python. Kode ini mencakup operasi dasar seperti:

* Menambah data di awal (*insert at first*)
* Menambah data di akhir (*insert at last*)
* Menambah data pada indeks tertentu (*insert at*)
* Mengukur panjang linked list
* Mencetak seluruh isi linked list

---

## # Struktur File

```
Linkedlist.py
```

---

## # Cara Menjalankan Program

1. Pastikan Python sudah terinstal.
2. Jalankan file dengan perintah:

```
python Linkedlist.py
```

---

## # Penjelasan Kode

### ## 1. **Class Node**

```python
class Node:
    def __init__(self, data=None, pointer=None):
        self.data = data
        self.next = pointer
```

* **Node** adalah elemen dasar Linked List.
* `data` menyimpan nilai.
* `next` adalah pointer menuju node berikutnya.
* Pointer default-nya `None` (akhir list).

---

### ## 2. **Class LinkedList**

```python
class LInkedList:
    def __init__(self):
        self.head = None
```

* `head` menunjuk node pertama dalam linked list.
* Di awal, list masih kosong → `head = None`.

---

### ## 3. **Insert di Awal**

```python
def insert_at_first(self, data):
    node = Node(data, self.head)
    self.head = node
```

* Membuat node baru yang menunjuk ke head lama.
* Lalu head diganti dengan node baru tersebut.
* Operasi ini sangat cepat → O(1).

---

### ## 4. **Insert di Akhir**

```python
def insert_at_last(self, data):
    if self.head is None:
        self.head = Node(data)
    else:
        node_sekarang = self.head
        while node_sekarang.next:
            node_sekarang = node_sekarang.next
        
        node = Node(data)
        node_sekarang.next = node
```

* Jika list kosong → node jadi head.
* Jika tidak, lakukan *traversing* hingga node terakhir.
* Node baru ditempelkan di ujung list.

---

### ## 5. **Insert di Indeks Tertentu**

```python
def insert_at(self, index, data):
    if index < 0 or index > self.length() -1:
        print("Index tidak valid")
    elif index == 0:
        self.insert_at_first(data)
    else:
        urutan = 0
        node_sekarang = self.head
    
        while urutan < index - 1:
            urutan += 1
            node_sekarang = node_sekarang.next
        
        node = Node(data, node_sekarang.next)
        node_sekarang.next = node
```

* Validasi indeks.
* Jika index = 0 → gunakan fungsi *insert_at_first*.
* Jika tidak → bergerak sampai node sebelum indeks yang dimaksud.
* Node baru disisipkan di tengah.

---

### ## 6. **Print Linked List**

```python
def print(self):
    if self.head is None:
        print("Linked list is empty")
    else:
        text_print = ""
        node_sekarang = self.head

        while node_sekarang:
            text_print += str(node_sekarang.data) + " -> "
            node_sekarang = node_sekarang.next

        print(text_print)
```

* Traversing setiap node dan menampilkannya dalam format:

  ```
  Mangga -> Jeruk -> Apel ->
  ```

---

### ## 7. **Menghitung Panjang List**

```python
def length(self):
    urutan = 0
    data_sekarang = self.head

    while data_sekarang:
        data_sekarang = data_sekarang.next
        urutan += 1

    return urutan
```

* Traversing dari head sampai akhir sambil menghitung jumlah node.

---

### ## 8. **Contoh Penggunaan**

```python
ll = LInkedList()

ll.insert_at_first("Jeruk")
ll.insert_at_first("Mangga")
ll.insert_at_first("Manggis")
ll.insert_at_last("Apel")
ll.insert_at(2, "Pisang")

ll.print()
print("Length:", ll.length())
```

---

## # Output Contoh

```
Manggis -> Mangga -> Pisang -> Jeruk -> Apel -> 
Length: 5
```

---

## # Kontribusi

Silakan fork, buka *issue*, atau buat *pull request*.