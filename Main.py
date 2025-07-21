from Operation import operation
from Tampil import Tampil

class Main:
    def __init__(self):
        self.operation = operation()
        self.tampil = Tampil()

    def run(self):
        input_string = input("Enter numbers separated by spaces: ")
        number_list = list(map(float, input_string.split()))

        hasil_tambah = self.operation.sum(number_list)
        hasil_minus = self.operation.minus(number_list)
        hasil_kali = self.operation.multiply(number_list)
        hasil_bagi = self.operation.divide(number_list)

        self.tampil.show_hasil("", hasil_tambah)
        self.tampil.show_hasil("", hasil_minus)
        self.tampil.show_hasil("", hasil_kali)
        self.tampil.show_hasil("", hasil_bagi)

if __name__ == "__main__":
    Kalkulator = Main()
    Kalkulator.run()
