'use strict';

(function() {
    let textBox = $('#text'),
        questionBox = $('#question'),
        // Это путь, по которому javascipt запрашивает ответ от сервера
        // То есть в urls.py должно быть что-то соответствующее.
        engineUri = '/api/request';

    function request(question) {
        // Перед тем, как отправить запрос на сервер, заблокируем поле ввода.
        // Так как javascipt асинхронный, следующий запрос можно будет отправить,
        // пока еще не будет получен предыдущий. Нам так не надо
        questionBox.prop('disabled', true);

        $.ajax({
            url: engineUri,
            type: 'POST',
            data: { data: question },

            // Здесь предусмотрено, что сервер будет просто отдавать текст.
            // Не json, а текст. Этот текст будет содержаться в response
            success: function(response) {
                textBox.text(response);
                // После выполнения запроса разблокируем поле
                questionBox.prop('disabled', false);
                // Если запрос был успешным и получен ответ, то поле надо очистить
                questionBox.val('');
                // И снова поставить курсор на поле
                questionBox.focus();
            },

            error: function(xhr, errormsg, err) {
                console.log(errormsg);
                textBox.html('С сервером что-то не то :( <br> Попробуй позже');
                questionBox.prop('disabled', false);
                questionBox.focus();
            }
        });
    }

    questionBox.on('keydown', function(e) {
        // Если была нажата 13 клавиша, то есть Enter, то отправим запрос,
        // сказав при этом браузеру, что мы займемся обработкой сами и нам не надо помогать
        if ( e.which === 13 ) {
            e.preventDefault();
            request(questionBox.val());
        }
    });
})();