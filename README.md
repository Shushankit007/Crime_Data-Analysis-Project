# OTP Verification System

## Project Overview
This project aims to develop an OTP (One-Time Password) verification system in Python. The system generates a 6-digit OTP and sends it to the user's email address for verification. Upon receiving the OTP, the user enters it into the system for validation. If the entered OTP matches the generated OTP, access is granted; otherwise, access is denied.

## Project Requirements
- **OTP Generation**: Implement a function to generate a 6-digit OTP randomly.
- **OTP Sending Simulation**: Develop a function to simulate sending the OTP to the user's email address.
- **OTP Entry Prompt**: Create a function to prompt the user to enter the OTP received in their email.
- **OTP Verification**: Implement a function to verify if the entered OTP matches the generated OTP.
- **Error Handling and User Interaction**: Ensure proper error handling and user-friendly prompts throughout the system. Allow the user to retry OTP entry in case of incorrect input.
- **GUI**: create a simple GUI interface for the OTP verification system to enhance user experience.

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

## Dependencies & Libraries
- Python 3.x
- Smtplib
- PyQt5
- Tkinter
- Re
- Random
- Sys
  
## Files
- OTPverify_Backend.py
- OTPverify_GUI.py
- OTP_Verification_System_Documentation.docx

## How to Run the Program
1. Clone the repository to your local machine.
2. Navigate to the project directory.
3. Run the Python script `OTPverify_Backend.py`
4. After successfull execution of `OTPverify_Backend.py` execute the `OTPverify_GUI.py`
5. Follow the prompts to generate, send, and verify the OTP.

