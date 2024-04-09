
import random
import smtplib
import re

# The OTPVerification class acts as an interface between the GUI
# and the backend features of OTP generation, sending, and verification
class OTPVerification:
    def __init__(self):
        self.otp_verify_feature = OTPVerifyFeatureBackend()
    def send_otp(self, email):
        return self.otp_verify_feature.send_otp(email)

    def verify_otp(self, generated_otp, entered_otp):
        return self.otp_verify_feature.verify_otp(generated_otp, entered_otp)

class OTPVerifyFeatureBackend():
    # Function to generate a 6-digit OTP
    def generate_otp(self):
        try:
            otp = ''.join([str(random.randint(0, 9)) for _ in range(6)])
            if len(otp) == 6:
                print("Generated OTP")
                print(f"{otp} is generated OTP")
                return otp
            else:
                print("Generated OTP is not exactly 6 digit ")
                return None
        except Exception as e:
            print("Error occurred while generating OTP:", str(e))
            return None

    # email format verifier
    def verify_email(self,email):
        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            print("Invalid email address format.")
            return False
        return True

    # Function to send OTP to user's email address
    def send_otp(self, email):
        try:
            otp = self.generate_otp()
            if otp:
                sender_email = 'shushankit.automate@gmail.com'
                sender_password = 'eeaw kxia wmrc vlbe'

                subject = 'OTP Verification'
                body = f'Your OTP is: {otp}'

                with smtplib.SMTP('smtp.gmail.com', 587) as server:
                    server.starttls()
                    server.login(sender_email, sender_password)
                    server.sendmail(sender_email, email, f'Subject: {subject}\n\n{body}')
                    print(f"OTP sent successfully to {email}, OTP: {otp}")
                    return True, otp
            else:
                print("Failed to generate OTP.")
                return False, None
        except Exception as e:
            print("Failed to send OTP:", str(e))
            return False, None

    # Function to prompt user for OTP input
    def prompt_for_otp(self):
        return input("Enter the OTP sent to your email: ")

    # Function to verify entered OTP
    def verify_otp(self, generated_otp, entered_otp):
        if generated_otp == entered_otp:
            print("OTP verification successful")
            return True
        else:
            print("OTP entered is invalid")
            return False

    # Main function
    # def main(self):
    #     email = input("Enter your email address: ")
    #     if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
    #         print("Invalid email address. Please enter a valid email address.")
    #         return
    #     otp = self.generate_otp()
    #     self.send_otp(email, otp)
    #     # Prompt user for OTP entry and verify
    #     attempts = 3
    #     while attempts > 0:
    #         entered_otp = self.prompt_for_otp()
    #         if self.verify_otp(otp, entered_otp):
    #             print("OTP verification successful. Access granted.")
    #             break
    #         else:
    #             attempts -= 1
    #             print(f"Invalid OTP. {attempts} attempts remaining.")
    #     if attempts == 0:
    #         print("Maximum attempts reached. Access denied.")
#
# if __name__ == "__main__":
#     OTPVerifyFeatureBackend.main()
