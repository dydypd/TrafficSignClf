import tkinter as tk
from tkinter import filedialog
from tkinter import *
from PIL import ImageTk, Image
import numpy

from keras.models import load_model

model = load_model('model/model.h5')

classes = {
    1: 'Giới hạn tốc độ (20km/h)',
    2: 'Giới hạn tốc độ (30km/h)',
    3: 'Giới hạn tốc độ (50km/h)',
    4: 'Giới hạn tốc độ (60km/h)',
    5: 'Giới hạn tốc độ (70km/h)',
    6: 'Giới hạn tốc độ (80km/h)',
    7: 'Kết thúc giới hạn tốc độ (80km/h)',
    8: 'Giới hạn tốc độ (100km/h)',
    9: 'Giới hạn tốc độ (120km/h)',
    10: 'Không vượt',
    11: 'Không vượt xe trên 3.5 tấn',
    12: 'Quyền ưu tiên tại ngã tư',
    13: 'Đường ưu tiên',
    14: 'Nhường đường',
    15: 'Dừng lại',
    16: 'Không có xe cộ',
    17: 'Xe cộ > 3.5 tấn cấm',
    18: 'Cấm vào',
    19: 'Cảnh báo chung',
    20: 'Làn nguy hiểm bên trái',
    21: 'Làn nguy hiểm bên phải',
    22: 'Làn đôi',
    23: 'Đường gập ghềnh',
    24: 'Đường trơn trượt',
    25: 'Đường hẹp bên phải',
    26: 'Công trường',
    27: 'Đèn giao thông',
    28: 'Người đi bộ',
    29: 'Qua đường cho trẻ em',
    30: 'Qua đường cho xe đạp',
    31: 'Cảnh báo băng tuyết/đá lạnh',
    32: 'Nguy hiểm: Động vật hoang dã qua đường',
    33: 'Kết thúc giới hạn tốc độ + vượt',
    34: 'Rẽ phải',
    35: 'Rẽ trái',
    36: 'Chỉ đi thẳng',
    37: 'Chỉ đi thẳng hoặc rẽ phải',
    38: 'Chỉ đi thẳng hoặc rẽ trái',
    39: 'Rẽ phải',
    40: 'Rẽ trái',
    41: 'Bắt buộc đi vòng qua',
    42: 'Kết thúc cấm vượt',
    43: 'Kết thúc cấm vượt xe trên 3.5 tấn'
}
# initialise GUI
top = tk.Tk()
top.geometry('800x600')
top.title('Traffic sign classification')
top.configure(background='#CDCDCD')
label = Label(top, background='#CDCDCD', font=('arial', 15, 'bold'))
sign_image = Label(top)


def classify(file_path):
    global label_packed
    image = Image.open(file_path)
    image = image.convert('RGB')
    image = image.resize((32, 32))
    image = numpy.expand_dims(image, axis=0)
    image = numpy.array(image)
    pred = model.predict([image])[0]
    predicted_class = numpy.argmax(pred) + 1  # Lấy chỉ số của lớp có xác suất cao nhất
    print(predicted_class)
    sign = classes[predicted_class]
    print(sign)
    label.configure(foreground='#011638', text=sign)


def show_classify_button(file_path):
    classify_b = Button(top, text="Test", command=lambda: classify(file_path), padx=10, pady=5)
    classify_b.configure(background='#364156', foreground='white', font=('arial', 10, 'bold'))
    classify_b.place(relx=0.79, rely=0.46)


def upload_image():
    try:
        file_path = filedialog.askopenfilename()
        uploaded = Image.open(file_path)
        uploaded.thumbnail(((top.winfo_width() / 2.25), (top.winfo_height() / 2.25)))
        im = ImageTk.PhotoImage(uploaded)
        sign_image.configure(image=im)
        sign_image.image = im
        label.configure(text='')
        show_classify_button(file_path)
    except:
        pass


upload = Button(top, text="Upload", command=upload_image, padx=10, pady=5)
upload.configure(background='#364156', foreground='white', font=('arial', 10, 'bold'))
upload.pack(side=BOTTOM, pady=50)
sign_image.pack(side=BOTTOM, expand=True)
label.pack(side=BOTTOM, expand=True)
heading = Label(top, text="Traffic Sign", pady=20, font=('arial', 20, 'bold'))
heading.configure(background='#CDCDCD', foreground='#364156')
heading.pack()
top.mainloop()
