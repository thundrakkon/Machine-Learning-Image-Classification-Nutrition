var url = "result.json"
console.log(url)

d3.json("result.json").then((data) => {
    console.log(data)

    var FruitName = data.foods[0].description
    console.log(FruitName)

    var proteinName = data.foods[0].foodNutrients[0].nutrientName
    console.log(proteinName)

    var proteinValue = data.foods[0].foodNutrients[0].nutrientNumber
    console.log(proteinValue)
})