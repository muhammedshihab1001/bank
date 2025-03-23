# MSB Bank ATM Simulation

This is a simple ATM simulation program where users can perform various banking operations, such as depositing money, checking balance, withdrawing money, and transferring funds to other accounts.

## Features

1. **Login**  
   - User is prompted to enter a card number and PIN.  
   - Default login credentials are:
     - Card Number: `10101010`
     - PIN: `1234`
   
2. **Banking Operations**  
   Once logged in, users can perform the following operations:
   
   - **Deposit**  
     - Users can deposit money into their account.  
     - Minimum deposit amount: 100  
     - Maximum deposit amount: 20,000
   
   - **Balance Check**  
     - Displays the current balance in the account.
   
   - **Withdraw**  
     - Users can withdraw money from their account.  
     - Minimum withdrawal amount: 100  
     - Maximum withdrawal amount: 20,000  
     - If the balance is insufficient, the withdrawal request will fail.
   
   - **Transfer**  
     - Users can transfer funds to another account.  
     - Minimum transfer amount: 1  
     - Maximum transfer amount: 200,000  
     - Users are required to provide the bank name, IFSC code, account number, name, amount, and their PIN for authorization.
   
   - **Exit**  
     - Exits the program.

## Code Flow

1. **Login**  
   The program starts by prompting the user for their card number and PIN. If the correct credentials are entered, the program proceeds to the banking menu.

2. **Banking Menu**  
   The user can choose one of the following options:
   
   - Deposit
   - Balance
   - Withdraw
   - Transfer
   - Exit
   
   The program processes each option as follows:
   
   - **Deposit**: It checks the amount and ensures it's within the allowable range. The user is informed if the deposit is successful.
   - **Balance**: The program displays the current balance.
   - **Withdraw**: It checks the balance and ensures the amount is within the allowable withdrawal limits.
   - **Transfer**: The user needs to input additional details, including the recipient's information and the amount to transfer. If the transfer is successful, a receipt is generated.
   - **Exit**: The program exits.

## Requirements

- Python 3.x
- No additional libraries are required as it only uses the built-in `time` library for delays.

## How to Run

1. Make sure you have Python 3.x installed on your machine.
2. Copy the provided code into a Python file, for example, `msb_bank.py`.
3. Run the Python script from your terminal or command prompt:
   ```bash
   python msb_bank.py
