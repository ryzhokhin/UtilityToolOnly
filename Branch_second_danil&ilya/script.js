let Zinli = false;
let Wise = false;
let AdvCash = false;
let ABA = false;
let Zelle = false;
let Utopia = false;
let AirTM = false;
let Perfect_Money = false;
let Payeer = false;



function changing_color_by_id( element_id, clicked_or_not){
    if(clicked_or_not){
        document.getElementById(element_id).style.backgroundColor = "#d9d9d9";
        clicked_or_not = !clicked_or_not;
        return clicked_or_not;
    }
        document.getElementById(element_id).style.backgroundColor = "#a7c0db";
        clicked_or_not = !clicked_or_not;
        return clicked_or_not;
}

function test_1(){
    Zinli = changing_color_by_id("Zinli", Zinli);
    console.log(Zinli);
}
function test_2(){
    Wise = changing_color_by_id("Wise", Wise);
    console.log(Wise);
}
function test_3(){
    AdvCash = changing_color_by_id("AdvCash", AdvCash);
    console.log(AdvCash);
}
function test_4(){
    ABA = changing_color_by_id("ABA", ABA);
    console.log(ABA);
}
function test_5(){
    Zelle = changing_color_by_id("Zelle", Zelle);
    console.log(Zelle);
}
function test_6(){
    Utopia = changing_color_by_id("Utopia", Utopia);
    console.log(Utopia);
}
function test_7(){
    AirTM = changing_color_by_id("AirTM", AirTM);
    console.log(AirTM);
}
function test_8(){
    Perfect_Money = changing_color_by_id("Perfect Money", Perfect_Money);
    console.log(Perfect_Money);
}
function test_9(){
    Payeer = changing_color_by_id("Payeer", Payeer);
    console.log(Payeer);

    return Payeer;
}

function choosed_currency() {
    var select = document.querySelector('select');
    let currency;
    //console.log(select.value);
    switch (select.value){
        case "1":
            currency = "UAH";
            break;
        case "2":
            currency = "USDT";
            break;
        case "3":
            currency = "Zalupa1";
            break;
        case "4":
            currency = "Zalupa2";
            break;
        case "5":
            currency = "penis";
            break;
        default:
            currency = "default";
    }
    return currency;
}
function on_submit(){
    let budget = document.getElementById("budget").value;
    console.log(budget);
    console.log(choosed_currency());

    let banks =   Zinli+Wise+AdvCash+ABA+Zelle+Utopia+AirTM+Perfect_Money+Payeer;
    console.log(banks);
}




