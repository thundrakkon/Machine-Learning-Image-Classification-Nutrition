var url = "./result.json"

d3.json(url).then((jsonData) => {
    console.log(jsonData)
  
    var FruitName = jsonData.foods[0].description
    console.log(FruitName)

    var proteinName = jsonData.foods[0].foodNutrients[0].nutrientName
    console.log(proteinName)

    var proteinValue = jsonData.foods[0].foodNutrients[0].nutrientNumber
    console.log(proteinValue)
})