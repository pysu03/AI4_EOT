
$(document).ready(function() {

    $("#region").on("change", function(){
        console.log("change - success");
        console.log($("#region"));
        console.log($("#region").val());
        loadWeather($("#region").val());
    });

    function loadWeather (region) {
        console.log(region);
        $.ajax({
        url : `http://api.openweathermap.org/data/2.5/weather?q=${region}&appid=89f01b74b3f891c0789c0beb732223bc&units=metric`,
        dataType : 'json',
        type : 'GET',
        success : function(data){
            var $Icon = (data.weather[0].icon).substr(0,2);
            var $Temp = Math.floor(data.main.temp) + '°C';
            var $city = data.name;
            var $Humi = data.main.humidity + "%";
            console.log(data.main.humidity);
            console.log(data);
            console.log($Icon);
            console.log(weathericon);
             $('.CurrIcon').empty();
             $('.CurrTemp').empty();
             $('.City').empty();
             $('.Humidity').empty();
             $('.CurrIcon').append('<i class="' + weathericon[$Icon] +'"></i>');
             $('.CurrTemp').prepend($Temp);
             $('.City').append($city);
             $('.Humidity').prepend($Humi);
             selectClothes(data);
            }
        });
    }
    let weathericon = {
        '01' : 'fas fa-sun',
        '02' : 'fas fa-cloud-sun',
        '03' : 'fas fa-cloud',
        '04' : 'fas fa-cloud-meatball',
        '09' : 'fas fa-cloud-sun-rain',
        '10' : 'fas fa-cloud-showers-heavy',
        '11' : 'fas fa-poo-storm',
        '13' : 'fas fa-snowflake',
        '50' : 'fas fa-smog',
    };

    function selectClothes(data) {
        let clothes = document.querySelector('.today-clothes');
        let currentTemp = data.main.temp;
        console.log(data.main.temp);
        let winter = currentTemp <= 4;
        let earlyWinter = currentTemp >=5 && currentTemp < 9;
        let beginWinter = currentTemp >= 9 && currentTemp < 12;
        let fall = currentTemp >= 12 && currentTemp < 17;
        let earlyFall = currentTemp >= 17 && currentTemp < 20;
        let earlySummer = currentTemp >= 20 && currentTemp < 23;
        let beginSummer = currentTemp >= 23 && currentTemp < 28;
        let summer = currentTemp >= 28;

        if(winter) {
            clothes.innerHTML=`
            <li><h1>패딩, 두꺼운 코트, 누빔 옷, 기모, 목도리</h1></li>
            <img src="{%  static  'resources/clothes/winter1.png' %}" style="width:80px; height:80px;">
            <img src="{%  static  'resources/clothes/winter2.png' %}" style="width:80px; height:80px;">
            <img src="{%  static  'resources/clothes/winter3.png' %}" style="width:80px; height:80px;">
            `;
        } else if(earlyWinter) {
            clothes.innerHTML = `
            <li><h1>울코트, 히트텍, 가죽 옷, 기모</h1></li>
            <img src="{%  static  'resources/clothes/earlywinter1.png' %}" style="width:80px; height:80px;">
            <img src="{%  static  'resources/clothes/earlywinter2.png' %}" style="width:80px; height:80px;">
            <img src="{%  static  'resources/clothes/earlywinter3.png' %}" style="width:80px; height:80px;">
            `;
        } else if(beginWinter) {
            clothes.innerHTML = `
            <li><h1>트렌치 코트, 야상, 점프, 스타킹, 기모바지</h1></li>
            <img src="{%  static  'resources/clothes/beginwinter1.png' %}" style="width:80px; height:80px;">
            <img src="{%  static  'resources/clothes/beginwinter2.png' %}" style="width:80px; height:80px;">
            <img src="{%  static  'resources/clothes/beginwinter3.png' %}" style="width:80px; height:80px;">
            `;
        } else if(fall) {
            clothes.innerHTML = `
            <li><h1>자켓, 가디건, 청자켓, 니트, 스타킹, 청바지</h1></li>
            <img src="{%  static  'resources/clothes/fall1.png' %}" style="width:80px; height:80px;">
            <img src="{%  static  'resources/clothes/fall2.png' %}" style="width:80px; height:80px;">
            <img src="{%  static  'resources/clothes/fall3.png' %}" style="width:80px; height:80px;">
            `;
        } else if(earlyFall) {
            clothes.innerHTML = `
            <li><h1>얇은 가디건, 니트, 맨투맨, 후드, 긴바지</h1></li>
            <img src="{%  static  'resources/clothes/earlyfall1.png' %}" style="width:80px; height:80px;">
            <img src="{%  static  'resources/clothes/earlyfall2.png' %}" style="width:80px; height:80px;">
            <img src="{%  static  'resources/clothes/earlyfall3.png' %}" style="width:80px; height:80px;">
            `;
        } else if(earlySummer) {
            clothes.innerHTML = `
            <li><h1>블라우스, 긴팔 티, 면바지, 슬랙스</h1></li>
            <img src="{%  static  'resources/clothes/earlysummer1.png' %}" style="width:80px; height:80px;">
            <img src="{%  static  'resources/clothes/earlysummer2.png' %}" style="width:80px; height:80px;">
            <img src="{%  static  'resources/clothes/earlysummer3.png' %}" style="width:80px; height:80px;">
            `;
        } else if(beginSummer) {
            clothes.innerHTML = `
            <li><h1>반팔, 얇은 셔츠, 반바지, 면바지</h1></li>
            <img src="{%  static  'resources/clothes/beginsummer1.png' %}" style="width:80px; height:80px;">
            <img src="{%  static  'resources/clothes/beginsummer2.png' %}" style="width:80px; height:80px;">
            <img src="{%  static  'resources/clothes/beginsummer3.png' %}" style="width:80px; height:80px;">
            `;
        } else if(summer) {
        clothes.innerHTML = `
            <li><h1>민소매, 반팔, 반바지, 짧은 치마, 린넨 옷</h1></li>
            <img src="{%  static  'resources/clothes/summer1.png' %}" style="width:80px; height:80px;">
            <img src="{%  static  'resources/clothes/summer2.png' %}" style="width:80px; height:80px;">
            <img src="{%  static  'resources/clothes/summer3.png' %}" style="width:80px; height:80px;">
            `;
        }
    }
})