import random
from sympy import isprime, mod_inverse

# Generate a larger random prime number
def generate_prime_number(bits=10):  # Default is 10 bits for larger primes
    while True:
        num = random.randint(2**(bits-1), 2**bits)  # Generate a random prime with specified bits
        if isprime(num):
            return num

# Generate RSA keys (public and private) with larger primes
def generate_keys(bits=10):  # Default to 10 bits for larger keys
    # Step 1: Choose two distinct prime numbers p and q
    p = generate_prime_number(bits)
    q = generate_prime_number(bits)
    while p == q:
        q = generate_prime_number(bits)

    # Step 2: Compute n = p * q
    n = p * q

    # Step 3: Compute Euler's Totient function φ(n) = (p - 1) * (q - 1)
    phi_n = (p - 1) * (q - 1)

    # Step 4: Choose a public exponent e such that 1 < e < φ(n) and gcd(e, φ(n)) = 1
    e = random.randint(2, phi_n - 1)
    while gcd(e, phi_n) != 1:
        e = random.randint(2, phi_n - 1)

    # Step 5: Compute the private key d such that e * d ≡ 1 (mod φ(n))
    d = mod_inverse(e, phi_n)

    # Public key (e, n)
    public_key = (e, n)
    # Private key (d, n)
    private_key = (d, n)

    return public_key, private_key

# Encryption function (with message splitting)
def encrypt(message, public_key):
    e, n = public_key
    encrypted_chunks = []
    
    # Split the message into chunks that fit the modulus
    chunk_size = (n.bit_length() // 8) - 1  # One byte less than the modulus size
    for i in range(0, len(message), chunk_size):
        chunk = message[i:i + chunk_size]
        message_int = int.from_bytes(chunk.encode(), 'big')
        
        # Ensure the message integer is smaller than n
        if message_int >= n:
            raise ValueError("Message chunk is too large for encryption with the chosen key size.")
        
        # Encrypt the chunk
        ciphertext = pow(message_int, e, n)
        encrypted_chunks.append(ciphertext)
    
    return encrypted_chunks

# Decryption function (with message recombination)
def decrypt(encrypted_chunks, private_key):
    d, n = private_key
    decrypted_message = []
    
    for chunk in encrypted_chunks:
        # Decrypt the chunk
        message_int = pow(chunk, d, n)
        
        # Convert the decrypted integer back to a string
        chunk_message = message_int.to_bytes((message_int.bit_length() + 7) // 8, 'big').decode()
        decrypted_message.append(chunk_message)
    
    return ''.join(decrypted_message)

# Helper function to compute gcd
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

# Main function to interact with the user
def rsa_program(bits=10):
    print("Welcome to the RSA Encryption Program!")

    # Generate RSA keys with larger primes
    public_key, private_key = generate_keys(bits)
    
    print("\nRSA Key Pair Generated!")
    print(f"Public Key (e, n): {public_key}")
    print(f"Private Key (d, n): {private_key}\n")

    # Get plaintext from the user
    message = input("Please enter the message you want to encrypt (plaintext):\n ")

    try:
        # Encrypt the message
        encrypted_message = encrypt(message, public_key)
        print(f"\nEncrypted message (ciphertext):\n {encrypted_message}\n\n")

        # Decrypt the message
        decrypted_message = decrypt(encrypted_message, private_key)
        print(f"Decrypted message:\n {decrypted_message}\n")
    except ValueError as e:
        print(f"Error: {e}")

rsa_program(bits=20)
