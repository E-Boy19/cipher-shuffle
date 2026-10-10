# CipherShuffle 🔐

A simple Python-based text substitution cipher that randomly shuffles vowels and consonants to translate text into a secret-looking format.

## 📌 About

CipherShuffle is a command-line application built using Python. It generates randomized mappings for vowels and consonants and uses them to transform user input into an encoded message.

The mappings are stored in a local file, allowing the same substitution pattern to be reused across multiple executions.

## ✨ Features

- **Randomized Character Mapping:** Shuffles vowels and consonants independently.
- **Persistent Mappings:** Saves the generated mappings in `data/data.data`.
- **Case Preservation:** Maintains uppercase and lowercase letters in the translated text.
- **Character Preservation:** Leaves spaces, numbers, punctuation, and special characters unchanged.
- **Interactive CLI:** Translate multiple messages in one session.
- **Simple Exit:** Enter `q` to quit the application.

## 🛠️ Tech Stack

- Python 3
- `random` — Randomizes character mappings.
- `os.path` — Handles file paths and checks file existence.
- `os` — Creates the data directory.

## 📂 Project Structure

```text
CipherShuffle/
├── main.py
├── data/
│   └── data.data
└── README.md
```

The `data/` directory and `data.data` file are generated automatically when the program runs for the first time.

## 🚀 Getting Started

### Prerequisites

- Python 3 installed on your system.


## 💻 Usage

Run the program and enter the text you want to translate.

```text
Enter the text (or q to quit): Hello World
Translation : [encoded message]

Enter the text (or q to quit): Python
Translation : [encoded message]

Enter the text (or q to quit): q
Press enter to quit
```

The actual output depends on the randomly generated character mapping stored in the data file.

## ⚙️ How It Works

1. **Initialize character sets:** The program defines separate lists of consonants and vowels.
2. **Generate shuffled mappings:** Both lists are independently shuffled to create randomized substitutions.
3. **Store the mappings:** The shuffled characters are saved in `data/data.data` if the file does not already exist.
4. **Load existing mappings:** On subsequent executions, the program loads the saved mappings instead of generating new ones.
5. **Translate the input:** Each alphabetic character is replaced with its corresponding mapped character while preserving its case.
6. **Preserve other characters:** Characters outside the defined vowel and consonant sets remain unchanged.

## ⚠️ Limitations

- This is a basic substitution cipher intended for learning and experimentation.
- The mapping is fixed once generated unless the stored data file is deleted.
- Spaces, punctuation, and numbers are not encoded.
- The cipher is **not cryptographically secure** and should not be used to protect sensitive information.

## 👨‍💻 Author

**Aaditya Garud**

Built with Python 🐍
