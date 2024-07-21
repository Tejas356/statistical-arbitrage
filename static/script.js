$(document).ready(function(){
    $('#inputForm').on('submit', function(event){
        event.preventDefault();
        let odds1 = $('#odds1').val();
        let odds2 = $('#odds2').val();
        let bet_amount = $('#bet_amount').val();

        $.ajax({
            url: '/calculate',
            type: 'POST',
            contentType: 'application/json',
            data: JSON.stringify({'odds1': odds1, 'odds2': odds2, 'bet_amount': bet_amount}),
            success: function(response) {
                let resultDiv = $('#result');
                resultDiv.html('<h2>Results:</h2>');
                if (typeof response.result === 'string') {
                    resultDiv.append('<p>' + response.result + '</p>');
                } else {
                    $.each(response.result, function(key, value) {
                        resultDiv.append('<p>Stakes: ' + key + ' - Outcome: ' + value + '</p>');
                    });
                }
            }
        });
    });
});