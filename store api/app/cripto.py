from cryptography.fernet import Fernet #IMPORTA MÓDULO

import pandas as pd

def gerar_chave():
    chave = Fernet.generate_key() #GERA UMA CHAVE RANDÔMICA
    print (chave)

    with open('chave.key', 'wb') as file:
        file.write(chave)
        file.close()



def gerar_relatorio(con):
    
    #  abrindo a chave
    with open('chave.key', 'rb') as filekey:
        key = filekey.read()

        # usando a chave gerada
        fernet = Fernet(key)

        # abrindo o arquivo original para criptografar
        #with open('nba.csv', 'rb') as file:
        #original = file.read()

        # criptografar o arquivo
        df = pd.read_sql_query("select * from customer",con)

        for i in df.index:
            encrypted = fernet.encrypt(bytes(df['customerNumber'][i]))
            df['customerNumber'][i] = encrypted
            
        print(df)
        return str(df)
        
        # abrir o arquivo no modo de gravação e
        # gravar os dados criptografados
        #with open('nba.csv', 'wb') as encrypted_file:
        #encrypted_file.write(encrypted)encrypted_file.write(encrypted)
if __name__ == "__main__":
    gerar_chave()
