# Lendo arquivo Cnab

Criação de uma interface web que aceite upload do arquivo CNAB, normalize os dados e armazene-os em um banco de dados relacional e exiba essas informações em tela.

### 🚰 Fluxo esperado

- É enviado um documento .txt com dados CNAB via upload.
- Os dados são armazenados em um banco de Dados;
- Retorna para o usuário o nome do estabelicmento, o tipo de transação e o valor, juntamento com o total do saldo em conta.;
 

# Observações sobre o projeto:
---

>### Este projeto foi desenvolvido com Python e Djando RestFramework então ao iniciar o projeto:
###  Crie o ambiente virtual
```
python -m venv venv
```
### Ative o venv
```bash linux: 

source venv/bin/activate

```

### Instale as dependências 
```
pip install -r requirements.txt
```
### Execute as migrações
```
python manage.py migrate
```



---
>### Certifique-se de que o projeto esta rodando antes de acessar a documentação.
# Exemplos básicos de requisição:
   
    Method POST
    Rota: http://localhost:8000/api/upload/cnab
    
    Documento .txt que contem o seguinte conteudo: 
    3201903010000014200096206760174753****3153153453JOÃO MACEDO   BAR DO JOÃO

    Enviado: {
      Binary File 
    }
    
    Recebido: [
	{
		"id": 22,
		"tipo": "3",
		"data": "20190301",
		"valor": "0000014200",
		"cpf": "09620676017",
		"cartao": "4753****3153",
		"hora": "153453",
		"dono_da_loja": "JOÃO MACEDO",
		"nome_loja": "BAR DO JOÃO"
	}
]
    
---
    
    Method GET
    Rota: http://localhost:8000/api/dados/
    
    Recebido: {
	"Transações": [
		{
			"loja": "BAR DO JOÃO",
			"tipo": "3",
			"valor": 142.0
		}
	],
	"SALDO EM CONTA": -142.0
}
    

---
>### Esse projeto ainda está em processo de desenvolvimento.
>### Falta:
> Deploy da API
> Tela com opção de enviar o documento e retornar uma lista.(Frontend)


