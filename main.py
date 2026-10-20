# Program Suara Hewan - Kelompok Leopard

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


# Kelas anak Kucing
class Kucing(Hewan):
    def bersuara(self):
        print(f"{self.nama} mengeluarkan suara: Meooow!")


# Kelas anak Anjing
class Anjing(Hewan):
    def bersuara(self):
        print(f"{self.nama} mengeluarkan suara: Guk Guk!")


# Fungsi untuk berinteraksi dengan hewan
def interaksi_dengan_hewan(hewan):
    print(f"Berinteraksi dengan {hewan.nama}:")
    hewan.bersuara()

    if hasattr(hewan, "info_tambahan"):
        hewan.info_tambahan()

    print("-" * 30)


# Membuat objek hewan
leo = Leopard("Leo", "hutan tropis")
kucing = Kucing("Mimi")
anjing = Anjing("Buddy")

# Menjalankan program
interaksi_dengan_hewan(leo)
interaksi_dengan_hewan(kucing)
interaksi_dengan_hewan(anjing)
