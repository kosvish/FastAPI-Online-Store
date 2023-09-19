// script.js
const userIcon = document.getElementById('user-icon');

// Обработчик клика на иконке пользователя
userIcon.addEventListener('click', async () => {
    // Проверка статуса аутентификации пользователя
    const response = await fetch('/auth/status'); // ендпоинт для аутенфикации
    if (response.status === 200) {
        // если Пользователь аутентифицирован
        window.location.href = '/user-profile'; // Перенаправление на страницу пользователя
    } else {
        // Пользователь не аутентифицирован
        window.location.href = '/login'; // Перенаправление на страницу входа
    }
});
