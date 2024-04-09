import sys
import random
import smtplib
import re
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout, QSizePolicy
from PyQt5.QtCore import Qt, QSize, QRect, QEasingCurve, QPropertyAnimation
from PyQt5.QtGui import QFont
from OTPverify_Backend import OTPVerifyFeatureBackend, OTPVerification

class OTPVerifyGUI(QWidget):
    
    def __init__(self):
        super().__init__()

        # Customize Window Title and Background Color:
        self.setWindowTitle('OTP Verification System')
        self.setStyleSheet("background-color: #f0f0f0;")
        # Adjust Window Size and Layout:
        self.setGeometry(400, 150, 900, 750) # self.setGeometry(x-axis top-left corner, y-axis top-left corner, width widget in pixels, height widget in pixels.)

        # heading
        self.heading_label = QLabel("Welcome to My Application!")
        # subheading
        self.subheading_label = QLabel("OTP Verification System")
        # ------------------------------
        self.status_label = QLabel("")  # Label for displaying status messages
        # email widget
        self.email_label = QLabel('Email:')
        self.email_input = QLineEdit()
        self.email_status_label = QLabel("")  # Error label for displaying email validation errors
        # otp widget
        self.otp_label = QLabel('OTP:')
        self.otp_input = QLineEdit()
        self.otp_status_label = QLabel("")  # Error label for displaying OTP validation errors
        # button widget
        self.send_button = QPushButton('Send OTP')
        self.verify_button = QPushButton('Verify OTP')

# -----------------------------------------------------------------------------------------------

        # Customize Labels and Buttons:
        self.heading_label.setStyleSheet("font-size: 24pt; font-weight: normal;")
        self.heading_label.setAlignment(Qt.AlignCenter)  # Align widget in the center
        self.subheading_label.setStyleSheet("font-size: 20pt; font-weight: bold; background-color: LightSlateGray;")
        self.subheading_label.setAlignment(Qt.AlignCenter)  # Align widget in the center
        self.email_label.setStyleSheet("font-weight: bold; font-size: 20px;")
        self.otp_label.setStyleSheet("font-weight: bold; font-size: 20px;color: grey;")
        self.send_button.setStyleSheet("font-weight: bold; font-size: 20px; background-color: #4CAF50; color: white; border-radius: 5px; padding: 8px 16px;")
        self.verify_button.setStyleSheet("font-weight: bold; font-size: 20px; background-color: #008CBA; color: white; border-radius: 5px; padding: 8px 16px;")

# -----------------------------------------------------------------------------------------------

        # Placeholder and Adjust Input Fields:
        # to set the size of the placeholders
        placeholder_font = QFont()
        placeholder_font.setPointSize(12)
        self.email_input.setPlaceholderText("Enter your email")
        self.email_input.setStyleSheet("padding: 5px; border-radius: 5px; border: 2px solid black;")
        self.email_input.setFont(placeholder_font)
        self.otp_input.setPlaceholderText("Enter the OTP sent to your email")
        self.otp_input.setStyleSheet("padding: 5px; border-radius: 5px; border: 2px solid grey;")
        self.otp_input.setFont(placeholder_font)
        # Disable OTP input initially
        self.otp_input.setEnabled(False)

# -----------------------------------------------------------------------------------------------

        # status label adjusting
        sub_status_label_font = QFont("roboto",10)
        self.email_status_label.setFont(sub_status_label_font)
        self.otp_status_label.setFont(sub_status_label_font)
        main_status_label_font = QFont("roboto",14)
        self.status_label.setFont(main_status_label_font)
        self.status_label.setAlignment(Qt.AlignCenter)  # Align widget in the center

# -----------------------------------------------------------------------------------------------

        # Set fixed size for input box
        self.email_input.setFixedSize(400, 50)
        self.otp_input.setFixedSize(400, 50)
        # Set fixed size for the button
        self.send_button.setFixedSize(200, 50)
        self.verify_button.setFixedSize(200, 50)

        # Implementing Functionality to buttons by methods
        self.send_button.clicked.connect(self.send_otp_button)
        self.verify_button.clicked.connect(self.verify_otp_button)
