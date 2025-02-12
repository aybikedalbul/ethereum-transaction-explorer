🚀 Ethereum Transaction Explorer
Welcome to the Ethereum Transaction Explorer! This web application allows users to view the latest transactions associated with a specific Ethereum wallet address on the Ethereum mainnet. Built with Django and Web3.py, it provides a seamless experience for exploring Ethereum transactions.

🌟 Features
🔍 Transaction Lookup: Retrieve and display the latest transactions for a given Ethereum wallet address.
📋 Detailed Information: View transaction details including hash, sender, recipient, and value.
🛠️ Technologies Used
Python: 3.12.3
Django: 5.1.6
Web3.py: 7.8.0
Ethereum Mainnet
📦 Installation
Clone the Repository:

bash
Copy
Edit
git clone https://github.com/aybikdedalbul/ethereum-transaction-explorer.git
cd ethereum-transaction-explorer
Create and Activate a Virtual Environment:

bash
Copy
Edit
python3 -m venv venv
source venv/bin/activate  # On Unix or MacOS
# or
venv\Scripts\activate  # On Windows
Install Dependencies:

bash
Copy
Edit
pip install -r requirements.txt
Apply Migrations:

bash
Copy
Edit
python manage.py migrate
Start the Development Server:

bash
Copy
Edit
python manage.py runserver
Access the Application:

Open your web browser and navigate to http://127.0.0.1:8000/.

🚀 Usage
On the homepage, enter an Ethereum wallet address in the search field and click the "Search" button.
The application will display the latest transactions associated with the provided address.
For each transaction, details such as the hash, sender address, recipient address, and value are shown.
🤝 Contributing
Contributions are welcome! Please open an issue to discuss what you would like to change or add.

📄 License
This project is licensed under the MIT License. See the LICENSE file for details.