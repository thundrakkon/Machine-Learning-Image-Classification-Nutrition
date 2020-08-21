// function scatterChart(data, canvasId, columnX, columnY, columnRad){
//     return "hola"
// }
console.log("heyyyyyyyyyyyyyyyyyy!!!!!!!!!!!!!!");


d3.csv('{{url_for("static", filename="fruits.csv")}}').then(function(data){
    console.log(data);
})