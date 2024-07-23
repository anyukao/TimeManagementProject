// JavaScript (script.js):

// Функция, которая открывает всплывающее окно
function openPopup() {
    document.getElementById("popup").style.display = "block";
}

document.getElementById("forgotPass").addEventListener("click", openPopup);

document.getElementById("close-popup").addEventListener("click", function () {
    document.getElementById("popup").style.display = "none";
});

// Валидация номера телефона (9 цифр после кода страны)
document.getElementById("send-code").addEventListener("click", function () {
    const countryCode = document.getElementById("country-code").value;
    const phoneNumber = document.getElementById("phone").value;

    if (/^\d{9}$/.test(phoneNumber)) {
        const fullPhoneNumber = countryCode + phoneNumber;
        // Здесь вы можете отправить fullPhoneNumber в базу данных
        alert("Номер телефона для сохранения: " + fullPhoneNumber);
    } else {
        alert("Пожалуйста, введите 9 цифр в поле номера телефона.");
    }
});
