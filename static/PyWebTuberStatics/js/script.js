function updateTime() {
    var currentTime = new Date();
    var hours = currentTime.getHours();
    var minutes = currentTime.getMinutes();
    var seconds = currentTime.getSeconds();

    hours = (hours < 10 ? "0" : "") + hours;
    minutes = (minutes < 10 ? "0" : "") + minutes;
    seconds = (seconds < 10 ? "0" : "") + seconds;

    document.getElementById("current-time").innerHTML = hours + " : " + minutes + " : " + seconds;
}

function updateDate() {
    var currentDate = new Date();
    var daysOfWeek = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'];
    var months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'];
  
    var dayOfWeek = daysOfWeek[currentDate.getDay()];
    var month = months[currentDate.getMonth()];
    var day = currentDate.getDate();
    var year = currentDate.getFullYear();
  
    document.getElementById("current-date").innerHTML = dayOfWeek + ', ' + month + ' ' + day + ', ' + year;
  }
  

setInterval(updateTime, 10);
setInterval(updateDate, 10);

// Powered by PouyaLj