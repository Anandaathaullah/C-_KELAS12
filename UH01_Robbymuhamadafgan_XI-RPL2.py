from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.uix.spinner import Spinner
from kivy.uix.scrollview import ScrollView
from kivy.properties import NumericProperty
from datetime import datetime, timedelta


class PerpustakaanLayout(BoxLayout):
    counter = NumericProperty(0)
    total_semua = NumericProperty(0)

    def __init__(self, **kwargs):
        super().__init__(orientation="vertical", padding=10, spacing=10, **kwargs)

        self.anggota = {}
        self.nis_aktif = None

        # ===== ATAS =====
        atas = BoxLayout(orientation="horizontal", spacing=10, size_hint_y=None, height=350)

        # ===== KIRI (ANGGOTA) =====
        kiri = BoxLayout(orientation="vertical", spacing=5)
        kiri.add_widget(Label(text="DATA ANGGOTA"))

        form_anggota = GridLayout(cols=2, spacing=5, size_hint_y=None, height=200)
        self.nama = TextInput(hint_text="Nama", multiline=False)
        self.nis = TextInput(hint_text="NIS", multiline=False)
        self.kelas = TextInput(hint_text="Kelas", multiline=False)
        self.hp = TextInput(hint_text="HP", multiline=False)

        form_anggota.add_widget(Label(text="Nama"))
        form_anggota.add_widget(self.nama)
        form_anggota.add_widget(Label(text="NIS"))
        form_anggota.add_widget(self.nis)
        form_anggota.add_widget(Label(text="Kelas"))
        form_anggota.add_widget(self.kelas)
        form_anggota.add_widget(Label(text="HP"))
        form_anggota.add_widget(self.hp)

        kiri.add_widget(form_anggota)

        btn_simpan = Button(text="Simpan Anggota")
        btn_simpan.bind(on_press=self.simpan_anggota)
        kiri.add_widget(btn_simpan)

        self.spinner_anggota = Spinner(text="Pilih Anggota (NIS)", values=[])
        self.spinner_anggota.bind(text=self.pilih_anggota)
        kiri.add_widget(self.spinner_anggota)

        atas.add_widget(kiri)

        # ===== KANAN (BUKU) =====
        kanan = BoxLayout(orientation="vertical", spacing=5)
        kanan.add_widget(Label(text="PEMINJAMAN BUKU"))

        form_buku = GridLayout(cols=2, spacing=5, size_hint_y=None, height=120)
        self.judul = TextInput(hint_text="Judul Buku", multiline=False)
        self.kode = TextInput(hint_text="Kode Buku", multiline=False)

        form_buku.add_widget(Label(text="Judul"))
        form_buku.add_widget(self.judul)
        form_buku.add_widget(Label(text="Kode"))
        form_buku.add_widget(self.kode)

        kanan.add_widget(form_buku)

        self.spinner_buku = Spinner(text="Pilih Buku", values=[])
        kanan.add_widget(self.spinner_buku)

        tombol = BoxLayout(size_hint_y=None, height=40, spacing=5)
        btn_pinjam = Button(text="Pinjam")
        btn_pinjam.bind(on_press=self.pinjam_buku)
        btn_kembali = Button(text="Kembalikan")
        btn_kembali.bind(on_press=self.konfirmasi_kembali)
        btn_reset = Button(text="Reset")
        btn_reset.bind(on_press=self.reset_semua)

        tombol.add_widget(btn_pinjam)
        tombol.add_widget(btn_kembali)
        tombol.add_widget(btn_reset)

        kanan.add_widget(tombol)

        self.label_counter = Label(text="Buku Anggota Ini: 0")
        self.bind(counter=self.update_counter)
        kanan.add_widget(self.label_counter)

        self.label_total = Label(text="Total Semua Buku: 0")
        self.bind(total_semua=self.update_total)
        kanan.add_widget(self.label_total)

        atas.add_widget(kanan)
        self.add_widget(atas)

        # ===== BAWAH =====
        bawah = BoxLayout(orientation="horizontal", spacing=10)

        self.data_anggota = self.buat_label_scroll()
        self.data_buku = self.buat_label_scroll()

        bawah.add_widget(self.data_anggota["scroll"])
        bawah.add_widget(self.data_buku["scroll"])

        self.label_anggota = self.data_anggota["label"]
        self.label_buku = self.data_buku["label"]

        self.add_widget(bawah)

    # =========================
    def buat_label_scroll(self):
        scroll = ScrollView()
        label = Label(size_hint_y=None, halign="left", valign="top")
        label.bind(texture_size=lambda l, v: setattr(l, "height", v[1]))
        scroll.add_widget(label)
        return {"scroll": scroll, "label": label}

    def popup(self, judul, pesan):
        Popup(title=judul, content=Label(text=pesan), size_hint=(0.6, 0.4)).open()

    def update_counter(self, instance, value):
        self.label_counter.text = f"Buku Anggota Ini: {value}"

    def update_total(self, instance, value):
        self.label_total.text = f"Total Semua Buku: {value}"

    def hitung_total_semua(self):
        return sum(len(a["buku"]) for a in self.anggota.values())

    # =========================
    def simpan_anggota(self, instance):
        if not all([self.nama.text, self.nis.text, self.kelas.text, self.hp.text]):
            self.popup("Error", "Semua data harus diisi")
            return

        nis = self.nis.text
        if nis not in self.anggota:
            self.anggota[nis] = {
                "nama": self.nama.text,
                "kelas": self.kelas.text,
                "hp": self.hp.text,
                "buku": []
            }
            self.spinner_anggota.values = list(self.anggota.keys())

        self.spinner_anggota.text = nis

    def pilih_anggota(self, spinner, nis):
        if nis in self.anggota:
            a = self.anggota[nis]
            self.nis_aktif = nis
            self.nama.text = a["nama"]
            self.nis.text = nis
            self.kelas.text = a["kelas"]
            self.hp.text = a["hp"]
            self.spinner_buku.values = a["buku"]
            self.counter = len(a["buku"])
            self.total_semua = self.hitung_total_semua()
            self.update_ringkasan()

    def pinjam_buku(self, instance):
        if not self.nis_aktif:
            self.popup("Error", "Pilih anggota dulu")
            return
        if not self.judul.text or not self.kode.text:
            self.popup("Error", "Judul & kode harus diisi")
            return

        tgl = datetime.now() + timedelta(days=7)
        data = f"{self.judul.text} ({self.kode.text}) - Kembali: {tgl.strftime('%d/%m/%Y')}"
        self.anggota[self.nis_aktif]["buku"].append(data)

        self.spinner_buku.values = self.anggota[self.nis_aktif]["buku"]
        self.counter += 1
        self.total_semua = self.hitung_total_semua()
        self.update_ringkasan()

        self.judul.text = ""
        self.kode.text = ""

    def konfirmasi_kembali(self, instance):
        buku = self.spinner_buku.text
        if self.nis_aktif and buku in self.anggota[self.nis_aktif]["buku"]:
            self.anggota[self.nis_aktif]["buku"].remove(buku)
            self.spinner_buku.values = self.anggota[self.nis_aktif]["buku"]
            self.counter -= 1
            self.total_semua = self.hitung_total_semua()
            self.update_ringkasan()

    def reset_semua(self, instance):
        self.anggota.clear()
        self.nis_aktif = None
        self.spinner_anggota.values = []
        self.spinner_buku.values = []
        self.label_anggota.text = ""
        self.label_buku.text = ""
        self.counter = 0
        self.total_semua = 0

    def update_ringkasan(self):
        if not self.nis_aktif:
            return

        a = self.anggota[self.nis_aktif]
        self.label_anggota.text = f"""
DATA ANGGOTA
Nama : {a['nama']}
NIS  : {self.nis_aktif}
Kelas: {a['kelas']}
HP   : {a['hp']}
"""

        teks = "DATA PEMINJAMAN\n"
        for i, b in enumerate(a["buku"], 1):
            teks += f"{i}. {b}\n"
        teks += f"\nJumlah Buku: {len(a['buku'])}"
        self.label_buku.text = teks


class PerpustakaanApp(App):
    def build(self):
        return PerpustakaanLayout()


if __name__ == "__main__":
    PerpustakaanApp().run()
