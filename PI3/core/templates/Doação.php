<!DOCTYPE html>
<html>

<head>
    <title>Página de Doação</title>
    <link rel="stylesheet" type="text/css" href="Doação.css">
</head>

<body>
    <header>
        <!-- Cabeçalho -->
        <div class="logo">
            <img src="logo_empresa.png" alt="Logo da Empresa">
        </div>
        <div class="header-buttons">
            <button>Login</button>
            <button>Cadastro</button>
            <button>Contato</button>
        </div>
    </header>

    <div class="main-content">
        <div class="thank-you">
            <!-- Texto de agradecimento -->
            <h1>OBRIGADO POR DOAR!!!</h1>
            <p>Gostaríamos de expressar nossa mais profunda gratidão por sua generosa contribuição para o nosso site de doação de alimentos.<br>
             Seu apoio é inestimável e fundamental para o sucesso desta iniciativa. <br>
             Com a sua ajuda, pudemos oferecer assistência alimentar a quem mais precisa. <br>
             Obrigado por fazer parte desta jornada e por ser a luz que ilumina o caminho dos que necessitam. <br>
             Sua solidariedade é incrivelmente valiosa.</p>
            <p>Com gratidão,<br>Equipe Food Share</p>
        </div>

        <div class="form-section">
            <!-- Formulário -->
            <form>
                <div style="display: flex; justify-content: center;">
                    <button type="button" class="doar-vez-button">Doar uma vez</button>
                    <button type="button" class="doar-mensal-button">Doar mensalmente</button>
                </div><br><br>

                <label for="nome">Nome Completo:</label>
                <input type="text" id="nome" name="nome" required><br><br>

                <label for="telefone">Telefone:</label>
                <input type="tel" id="telefone" name="telefone" required><br><br>

                <label for="email">Email:</label>
                <input type="email" id="email" name="email" required><br><br>

                <label for="endereco">Endereço:</label>
                <input type="text" id="endereco" name="endereco" required><br><br>

                <div style="display: flex;">
                    <input type="text" id="cidade" name="cidade" required placeholder="Cidade">
                    <input type="text" id="estado" name="estado" required placeholder="Estado">
                    <input type="text" id="cep" name="cep" required placeholder="CEP">
                </div><br><br>

                <label for="confirm_alimentos">
                    <input type="checkbox" id="confirm_alimentos" name="confirm_alimentos" required> Confirmo que os alimentos doados estão em boas condições e dentro do prazo de validade
                </label><br><br>

                <label for="confirm_privacidade">
                    <input type="checkbox" id="confirm_privacidade" name="confirm_privacidade" required> Li e concordo com a Política de Privacidade e o uso dos meus dados pessoais para a finalidade indicada
                </label><br><br>

                <div style="display: flex; justify-content: center;">
                    <button type="submit" class="doar-button">DOAR</button>
                </div>
            </form>
        </div>
    </div>

    <footer>
        <!-- Rodapé -->
        <div class="contact-info">
            <div class="info">
                <img src="telefone_icone.png" alt="Imagem de Telefone">
                <p>(11) 1234-5678</p>
            </div>
            <div class="info">
                <img src="email_icone.png" alt="Imagem de E-mail">
                <p>contato@empresa.com</p>
            </div>
            <div class="info">
                <img src="endereço_icone.png" alt="Imagem de Endereço">
                <p>Rua da Empresa, 123</p>
            </div>
        </div>
        <p class="credit">Crédito da imagem: Nome do Autor / Freepik</p>
    </footer>
</body>

</html>






















