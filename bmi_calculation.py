import tkinter
from tkinter import messagebox

screen = tkinter.Tk()  # pencere olusturur
screen.title("BMI CALCULATOR")  # pencere basligini olusturur
screen.minsize(width=200, height=200)  # pencere boyutunu ayarlar

# Pencere'nin ekran'in ortasin da cikmasini saglar.
screen_width = screen.winfo_screenwidth()
screen_height = screen.winfo_screenheight()

x_coordinate = (screen_width / 2) - (200 / 2)  # 200, pencere genişliği
y_coordinate = (screen_height / 2) - (200 / 2)  # 150, pencere yüksekliği

screen.geometry(f"200x200+{int(x_coordinate)}+{int(y_coordinate)}")

# BMI degerlerini saklamak icin liste
bmi_values = []


def click_button():
    # try-except blogu icinde kullanicidan alinan agirlik ve boy degerlerini kullanarak BMI hesaplanir. Ayni blok
    # icinde, agirlik ve boyun pozitif degerler olup olmadigi kontrol edilir.
    try:
        user_weight = float(my_entry.get())
        user_height = float(my_entry_two.get())

        # Agirlik ve boy'un pozitif degerler olup olmadigini kontrol eder
        if user_weight <= 0 or user_height <= 0:
            # eger negtif deger girilirse uyari mesaji alir.
            messagebox.showerror("Error", "Weight and height must be positive values.")
            return

        bmi = user_weight / (user_height / 100) ** 2

        # Mevcut BMI degerlerini temizler
        bmi_values.clear()

        # BMI degerini listeye ekle
        bmi_values.append(bmi)

        result_label.config(text=f"BMI: {bmi:.2f}")

        if bmi < 18.5:
            result_label.config(text="Underweight", fg="blue")
        elif 18.5 <= bmi < 25:
            result_label.config(text="Normal", fg="green")
        elif 25 <= bmi < 30:
            result_label.config(text="Overweight", fg="orange")
        else:
            result_label.config(text="Obesity", fg="red")

        # Ortalama BMI'yi hesaplar ve gösterir
        average_bmi = sum(bmi_values) / len(bmi_values)
        average_label.config(text=f"Average BMI: {average_bmi:.2f}")

    # Kullanici gecerli bir sayisal deger girmemisse, bir hata mesaji goruntuler.
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numeric values for weight and height.")


# kullanici'nin agirligi'ni girebilecegi etiket'i olusturur
my_label = tkinter.Label(text="Enter Your Weight(kg)", font=('arial', 10, 'italic'))
my_label.pack()  # etiketi pencere de ortalar

# kullanici'nin agirligı'ni girebilecegi alan'i olusturur
my_entry = tkinter.Entry(width=20)
my_entry.pack(pady=(0, 5))

# kullanici'nin boy'unu girmesi icin etiket' i olusturur
my_label_two = tkinter.Label(text="Enter Your Height(cm)", font=('arial', 10, 'italic'))
my_label_two.pack()

# kullanici'nin boy'unu girebilecegi alan'i olusturur
my_entry_two = tkinter.Entry(width=20)
my_entry_two.pack()

# "Calculate" butonunu ekran da olusturur.
my_button = tkinter.Button(text="Calculate", command=click_button)
my_button.pack(pady=10)

# BMI sonucunu ekran'a yazdirir
result_label = tkinter.Label(text="")
result_label.pack()

# Ortalama BMI'yi göstermek icin etiket
average_label = tkinter.Label(text="")
average_label.pack()

# Tkinter uygulamasini baslatir ve pencere'nin surekli olarak goruntulenmesini saglar
screen.mainloop()
