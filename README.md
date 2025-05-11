# Back-Integracao

Este README descreve como utilizar as rotas da aplicação. A URL base para todas as requisições é `http://localhost/api`.

> Pre-fixo: `/api`

## Rotas

### 1. **GET** `/users`

- **Descrição:** Retorna a lista de usuários.

---

### 2. **POST** `/users`

- **Descrição:** Cria um novo usuário.
- **Exemplo de Body:**
  ```json
  {
    "first_name": "Carlos Eduardo",
    "email": "carlos.ed@empresa.com",
    "last_name": "Santos",
    "ip_address": "a0eebc99-9c0b-4ef8-bb6d-6bb9bd380a22",
    "data_nascimento": "1978-11-30"
  }
  ```

---

### 3. **DELETE** `/users/:user_id`

- **Descrição:** Remove um usuário específico.
- **Parâmetros:**
  - `user_id` (obrigatório): ID do usuário.

---

### 4. **POST** `/files`

- **Descrição:** Faz o upload de um arquivo e vincula ele à um usuário.
- **Exemplo de Body:**
  ```json
  {
    "file": "documento.pdf",
    "user_id": "2"
  }
  ```

---

### 5. **POST** `/zips`

- **Descrição:** cria uma linha no database para arquivos zips do usuário com um zip file name.
- **Exemplo de Body:**
  ```json
  {
    "user_id": 2,
    "zip_name": "zip_name_fake"
  }
  ```

---

### 6. **GET** `/files/users/:user_id`

- **Descrição:** Retorna a lista de todos os arquivos que o usuário tem registrado no banco de dados.
- **Parâmetros:**
  - `user_id` (obrigatório): ID do usuário.
- **Exemplo de saida:**

```json
[
  {
    "create_file": "2025-05-10T23:59:50.711731",
    "file_name": "Captura_de_tela_2024-03-13_114127.png",
    "file_path": "storage/files\\user_2_Captura_de_tela_2024-03-13_114127.png",
    "file_type": "image/png",
    "id": 13,
    "user_id": 2,
    "zip_id": 2
  }
]
```

---

### 7. **GET** `/zips/generate/:user_id`

- **Descrição:** Pega os arquivos vinculados a quele usuário e gera um zip dos arquivos na pasta de arquivos zip.
- **Parâmetros:**
  - `user_id` (obrigatório): ID do usuário.
- **Exemplo de saida:**

```json
{
  "zip_path": "storage/zips\\zip_2_zip_name_fake.zip"
}
```

---

### 8. **GET** `/files/download-zip`

- **Descrição:** O download do arquivo ZIP é feito via browser.
