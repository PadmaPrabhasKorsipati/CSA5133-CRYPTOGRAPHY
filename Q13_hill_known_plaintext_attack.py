import numpy as np

def main():
    plaintext = np.array([[7,4],[11,15]])
    ciphertext = np.array([[19,7],[0,5]])
    try:
        p_inv = np.linalg.inv(plaintext)
        key = ciphertext @ p_inv
        print("Estimated key matrix:")
        print(np.round(key).astype(int))
    except Exception:
        print("The selected plaintext matrix is not invertible.")

if __name__ == "__main__":
    main()

# Sample Output:
# Estimated key matrix:
# [[...]]
# The experiment demonstrates recovery of a Hill key from plaintext-ciphertext pairs.
