        //
        // $(document).ready(function() {
        //     let weathericon = {
        //         '01' : 'fas fa-sun',
        //         '02' : 'fas fa-cloud-sun',
        //         '03' : 'fas fa-cloud',
        //         '04' : 'fas fa-cloud-meatball',
        //         '09' : 'fas fa-cloud-sun-rain',
        //         '10' : 'fas fa-cloud-showers-heavy',
        //         '11' : 'fas fa-poo-storm',
        //         '13' : 'fas fa-snowflake',
        //         '50' : 'fas fa-fa-smog',
        //     };
        //
        //     $.ajax({
        //         url : 'http://api.openweathermap.org/data/2.5/weather?q=Seoul&appid=89f01b74b3f891c0789c0beb732223bc&units=metric',
        //         dataType : 'json',
        //         type : 'GET',
        //         success : function(data){
        //             var $Icon = (data.weather[0].icon).substr(0,2);
        //             var $Temp = Math.floor(data.main.temp) + '°C' ;
        //             var $city = data.name;
        //              $('.CurrIcon').append('<i class="' + weathericon[$Icon] +'"></i>');
        //              $('.CurrTemp').prepend($Temp);
        //              $('.City').append($city);
        //         }
        //     })
        // })
