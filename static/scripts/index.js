function getData() {

    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
        document.getElementById("receivedData").innerHTML =this.responseText;
        }
    };
    xhttp.open("GET", "https://AyuSharma-dev.github.io/ThanksGiving/static/data/index.json", true);
    xhttp.send();

}