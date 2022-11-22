function getData() {
    
    $.ajax({
        url: "https://AyuSharma-dev.github.io/ThanksGiving/index.json",
        dataType: "json"
    }).done(function(result){
        console.log(result);
    });

}