//Codigo do login
let lastClickedButton = null;

document.querySelectorAll('#loginForm button[type="submit"]').forEach(button => {
    button.addEventListener('click', function () {
        lastClickedButton = this;
    });
});

document.getElementById('loginForm').addEventListener('submit', async function (e) {
    e.preventDefault();

    const form = e.target;
    const data = new FormData(form);
    const action = lastClickedButton?.getAttribute('formaction') || form.getAttribute('action');

    try {
        const response = await fetch(action, {
            method: 'POST',
            body: data
        });

        let result;
        try {
            result = await response.json();
        } catch {
            throw new Error("Resposta não é JSON.");
        }

        if (response.ok) {
            window.location.href = result.redirect;
        } else {
            document.getElementById('errorMsg').innerText = result.mensagem || 'Erro ao processar.';
        }
    } catch (err) {
        document.getElementById('errorMsg').innerText = 'Erro de conexão ou servidor.';
        console.error(err);
    }
});

console.log("Alfredo");

// Animação para links do header (opcional)
document.querySelectorAll('.main-nav a').forEach(link => {
    link.addEventListener('mouseenter', () => {
        link.style.transform = 'scale(1.05)';
    });
    link.addEventListener('mouseleave', () => {
        link.style.transform = 'scale(1)';
    });
});