# RandomDATA101
A idéia é montar um gerador de dados aleatórios com uma vasta variedade de keys/values em determinado objeto. Várias linguagens estarão disponíveis e TODAS elas terão o mesmo uso. O arquivo final será um JSON com os dados gerados. O objeto inicial vai ser "human".

Exemplo: Ao executar o script ou fazer uma requisição à API (Possívelmente em algum futuro?), o usuário poderá escolher uma das diferentes possibilidades de conteúdo que será gerado e alimentado em um JSON. Em tese, centenas de values pairs vão estar disponíveis em centenas de keys do JSON.
```
{
  "human": {
    "data":{ 
      "name": [
          "fullname": "Paolo Django de Santo",
          "name": "Paolo",
          "surname": "Django de Santo"
        ],
      "age": "22",
      "bloodtype": "A+",
      e mais 1000 opções geradas aleatórios e automaticamente...
    }
  }
}

        "fullname": "Paolo Django de Santo"
            /\              /\
            |               |
           Key             value

```


# Linguagem inicial:
- Python

## Passo à passo
- [X] Primeiros passos (criar repositório, iniciar o readme).
- [X] Escrever idéia inicial.
- [X] Determinar quais serão as linguagens iniciais disponíveis.
- [X] Determinar qual vai ser a tree dos arquivos.
- [ ] Criar IMAGEM e LOGO para o reposítório.
- [ ] Melhorar o README a partir das atualizações do reposítório.
- [ ] Documentar TUDO.
- [ ] Melhorar a documentação. \o/
- [ ] Escolher a keys da opção inicial.
- [ ] Escolher e escrever as centenas de values para cada KEY individual. (Keys com values numéricas não necessitarão dessa opção(Podemos gerar valores números aleatórios com alguns métodos ou frameworks(math.Random() em python)).)
    * Template: nameFem = {"ana", "lucia", "Jessica", "Brianna"};
    * Template: nameMan = {"Gabriel", "Joseph", "Khan", "Victor"};
- [ ] Estudar qual será a melhor opção para o algoritmo (velocidade e facilidade na manutenção)(Colocar tudo direto no JSON junto ou dividir tudo em subcamadas?)(Dividir em arrays ou deixar tudo em uma única array).
- [ ] Funcional ou OOP?
- [ ] Vídeo demonstrando algoritmo em execução SEM JSON (fase alpha).
- [ ] Vídeo demonstrando algoritmo em execução COM JSON (fase beta).
- [ ] Adicionar opção para imagem aleatória de uma pessoa não-existente (Opcional).
    * API para imagem: https://thispersondoesnotexist.com/
    * Segunda opção: https://github.com/David-Lor/ThisPersonDoesNotExistAPI
- [ ] Fazer uma GUI (graphical user interface) para o algoritmo (?).
- [ ] Testar.
- [ ] Testar mais.
- [ ] Reorganizar o github e as branches (Dividir as pastas certinhas e os ReadME).
- [ ] Montar apresentação para divulgação com GIF.
- [ ] Melhorar código (Refactoring).
- [ ] Montar uma API para consumo do algoritmo.
- [ ] Refazer o script para outras linguagens (JS, C++).
