## Branch Contains:
- OTPverify_Backend.py
- OTPverify_GUI.py
- OTP_Verification_System_Documentation.docx


# OTP Verification System

## Project Overview
This project aims to develop an OTP (One-Time Password) verification system, it is Python-based application designed to generate and validate OTPs (One-Time Passwords) for user authentication. The system generates a 6-digit OTP and sends it to the user's email address for verification. The user then enters the received OTP for verification. If the entered OTP matches the generated OTP, access is granted; otherwise, access is denied.

## Project Requirements
- **OTP Generation**: Implement a function to generate a 6-digit OTP randomly.
- **OTP Sending Simulation**: Develop a function to simulate sending the OTP to the user's email address.
- **OTP Entry Prompt**: Create a function to prompt the user to enter the OTP received in their email.
- **OTP Verification**: Implement a function to verify if the entered OTP matches the generated OTP.
- **Error Handling and User Interaction**: Ensure proper error handling and user-friendly prompts throughout the system. Allow the user to retry OTP entry in case of incorrect input.
- **GUI**: create a simple GUI interface for the OTP verification system to enhance user experience.

## Project Structure:
The project consists of two main components: the backend logic and the graphical user interface (GUI). The backend logic handles OTP generation, email sending, and OTP verification, while the GUI provides a user-friendly interface for interacting with the system. Refer below file
- Backend components : `OTPverify_Backend.py` 
- GUI components : `OTPverify_GUI.py`

## Components and Its Functionality:
* #### OTPverify_Backend.py : 
* **OTPVerifyFeatureBackend Class**: This class contains the backend logic for OTP generation, email sending, and OTP verification. It includes methods for generating OTPs, validating email addresses, sending OTPs via email, prompting users for OTP input, and verifying entered OTPs.
1. **generate_otp(self)**:
   - Generates a 6-digit OTP using random integers.
   - Returns the generated OTP if it consists of exactly 6 digits; otherwise, returns None.
2. **verify_email(self, email)**:
   - Verifies the format of the provided email address using a regular expression.
   - Returns True if the email format is valid; otherwise, returns False.
3. **send_otp(self, email)**:
   - Generates an OTP using the `generate_otp` method.
   - Constructs an email message containing the OTP and sends it to the provided email address using SMTP.
   - Prints a success message if the OTP is sent successfully and returns a tuple containing a boolean indicating success and the generated OTP.
4. **prompt_for_otp(self)**:
   - Prompts the user to enter the OTP sent to their email address.
   - Returns the entered OTP as a string.
5. **verify_otp(self, generated_otp, entered_otp)**:
   - Compares the entered OTP with the generated OTP.
   - Returns True if the entered OTP matches the generated OTP; otherwise, returns False.
6. Main Function 
 **Def main (self)**: (if __name__ == '__main__'):
- Contains commented-out code for testing the functionality of the OTPVerifyFeatureBackend class.
- Allows manual testing of OTP generation, sending, and verification by interacting with the console.
- Validates the OTP verification system's functionality and error handling.
### Note:
- The commented-out main function is intended for manual testing and validation purposes. Uncommenting and executing this section will allow testing of OTP generation, sending, and verification directly through the console.

*	**OTPVerification Class :** This class acts as an interface between the GUI and the backend features. It provides methods for sending OTPs and verifying entered OTPs.
1. **__init__(self)**:
   - Initializes the OTPVerification class.
   - Creates an instance of the OTPVerifyFeatureBackend class to access OTP generation, sending, and verification features.
2. **send_otp(self, email)**:
   - Calls the `send_otp` method of the OTPVerifyFeatureBackend class to send the OTP to the provided email address.
   - Returns a tuple containing a boolean indicating whether the OTP sending was successful and the generated OTP.
3. **verify_otp(self, generated_otp, entered_otp)**:
   - Calls the `verify_otp` method of the OTPVerifyFeatureBackend class to verify the entered OTP against the generated OTP.
   - Returns a boolean indicating whether the entered OTP matches the generated OTP.

