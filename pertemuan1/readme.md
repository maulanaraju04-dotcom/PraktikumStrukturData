1. Penjelasan Kode queue.py (struktur data Queue / Antrian)

// Queue bekerja dengan prinsip FIFO (First In First Out).

Isi kode: 

queue

queue = []


// Membuat list kosong yang akan digunakan sebagai antrian.

queue.append('A')
queue.append('B')
queue.append('C')
print("Queue: ", queue)


append() menambah elemen ke belakang antrian.

// Setelah kode di atas dijalankan, isi queue menjadi:

['A', 'B', 'C']


Output:

Queue:  ['A', 'B', 'C']

element = queue.pop(0)
print("Dequeue: ", element)


// pop(0) mengambil dan menghapus elemen paling depan.

// Karena queue FIFO, elemen pertama 'A' dikeluarkan.

Output:

Dequeue:  A


// Isi queue sekarang:

['B', 'C']

frontElement = queue[0]
print("Peek: ", frontElement)


// queue[0] melihat elemen paling depan tanpa menghapusnya.

// Elemen depan saat ini adalah 'B'.

Output:

Peek:  B

isEmpty = not bool(queue)
print("isEmpty: ", isEmpty)


// bool(queue) bernilai True jika queue tidak kosong.

// not membalik nilainya.

// Karena queue masih berisi ['B', 'C'], maka hasilnya False.

Output:

isEmpty:  False

print("Size: ", len(queue))


// Menghitung jumlah elemen saat ini. Ada 2 item.

Output:

Size:  2

// Ringkasan Output queue.py
Queue:  ['A', 'B', 'C']
Dequeue:  A
Peek:  B
isEmpty:  False
Size:  2

2. Penjelasan Kode stack.py (struktur data Stack / Tumpukan)

// Stack bekerja dengan prinsip LIFO (Last In First Out).

Isi kode: 

stack

stack = []


// Membuat list kosong yang akan digunakan sebagai stack.

stack.append('A')
stack.append('B')
stack.append('C')
print("Stack: ", stack)


// append() menambah elemen ke puncak tumpukan.

// Isi stack sekarang:

['A', 'B', 'C']


Output:

Stack:  ['A', 'B', 'C']

element = stack.pop()
print("Pop: ", element)


// pop() tanpa indeks menghapus elemen paling atas.

// Karena stack LIFO, elemen terakhir 'C' diambil.

Output:

Pop:  C


// Isi stack sekarang:

['A', 'B']

topElement = stack[-1]
print("Peek: ", topElement)


// stack[-1] melihat elemen paling atas tanpa menghapusnya.

// Elemen paling atas adalah 'B'.

Output:

Peek:  B

isEmpty = not bool(stack)
print("isEmpty: ", isEmpty)


// Stack masih berisi ['A', 'B'], jadi tidak kosong → False.

Output:

isEmpty:  False

print("Size :", len(stack))


// Jumlah elemen saat ini: 2.

Output:

Size : 2

// Ringkasan Output stack.py
Stack:  ['A', 'B', 'C']
Pop:  C
Peek:  B
isEmpty:  False
Size : 2

// Kesimpulan Perbedaan Utama
Operasi	Queue (FIFO)	Stack (LIFO)
Menambah	append() → belakang	append() → atas
Menghapus	pop(0) → depan	pop() → atas
Melihat elemen	queue[0]	stack[-1]
