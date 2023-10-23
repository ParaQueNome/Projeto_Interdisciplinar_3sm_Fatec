<!DOCTYPE html>
<html>
<head>
    <link rel="stylesheet" type="text/css" href="Cadastro.css">
    <title>Página de Cadastro</title>
</head>
<body>
    <header>
        <div class="logo">
            <img src="logo_empresa.png" alt="Logo da Empresa">
        </div>
        <div class="header-buttons">
            <button>Login</button>
            <button>Cadastro</button>
        </div>
    </header>
    <div class="container">
        <div class="image">
            <img src="cadastro3.jpg" alt="Imagem de Cadastro">
        </div>
        <div class="form">
            <h1>Cadastro</h1>
            <form method="POST" action="processa_cadastro.php">
                <label for="nome">Nome:</label>
                <input type="text" id="nome" name="nome" required><br>

                <label for="email">E-mail:</label>
                <input type="email" id="email" name="email" required><br>

                <label for="senha">Senha:</label>
                <input type="password" id="senha" name="senha" required><br>

                <label for="confirmaSenha">Confirme a Senha:</label>
                <input type="password" id="confirmaSenha" name="confirmaSenha" required><br>

                <button type="submit">Cadastrar</button>
            </form>
        </div>
    </div>
    <footer>
        <div class="contact-info">
            <div class="info">
                <img src="telefone_icone.png" alt="Ícone de Telefone">
                <p>(11) 1234-5678</p>
            </div>
            <div class="info">
                <img src="email_icone.png" alt="Ícone de Email">
                <p>contato@empresa.com</p>
            </div>
            <div class="info">
                <img src="endereço_icone.png" alt="Ícone de Endereço">
                <p>Rua da Empresa, 123</p>
            </div>
        </div>
        <p class="credit">Crédito da imagem: Nome do Autor / Freepik</p>
    </footer>
</body>
</html>



<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $nome = $_POST["nome"];
    $email = $_POST["email"];
    $senha = $_POST["senha"];
    $confirmaSenha = $_POST["confirmaSenha"];
    
    $erro = false;
    $mensagemErro = "";

    if (empty($nome) || empty($email) || empty($senha) || empty($confirmaSenha)) {
        $erro = true;
        $mensagemErro = "Todos os campos devem ser preenchidos.";
    } elseif (!filter_var($email, FILTER_VALIDATE_EMAIL)) {
        $erro = true;
        $mensagemErro = "E-mail inválido.";
    }

    $temNumero = preg_match('/\d/', $senha);  
    $temLetra = preg_match('/[A-Za-z]/', $senha);  

    if (strlen($senha) < 6 || !$temNumero || !$temLetra) {
        $erro = true;
        $mensagemErro = "A senha deve conter pelo menos 6 caracteres, incluindo números e letras.";
    } elseif ($senha !== $confirmaSenha) {
        $erro = true;
        $mensagemErro = "As senhas devem ser iguais.";
    }

    if (!$erro) {
        echo "Cadastro realizado com sucesso!";
    } else {
        echo "<p style='color: red;'>Erro: $mensagemErro</p>";
    }
}
?>