* #### OTPverify_GUI.py :
•	**OTPVerifyGUI Class :** This class implements the graphical user interface using PyQt5. It includes widgets for inputting email addresses and OTPs, buttons for sending and verifying OTPs, and labels for displaying status messages.
1. **__init__(self)**:
   - Initializes the OTPVerifyGUI class, creating the graphical user interface (GUI) for OTP verification.
   - Sets the window title, background color, and geometry (size and position).
   - Creates labels, input fields, status labels, and buttons for email, OTP, status messages, and actions (send OTP, verify OTP).
   - Configures the style (font size, weight, color, background color, border) of labels, buttons, and input fields.
   - Sets placeholder text for email and OTP input fields and disables the OTP input initially.
   - Connects the `clicked` signals of the send OTP and verify OTP buttons to their respective methods.
2. **send_otp_button(self)**:
   - Retrieves the email entered by the user from the email input field.
   - Validates the email format using a regular expression.
   - If the email format is valid, calls the `send_otp` method of the `OTPVerification` class to send the OTP.
   - If OTP sending is successful, enables the OTP input field, updates the status label, and stores the generated OTP.
   - If OTP sending fails, disables the OTP input field and updates the status label with an error message.
3. **verify_otp_button(self)**:
   - Retrieves the entered OTP from the OTP input field.
   - Retrieves the generated OTP from the instance variable `generated_otp`.
   - If a generated OTP exists and the entered OTP is not empty, calls the `verify_otp` method of the `OTPVerification` class to verify the OTP.
   - Updates the status label with either a success message for correct OTP or an error message for incorrect OTP.
   - If no OTP is generated, updates the status label with an error message prompting the user to send OTP first.
#### Main Function (if __name__ == '__main__'):
- Initializes a PyQt5 application.
- Creates an instance of the OTPVerifyGUI class, representing the OTP verification GUI window.
- Shows the OTP verification GUI window.
- Executes the PyQt5 application event loop.
### Note:
- The `OTPVerifyGUI` class encapsulates the graphical user interface for OTP verification, while the functionality for OTP generation, sending, and verification is implemented in the `OTPVerification` class imported from `OTPverify_Backend`.

## Dependencies & Libraries
- Python 3.x
- Smtplib
- PyQt5
- Tkinter
- Re
- Random
- Sys
  
## Usage:
1. Run the OTPVerifyGUI.py script to launch the OTP Verification System.
2. Enter your email address in the provided input field and click the "Send OTP" button.
3. Check your email inbox for the OTP sent by the system.
4. Enter the received OTP in the OTP input field and click the "Verify OTP" button.
5. If the entered OTP is valid, access will be granted; otherwise, access will be denied.
## How to Run the Program
1. Clone the repository to your local machine.
2. Navigate to the project directory.
3. Run the Python script `OTPverify_Backend.py`
4. After successfull execution of `OTPverify_Backend.py` execute the `OTPverify_GUI.py`
5. Follow the prompts to generate, send, and verify the OTP.

## Test Cases:
1. **Valid Email Address**: Verify that the system accepts valid email addresses for OTP delivery.
2. **Invalid Email Address**: Verify that the system rejects invalid email addresses and prompts the user to enter a valid one.
3. **Successful OTP Generation**: Verify that the system successfully generates a 6-digit OTP and sends it to the user's email address.
4. **Invalid OTP Entry**: Verify that the system prompts the user to enter a valid OTP if the entered OTP is incorrect.
5. **OTP Verification**: Verify that the system correctly verifies the entered OTP and grants access if it matches the generated OTP.

## Achievements:
1. Successfully implemented and verified the functionality of OTP generation, sending, and verification processes.
Ensured accuracy and reliability in generating, sending, and verifying OTPs.
2. Maintained high code quality by following Python best practices.
Ensured readability and maintainability of the codebase.
Provided comprehensive documentation for easy understanding and future reference.
3. Implemented robust error handling mechanisms to handle invalid inputs and errors gracefully.
Provided clear and user-friendly prompts for seamless interaction with the system.
4. Tested the system under various scenarios to ensure robustness and reliability.
Addressed edge cases and potential issues to enhance system resilience.
5. Designed and implemented a creative and user-friendly GUI interface.
Enhanced user experience through intuitive design and interaction.
