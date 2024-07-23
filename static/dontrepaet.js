
var inputs = document.querySelectorAll(".pincodeInput");

// Добавляем обработчик события на каждый элемент
inputs.forEach(function(input) {
    input.addEventListener("input", function(event) {
        var value = event.target.value;
        
        // Если длина значения больше 1, оставляем только первый символ
        if (value.length > 1) {
            event.target.value = value[0];
        }
    });
});