document.addEventListener("DOMContentLoaded", function () {
    const phoneInput = document.getElementById("phone-input");

    phoneInput.addEventListener("input", function (event) {
        const input = event.target;
        const inputValue = input.value.replace(/\D/g, "").substring(0,
            9); // Удаление всего, кроме цифр и ограничение в 8 символов

        if (inputValue.length > 5) {
            const maskedValue =
                `${inputValue.substring(0, 3)} ${inputValue.substring(3, 6)} ${inputValue.substring(6, 9)}`;
            input.value = maskedValue;
        } else if (inputValue.length > 2) {
            const maskedValue =
                `${inputValue.substring(0, 3)} ${inputValue.substring(3, 6)}`;
            input.value = maskedValue;
        } else {
            input.value = inputValue;
        }
    });

    
});


document.addEventListener("DOMContentLoaded", function() {
    var value = document.getElementById("popup2_check");; // Здесь установите значение true или false в зависимости от вашей логики
    var popup2 = document.getElementById("popup2");

    if (value) {
        popup2.style.visibility = "visible";
        popup2.style.opacity = "1";
    }
});

document.addEventListener("DOMContentLoaded", function() {
    var closeButton = document.getElementById("closeButton");
    var popup2 = document.getElementById("popup2");

    closeButton.addEventListener("click", function(event) {
        event.preventDefault(); // Предотвращаем стандартное поведение ссылки (переход по якорю)

        // Устанавливаем пару стилей для popup2
        popup2.style.visibility = "hidden";
        popup2.style.opacity = "0";
    });
});
