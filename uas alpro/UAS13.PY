students = []

for i in range(5):
    print("Data mahasiswa ke-", i + 1)
    nim = input("NIM: ")
    nama = input("Nama: ")
    nilai = int(input("Nilai: "))
    students.append([i + 1, nim, nama, nilai])

print("\nNo | NIM | NAMA | NILAI | KETERANGAN")
print("---|-----|------|-------|----------")
lulus = 0
tidak_lulus = 0
total_nilai = 0
for student in students:
    no, nim, nama, nilai = student
    keterangan = "Lulus" if nilai >= 56 else "Tidak Lulus"
    if keterangan == "Lulus":
        lulus += 1
    else:
        tidak_lulus += 1
    total_nilai += nilai
    print(f"{no} | {nim} | {nama} | {nilai} | {keterangan}")

print("\nJumlah mahasiswa: ", len(students))
print("Rata-rata nilai: ", total_nilai / len(students))

nilai_tertinggi = 0
nilai_terendah = 100
nama_tertinggi = ""
nama_terendah = ""
for student in students:
    no, nim, nama, nilai = student
    if nilai > nilai_tertinggi:
        nilai_tertinggi = nilai
        nama_tertinggi = nama
    if nilai < nilai_terendah:
        nilai_terendah = nilai
        nama_terendah = nama

print(f"Mahasiswa dengan nilai tertinggi adalah {nama_tertinggi} dengan nilai {nilai_tertinggi}")
print(f"Mahasiswa dengan nilai terendah adalah {nama_terendah} dengan nilai {nilai_terendah}")
print("Jumlah mahasiswa yang lulus: ", lulus)
print("Jumlah mahasiswa yang tidak lulus: ", tidak_lulus)
