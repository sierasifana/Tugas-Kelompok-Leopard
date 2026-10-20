
# Program Suara Hewan Leopard
# Kelompok Leopard

# Kelas induk
class Hewan:
    def __init__(self, nama):
        self.nama = nama

    def bersuara(self):
        print(f"{self.nama} mengeluarkan suara hewan.")


# Kelas anak Leopard
class Leopard(Hewan):
    def __init__(self, nama, habitat):
        super().__init__(nama)
        self.habitat = habitat

    def bersuara(self):
        print(f"{self.nama} mengeluarkan suara: Grrrawww!")

    def info_tambahan(self):
        print(f"{self.nama} hidup di habitat {self.habitat}.")


# Fungsi interaksi dengan leopard
def interaksi_dengan_hewan(hewan):
    print(f"Berinteraksi dengan {hewan.nama}:")
    hewan.bersuara()
    hewan.info_tambahan()
    print("-" * 30)


# Membuat objek leopard
leo = Leopard("Leo", "hutan dan padang rumput")

# Menjalankan program
interaksi_dengan_hewan(leo)