# -----------------------------------------------------------------------------------------------

        # All widget Layouts
        # Email Layout
        email_layout = QVBoxLayout()
        email_layout.addWidget(self.email_label)
        email_layout.addWidget(self.email_input)
        email_layout.addWidget(self.email_status_label)
        email_layout.setAlignment(Qt.AlignCenter)  # Align items in the center vertically
        # OTP Layout
        otp_layout = QVBoxLayout()
        otp_layout.addWidget(self.otp_label)
        otp_layout.addWidget(self.otp_input)
        otp_layout.addWidget(self.otp_status_label)
        otp_layout.setAlignment(Qt.AlignCenter)  # Align items in the center vertically
        # Button layout
        button_layout = QHBoxLayout()
        button_layout.addWidget(self.send_button)
        button_layout.addWidget(self.verify_button)
        button_layout.setAlignment(Qt.AlignCenter)  # Align items in the center horizontally

# -----------------------------------------------------------------------------------------------

        main_layout = QVBoxLayout()
        main_layout.addWidget(self.heading_label)
        main_layout.addSpacing(20)  # Add some spacing between heading and subheading
        main_layout.addWidget(self.subheading_label)
        main_layout.addSpacing(30)  # Add some spacing between heading and subheading
        #----------------------
        main_layout.addWidget(self.status_label)
        main_layout.addLayout(email_layout)
        main_layout.addLayout(otp_layout)
        # ---------------------
        main_layout.addLayout(button_layout)
        # ---------------------
        # Align layouts in the center vertically
        main_layout.setAlignment(Qt.AlignCenter)
        # Add Spacing and Alignment:
        main_layout.setSpacing(10)
        self.setLayout(main_layout)

        # OTP verifcation object
        self.otp_verification = OTPVerification()

# -----------------------------------------------------------------------------------------

    def send_otp_button(self):
        email = self.email_input.text()
        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            print("Invalid email address is entered")
            self.email_status_label.setText("Invalid email address. Please enter a valid email address.")
            self.email_status_label.setStyleSheet("color: red")
            return None

        # Clear the error label if email is valid
        self.email_status_label.setText("")

        # Generate OTP and send email
        success, otp = self.otp_verification.send_otp(email)
        if success:
            self.otp_input.setEnabled(True)  # Enable OTP input after sending OTP
            # making it black and enable after succesfully send otp
            self.otp_label.setStyleSheet("font-weight: bold; font-size: 20px;color: black;")
            self.otp_input.setStyleSheet("padding: 5px; border-radius: 5px; border: 2px solid black;")
            self.status_label.setText("OTP sent successfully.")
            self.status_label.setStyleSheet("color: green")
            self.status_label.setStyleSheet("font-size: 20px; color: green; ")
            self.generated_otp = otp  # Store the generated OTP in an instance variable
            return True  # Return True if OTP is sent successfully
        else:
            self.otp_input.setEnabled(False)
            self.status_label.setText("Failed to send OTP or entered email address not exist")
            self.status_label.setStyleSheet("color: red")
            return False  # Return False if OTP sending fails

    def verify_otp_button(self):
        entered_otp = self.otp_input.text()
        generated_otp = getattr(self, 'generated_otp', None)  # Get the generated OTP if it exists
        if generated_otp:
            if entered_otp:
                if self.otp_verification.verify_otp(generated_otp, entered_otp):
                    self.status_label.setText("OTP verification successful!")
                    self.status_label.setStyleSheet("color: green; ")
                else:
                    self.otp_status_label.setText("Invalid OTP. Please enter a valid OTP.")
                    self.otp_status_label.setStyleSheet("color: red")
        else:
            print("OTP not generated, Please send OTP first")
            self.status_label.setText("OTP not generated, Please send OTP first.")
            self.status_label.setStyleSheet("color: red")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = OTPVerifyGUI()
    window.show()
    sys.exit(app.exec_())
