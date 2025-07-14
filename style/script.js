//Codigo do login
let lastClickedButton = null

// Captura qual botão foi clicado
document.querySelectorAll('#loginForm button[type="submit"]').forEach(button => {
    button.addEventListener('click', function () {
        lastClickedButton = this
    })
})

document.getElementById('loginForm').addEventListener('submit', async function (e) {
    e.preventDefault()

    const form = e.target
    const data = new FormData(form)

    // Usa o formaction do botão clicado (não do form)
    const action = lastClickedButton?.getAttribute('formaction') || form.getAttribute('action')

    try {
        const response = await fetch(action, {
            method: 'POST',
            body: data
        })

        const result = await response.json()

        if (response.ok) {
            window.location = result.redirect
        } else {
            document.getElementById('errorMsg').innerText = result.mensagem || 'Erro ao processar.'
        }
    } catch (err) {
        document.getElementById('errorMsg').innerText = 'Erro de conexão ou servidor.'
        console.error(err)
    }
})