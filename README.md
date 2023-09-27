# pucrio-mvp3-c

Este é um projeto básico (MVP) para estudo e avaliação da disciplina **Arquitetura de Software**.

O projeto é o componente C da solução, contendo a parte transacional do fluxo e integração com serviço externo para validar tokens de autorização.

O serviço externo utilizado é a api [Platzi Fake Store API](https://fakeapi.platzi.com/en/rest/auth-jwt) e não demanda de cadastro.

## Rodando o projeto

### Instale o Docker

```bash
sudo apt install docker-ce
```

Caso a instalação não seja concluída com sucesso, siga [esses passos](https://www.digitalocean.com/community/tutorials/how-to-install-and-use-docker-on-ubuntu-20-04) para pré-configurar seu ambiente.

### Construa a imagem

```bash
docker build --tag mvp3-a .
```

### Suba seu container

```bash
docker run -d -p 5001:5001 mvp3-a
```
