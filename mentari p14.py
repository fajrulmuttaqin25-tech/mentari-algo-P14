def bubble_sort_nama(daftar_nama):
    """
    Mengurutkan daftar nama peserta secara alfabetis (ascending)
    menggunakan algoritma Bubble Sort.
    
    Parameter:
        daftar_nama (list): List berisi nama-nama peserta.
    
    Returns:
        list: List nama yang sudah terurut secara alfabetis.
    """
    n = len(daftar_nama)
    
    for i in range(n - 1):
        swapped = False
        
        for j in range(n - 1 - i):
            # Bandingkan nama secara alfabetis (case-insensitive)
            if daftar_nama[j].lower() > daftar_nama[j + 1].lower():
                # Tukar posisi
                daftar_nama[j], daftar_nama[j + 1] = daftar_nama[j + 1], daftar_nama[j]
                swapped = True
        
        if not swapped:
            break
    
    return daftar_nama

def tampilkan_papan_pengumuman(daftar_nama):
    print("=" * 35)
    print("   PAPAN PENGUMUMAN PESERTA LOMBA")
    print("=" * 35)
    for nomor, nama in enumerate(daftar_nama, start=1):
        print(f"  {nomor:2}. {nama}")
    print("=" * 35)

if __name__ == "__main__":
    peserta = [
        "Muhamad Fajrul Muttaqin",
        "Melani Alisya Putri",
        "Ahmad Darul Qutni",
        "Ahmad Refi Fadilah",
        "Sayyid Syafiqurahman",
        "Ilyasyach Raihan Resfiana",
        "Muhammad Munanda",
        "Sela Aryani",
        "Selloh Novita Sari",
        "Eef Saeful Azis"
    ]
    
    print(f"Jumlah peserta: {len(peserta)} orang\n")
    print("Daftar nama SEBELUM diurutkan:")
    tampilkan_papan_pengumuman(peserta)
    
    bubble_sort_nama(peserta)
    print("\nDaftar nama SESUDAH diurutkan (Alfabetis):")
    tampilkan_papan_pengumuman(peserta)