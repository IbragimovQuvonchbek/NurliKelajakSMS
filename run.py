from tkinter import Tk, Frame, Entry, Text, Button, Label, filedialog, PhotoImage, BOTH, END
from getToken import get_token
import pandas as pd
import requests
import os
import dotenv

dotenv.load_dotenv()
TOKEN = get_token()


def send_sms(token, mobile_phone, message, from_number, callback_url):
    url = 'https://notify.eskiz.uz/api/message/sms/send'
    headers = {
        'Authorization': f'Bearer {token}',
    }
    data = {
        'mobile_phone': mobile_phone,
        'message': message,
        'from': from_number,
        'callback_url': callback_url
    }
    response = requests.post(url, headers=headers, data=data)
    return response.json()


class SendSMS:
    def __init__(self):
        self.root = Tk()
        self.root.geometry('600x600')
        self.root.title('NurliKelajakSMS')
        self.root.resizable(False, False)
        self.set_icon()

        self.frame = Frame(self.root, bg='#F0F8FF')  # Light blue background
        self.frame.pack(fill=BOTH, expand=True)

        # Add a title label with a larger font
        self.title_label = Label(self.frame, text='Nurli Kelajak SMS Sender', font=('Helvetica', 20, 'bold'),
                                 bg='#F0F8FF', fg='#4682B4')  # Steel blue text
        self.title_label.pack(pady=(20, 30))

        # Entry for Excel column
        self.excel_column = Entry(self.frame, width=40, font=('Helvetica', 14))
        self.excel_column.insert(0, "Enter Excel column name")
        self.excel_column.pack(pady=(10, 10))

        # Text widget for message input
        self.text_entry = Text(self.frame, height=5, width=40, font=('Helvetica', 12), bg='#E6E6FA',
                               fg='#000080')  # Lavender background, navy text
        self.text_entry.insert(END, "Enter your message here")
        self.text_entry.pack(pady=10)

        # Button to upload Excel file
        self.upload_button = Button(self.frame, text="Upload Excel File", font=('Helvetica', 14, 'bold'), bg='#87CEEB',
                                    fg='#FFFFFF', command=self.upload_file_action)  # Sky blue background, white text
        self.upload_button.pack(pady=(10, 20))

        # Button to send SMS
        self.send_button = Button(self.frame, text="Send SMS", font=('Helvetica', 16, 'bold'), bg='#32CD32',
                                  fg='#FFFFFF', command=self.send_sms_action)  # Lime green background, white text
        self.send_button.pack(pady=(20, 50))

        # Label for status messages
        self.status_label = Label(self.frame, text='', font=('Helvetica', 14, 'italic'), fg='#666',
                                  bg='#F0F8FF')  # Grey text on light blue background
        self.status_label.pack(pady=(10, 50))

        self.file_path = None
        self.root.mainloop()

    def set_icon(self):
        try:
            # For Windows
            self.root.iconbitmap('media/logo.ico')
        except Exception as e:
            print(f"Error setting icon: {e}")

        try:
            # For macOS/Linux
            icon = PhotoImage(file='media/logo.png')  # Use PNG for macOS/Linux
            self.root.iconphoto(True, icon)
        except Exception as e:
            print(f"Error setting icon: {e}")

    def upload_file_action(self):
        self.file_path = filedialog.askopenfilename(filetypes=[("Excel files", "*.xlsx")])
        if self.file_path:
            self.status_label.config(text=f"File uploaded: {self.file_path}", fg='#008000')  # Dark green text

    def send_sms_action(self):
        message_text = self.text_entry.get("1.0", END).strip()

        if self.file_path:
            df = pd.read_excel(self.file_path)
            if self.excel_column.get() not in df.columns:
                self.status_label.config(text='Excel file must contain the specified column.', fg='#FF0000')  # Red text
                return

            success_count = 0
            failure_count = 0
            for i, number in enumerate(df[self.excel_column.get()]):
                mobile_phone = str(number).strip()
                message = message_text
                if mobile_phone and mobile_phone.isnumeric():
                    from_number = "4546"
                    callback_url = "http://0000.uz/test.php"
                    response = send_sms(TOKEN, mobile_phone, message, from_number, callback_url)
                    # print(response)
                    if response.get('status') == 'waiting':
                        success_count += 1
                    else:
                        failure_count += 1

            self.status_label.config(
                text=f'SMS sent successfully to {success_count} numbers. Failed to send to {failure_count}.',
                fg='#008000' if failure_count == 0 else '#FF0000')


SendSMS()
