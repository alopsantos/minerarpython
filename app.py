from hashlib import sha256
import requests


def aplicar_sha256(texto):
    return sha256(texto.encode("ascii")).hexdigest()


def minerar(num_bloco, transacoes, hash_anteiror, qtde_zeros):
    nonce = 357820842

    while True:
        texto = str(num_bloco) + transacoes + hash_anteiror + str(nonce)

        meu_hash = aplicar_sha256(texto)
        print(meu_hash)
        if meu_hash.startswith("0" * qtde_zeros):
            return nonce, meu_hash
        nonce += 1


if __name__ == "__main__":
    response = requests.request(
        "GET", "https://blockchain.info/latestblock").json()
    print(response["hash"])

    num_bloco = int(response["block_index"]) + 1
    transacoes = str(response["txIndexes"])
    qtde_zeros = 20
    hash_anteiror = response["hash"]

    resultado = minerar(num_bloco, transacoes, hash_anteiror, qtde_zeros)

    print(resultado)
