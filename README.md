
# RSA Project

This repository provides a full implementation of the RSA (Rivest–Shamir–Adleman) cryptosystem in Python, developed as part of the CS1702 Network Security assignment. It features key generation, encryption and decryption functionalities, along with a detailed technical report and result analysis.
---

## Project Structure

```
RSA/
├── Code/
│   └── RSA_Implementation_CS22B1049.py   # Python implementation of RSA
│
├── Report/
│   └── RSA_Report_CS22B1049.pdf          # Detailed project report
│
├── Result/
│   └── RSA_Results_CS22B1049.png         # Output visualization or encryption result screenshot
│
└── README.md                             # Project description and instructions
```

---

## About RSA

**RSA (Rivest-Shamir-Adleman)** is an asymmetric cryptographic algorithm used for secure data transmission. It plays a vital role in digital security systems and serves as the foundation for many secure communication protocols.

RSA uses two keys:
- **Public Key (e, n)** to encrypt messages.
- **Private Key (d, n)** to decrypt them.

The security of RSA lies in the computational difficulty of factoring large prime products.

---

## Features

- Asymmetric Key Encryption
- Data Confidentiality and Authentication
- Widely Adopted in Security Protocols
- Decryption of ciphertext back to original message
- Scalability and Flexibility

---

## How to Run the Code

### 1. Clone the Repository
```bash
git clone https://github.com/vardhan132/RSA.git
cd RSA
```

### 2. Run the RSA Program
```bash
python Code/RSA_Implementation_CS22B1049.py
```

Follow the prompts to input your plaintext message and see encrypted and decrypted results.

---

## Report

The complete technical explanation of RSA is provided in the [`Report/RSA_Report_CS22B1049.pdf`](Report/RSA_Report_CS22B1049.pdf). It covers:
- Overview of RSA
- Methodology (Key Generation, Encryption, Decryption)
- Applications of RSA
- Keyspace and security analysis
- Conclusion

---

## Result

An example result of RSA encryption and decryption is available in the [`Result/RSA_Results_CS22B1049.png`](Result/RSA_Result_CS22B1049.png) file.

---

## Applications of RSA

- Secure email communication (PGP)
- Digital signatures
- SSL/TLS certificates
- Secure authentication
- Blockchain wallets and identities

---

## Security Considerations

- Determined by the size of the modulus nnn; modern RSA implementations typically use key lengths ranging from 2048 to 4096 bits.
- Depends on the computational difficulty of factoring large semi-prime numbers. 
- While RSA remains secure against classical attacks, it is theoretically breakable by Shor’s algorithm on a sufficiently powerful quantum computer. 

---
