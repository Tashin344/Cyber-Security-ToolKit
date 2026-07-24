# File Integrity Monitor

## Overview

A Python-based File Integrity Monitor (FIM) that detects file modifications, newly created files, and deleted files using SHA-256 hashing.

---

## Features

- SHA-256 file hashing
- Recursive directory scanning
- Per-directory baseline databases
- Detects modified files
- Detects newly created files
- Detects deleted files
- Generates scan reports
- Modular architecture

---

## Technologies Used

- Python 3
- hashlib
- json
- os
- time

---

## How to Run

```bash
python main.py
```

Enter the directory you want to monitor when prompted.

---

## Project Structure

```
main.py
compare.py
scanner.py
...
```

---

## Future Improvements

- Logging
- Real-time monitoring
- Ignore rules
- Command-line arguments