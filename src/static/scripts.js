// script.js
const userIcon = document.getElementById('user-icon');

// Обработчик клика на иконке пользователя
userIcon.addEventListener('click', async () => {
    // Проверка статуса аутентификации пользователя
    const response = await fetch('/auth/status'); // ендпоинт для аутенфикации
    if (response.status === 200) {
        // если Пользователь аутентифицирован
        window.location.href = '/pages/user_profile'; // Перенаправление на страницу пользователя
    } else {
        // Пользователь не аутентифицирован
        window.location.href = '/pages/login'; // Перенаправление на страницу входа
    }
});



