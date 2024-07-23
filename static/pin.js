document.addEventListener("DOMContentLoaded", function () {
    
    const pinbutton = document.querySelector(".pinbutton");

    var pincodeInput = document.getElementById("pincodeInput");
    var pincodeForm = document.getElementById("pincodeForm");

 

    const timerDiv = document.getElementById("timer");
    let countdown = 59;

    // Функция для обновления таймера каждую секунду
    function updateTimer() {
        if (countdown > 0) {
            try{
               timerDiv.textContent = `Осталось времени: ${countdown} секунд`;
            }
            catch(error){
                console.log("")
            }

            countdown -= 1;
            setTimeout(updateTimer, 1000);
        } else {
            timerDiv.style.display = "none";
            pinbutton.style.display = "block";
            // Дополнительные действия, которые нужно выполнить после истечения времени
        }
    }

    // Запустить таймер при загрузке страницы
    updateTimer();
});

document.addEventListener("DOMContentLoaded", function() {
    var pincodeInputs = [
        document.getElementById("pincodeInput1"),
        document.getElementById("pincodeInput2"),
        document.getElementById("pincodeInput3"),
        document.getElementById("pincodeInput4")
    ];
    var pincodeForm = document.getElementById("pincodeForm");

    pincodeInputs.forEach(function(input, index) {
        try{
            input.addEventListener("input", function() {
                if (input.value.length === 1) {
                    if (index < 3) {
                        // Перейти к следующему полю ввода после ввода символа
                        pincodeInputs[index + 1].focus();
                    } else {
                        // Если это последнее поле ввода, отправить форму
                        pincodeForm.submit();
                    }
                } else if (input.value.length === 0 && index > 0) {
                    // Если символ удален, вернуться к предыдущему полю ввода
                    pincodeInputs[index - 1].focus();
                }
            });}
            catch(error){
                console.log("")
            }
    });
});

//  document.addEventListener("DOMContentLoaded", function() {
//     var modal1 = document.getElementById("content");
//     var btn3 = document.getElementById("forgotPass");
//     var span1 = document.getElementById("close");

//     btn3.onclick = function () {
//         modal1.style.display = "block";
//     }

//     span1.onclick = function () {
//         modal1.style.display = "none";
//     }

//     window.onclick = function (event) {
//         if (event.target == modal1) {
//             modal1.style.display = "none";
//         }
//     }
//      });

