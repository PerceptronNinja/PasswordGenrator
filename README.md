# Password Generator Web App

A secure password generator built with Flask. This web application allows users to generate random passwords based on customizable criteria like length, inclusion of uppercase letters, numbers, and special characters.

---

## Features

- Generate secure, random passwords.
- Customize password length.
- Include/exclude uppercase letters, numbers, and special characters.
- Simple and intuitive user interface.
- Responsive design for all screen sizes.

---

## Directory Structure

```
PasswordGenerator/
├── app.py                 
├── password_generator.py
├── templates/
│   ├── base.html
│   ├── index.html 
├── static/
│   └── styles.css
├── requirements.txt
├── README.md
```

---

## Requirements

- Python 3.7 or higher
- Flask 2.x

---

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/PasswordGenerator.git
   cd PasswordGenerator
   ```

2. **Create a virtual environment** (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

---

## Usage

1. **Run the application**:
   ```bash
   python app.py
   ```

2. **Access the application**:
   Open your browser and navigate to [http://127.0.0.1:5000](http://127.0.0.1:5000).

3. **Generate a password**:
   - Specify the desired password length.
   - Choose whether to include uppercase letters, numbers, and special characters.
   - Click "Generate Password" to get your secure password.

---

## Screenshots
<img width="1470" alt="387665800-47e0f72c-32b1-4ae5-a408-52bc848705c1" src="https://github.com/user-attachments/assets/8904f81d-01f0-40a1-8f05-93ce208f7d97">

## Future Enhancements

- **Save Passwords**: Allow users to save and retrieve generated passwords.
- **User Accounts**: Add user authentication for personal password management.
- **Password Strength Checker**: Evaluate the strength of generated passwords.
- **Mobile App**: Extend functionality to a mobile platform.

---

## Contributing

Contributions are welcome! Feel free to submit a pull request or open an issue.

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
