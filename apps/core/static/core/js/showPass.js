function showPassword(event) {
    const passwordIcon = event.target; // El ícono que disparó el evento
    const passwordInput = passwordIcon.closest('div').querySelector('input[type="password"], input[type="text"]');

    if (!passwordInput) {
        console.error('No se encontró el campo de contraseña asociado.');
        return;
    }

    if (passwordInput.type === 'password') {
        passwordInput.type = 'text';
        passwordIcon.setAttribute('fill', '#000');
        passwordIcon.setAttribute('stroke', '#000');
    } else {
        passwordInput.type = 'password';
        passwordIcon.setAttribute('fill', '#bbb');
        passwordIcon.setAttribute('stroke', '#bbb');
    }
}