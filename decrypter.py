import os
import pyaes
import logging

# Configuração de log
logging.basicConfig(filename='ransomware_log.txt', level=logging.INFO, format='%(asctime)s - %(message)s')

def decrypt_file(file_name, key):
    """Descriptografa um arquivo com a chave fornecida."""
    try:
        # Abrir o arquivo criptografado
        with open(file_name, "rb") as file:
            file_data = file.read()

        # Criptografia com AES
        aes = pyaes.AESModeOfOperationCTR(key)
        decrypted_data = aes.decrypt(file_data)

        # Remover o arquivo criptografado
        os.remove(file_name)

        # Criar o arquivo descriptografado
        new_file_name = file_name.replace('.ransomwaretroll', '')  # Remove a extensão .ransomwaretroll
        with open(new_file_name, "wb") as new_file:
            new_file.write(decrypted_data)

        logging.info(f"Arquivo descriptografado com sucesso: {new_file_name}")
        print(f"Arquivo descriptografado com sucesso: {new_file_name}")
    
    except Exception as e:
        logging.error(f"Erro ao descriptografar o arquivo {file_name}: {e}")
        print(f"Erro ao descriptografar o arquivo {file_name}: {e}")

if __name__ == "__main__":
    # Nome do arquivo criptografado
    encrypted_file_name = "teste.txt.ransomwaretroll"  # Substitua com o arquivo criptografado
    
    # Chave de descriptografia
    key = b"testeransomwares"  # Substitua por uma chave mais segura, se necessário
    
    # Descriptografar o arquivo
    decrypt_file(encrypted_file_name, key)