# Program Suara Hewan Leopard
# Kelas induk
class Hewan:
    def __init__(self, nama):
        self.nama = nama

    def bersuara(self):
        print(f"{self.nama} mengeluarkan suara umum hewan.")


# Kelas anak Leopard
class Leopard(Hewan):
    def __init__(self, nama):
        super().__init__(nama)

    def bersuara(self):
        print(f"{self.nama} mengeluarkan suara: Grrrawww!")

    def info_tambahan(self):
        print(f"{self.nama} adalah seekor leopard.")


# Fungsi interaksi dengan hewan
def interaksi_dengan_hewan(hewan_objek):
    print(f"Berinteraksi dengan {hewan_objek.nama}:")
    hewan_objek.bersuara()
    hewan_objek.info_tambahan()
    print("-" * 20)


# Membuat objek leopard
leo = Leopard("Leo")

# Menjalankan program
interaksi_dengan_hewan(leo)
