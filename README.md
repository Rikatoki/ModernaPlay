# ModernaPlay

ModernaPlay é um site desenvolvido como parte de um trabalho escolar, com o objetivo de criar um site e-commerce. O projeto não foi pensado para ser funcional ou utilizado como uma plataforma real, mas sim como exercício acadêmico e demonstração de conceitos básicos de back-end, front-end e organização de código.

## Sobre o Projeto

- **Proposto para fins didáticos**: O ModernaPlay serve apenas como exemplo para apresentação em colégio.
- **Listagem de jogos**: O site exibe uma lista de jogos com imagens, descrição, preço e links externos.
- **Autenticação de usuários**: Inclui um sistema básico de cadastro e login (não recomendado para uso real).
- **Estrutura modular**: O código está organizado em módulos para facilitar entendimento e aprendizado.

## Estrutura de Pastas

```
app/
├── __init__.py
├── config.py
├── data/
│   └── jogos.json
├── models/
│   ├── __init__.py
│   └── user.py
├── routes/
│   └── (rotas de autenticação, usuário, etc.)
├── services/
│   └── (serviços auxiliares)
├── static/
│   └── imgs/
```

## Como Executar Localmente

1. **Clone o repositório:**
   ```bash
   git clone https://github.com/Rikatoki/ModernaPlay.git
   cd ModernaPlay
   ```

2. **Crie e ative um ambiente virtual:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/macOS
   venv\Scripts\activate     # Windows
   ```

3. **Instale as dependências:**
   ```bash
   pip install flask flask_sqlalchemy
   ```

4. **Execute a aplicação:**
   ```bash
   flask run
   ```
   O site estará disponível localmente e pode ser explorado para fins de apresentação.

## Observações Importantes

- **Não utilize para fins comerciais ou reais!**
- As informações de usuários e jogos são apenas exemplos e não possuem proteção adequada.
- O foco é mostrar conceitos básicos de desenvolvimento web e organização de projetos em Python.

## Licença

Distribuído sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais informações.

## Autor

Hanisson Silva Pereira // Rikatoki

---

Este projeto foi feito exclusivamente para um trabalho escolar. Se quiser aprender ou contribuir, fique à vontade!
