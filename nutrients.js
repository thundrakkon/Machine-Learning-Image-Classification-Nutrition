// var url = "./result.json"
var url = "./results_details.json"
var csv = "./Daily-Values.csv"

d3.json(url).then((jsonData) => {
    d3.csv(csv).then((daily) => {
        console.log(jsonData)
        console.log(daily)

        var i = 1
        var j = 0
            // Fruit name
        var fruitName = jsonData[i].description
        console.log(fruitName)

        // Portions Data
        var fruitPortDesc = jsonData[i].foodPortions[j].portionDescription
        console.log(fruitPortDesc)
        var fruitPortWeight = jsonData[i].foodPortions[j].gramWeight
        console.log(fruitPortWeight)

        // Protein
        var proteinName = jsonData[i].foodNutrients[0].nutrient.name
        console.log(proteinName)
        var proteinAmt = jsonData[i].foodNutrients[0].amount
        console.log(proteinAmt)
        var proteinUnit = jsonData[i].foodNutrients[0].nutrient.unitName
        console.log(proteinUnit)
        var proteinDVAdult = daily[33].Adults
        console.log(proteinDVAdult)

        // Total lipid (fat)
        var lipfatName = jsonData[i].foodNutrients[1].nutrient.name
        console.log(lipfatName)
        var lipfatAmt = jsonData[i].foodNutrients[1].amount
        console.log(lipfatAmt)
        var lipfatUnit = jsonData[i].foodNutrients[1].nutrient.unitName
        console.log(lipfatUnit)
        var lipfatDVAdult = daily[27].Adults
        console.log(lipfatDVAdult)

        // Carbohydrate, by difference
        var carbName = jsonData[i].foodNutrients[2].nutrient.name
        console.log(carbName)
        var carbAmt = jsonData[i].foodNutrients[2].amount
        console.log(carbAmt)
        var carbUnit = jsonData[i].foodNutrients[2].nutrient.unitName
        console.log(carbUnit)
        var carbDVAdult = daily[30].Adults
        console.log(carbDVAdult)

        // Energy
        var calName = jsonData[i].foodNutrients[3].nutrient.name
        console.log(calName)
        var calAmt = jsonData[i].foodNutrients[3].amount
        console.log(calAmt)
        var calUnit = jsonData[i].foodNutrients[3].nutrient.unitName
        console.log(calUnit)

        // Water
        var waterName = jsonData[i].foodNutrients[5].nutrient.name
        console.log(waterName)
        var waterAmt = jsonData[i].foodNutrients[5].amount
        console.log(waterAmt)
        var waterUnit = jsonData[i].foodNutrients[5].nutrient.unitName
        console.log(waterUnit)
        var waterDVAdult = 0
        console.log(waterDVAdult)

        // Sugars, total including NLEA
        var sugarName = jsonData[i].foodNutrients[8].nutrient.name
        console.log(sugarName)
        var sugarAmt = jsonData[i].foodNutrients[8].amount
        console.log(sugarAmt)
        var sugarUnit = jsonData[i].foodNutrients[8].nutrient.unitName
        console.log(sugarUnit)
        var sugarDVAdult = daily[34].Adults
        console.log(sugarDVAdult)

        // Fiber, total dietary
        var fiberName = jsonData[i].foodNutrients[9].nutrient.name
        console.log(fiberName)
        var fiberAmt = jsonData[i].foodNutrients[9].amount
        console.log(fiberAmt)
        var fiberUnit = jsonData[i].foodNutrients[9].nutrient.unitName
        console.log(fiberUnit)
        var fiberDVAdult = daily[32].Adults
        console.log(fiberDVAdult)

        // Calcium, Ca
        var calciumName = jsonData[i].foodNutrients[10].nutrient.name
        console.log(calciumName)
        var calciumAmt = jsonData[i].foodNutrients[10].amount
        console.log(calciumAmt)
        var calciumUnit = jsonData[i].foodNutrients[10].nutrient.unitName
        console.log(calciumUnit)
        var calciumDVAdult = daily[2].Adults
        console.log(calciumDVAdult)

        // Iron, Fe
        var ironName = jsonData[i].foodNutrients[11].nutrient.name
        console.log(ironName)
        var ironAmt = jsonData[i].foodNutrients[11].amount
        console.log(ironAmt)
        var ironUnit = jsonData[i].foodNutrients[11].nutrient.unitName
        console.log(ironUnit)
        var ironDVAdult = daily[3].Adults
        console.log(ironDVAdult)

        // Magnesium, Mg
        var mgName = jsonData[i].foodNutrients[12].nutrient.name
        console.log(mgName)
        var mgAmt = jsonData[i].foodNutrients[12].amount
        console.log(mgAmt)
        var mgUnit = jsonData[i].foodNutrients[12].nutrient.unitName
        console.log(mgUnit)
        var mgDVAdult = daily[17].Adults
        console.log(mgDVAdult)

        // Phosphorus, P
        var pName = jsonData[i].foodNutrients[13].nutrient.name
        console.log(pName)
        var pAmt = jsonData[i].foodNutrients[13].amount
        console.log(pAmt)
        var pUnit = jsonData[i].foodNutrients[13].nutrient.unitName
        console.log(pUnit)
        var pDVAdult = daily[15].Adults
        console.log(pDVAdult)

        // Potassium, K
        var kName = jsonData[i].foodNutrients[14].nutrient.name
        console.log(kName)
        var kAmt = jsonData[i].foodNutrients[14].amount
        console.log(kAmt)
        var kUnit = jsonData[i].foodNutrients[14].nutrient.unitName
        console.log(kUnit)
        var kDVAdult = daily[25].Adults
        console.log(kDVAdult)

        // Sodium, Na
        var naName = jsonData[i].foodNutrients[15].nutrient.name
        console.log(naName)
        var naAmt = jsonData[i].foodNutrients[15].amount
        console.log(naAmt)
        var naUnit = jsonData[i].foodNutrients[15].nutrient.unitName
        console.log(naUnit)
        var naDVAdult = daily[31].Adults
        console.log(naDVAdult)

        // Zinc, Zn
        var znName = jsonData[i].foodNutrients[16].nutrient.name
        console.log(znName)
        var znAmt = jsonData[i].foodNutrients[16].amount
        console.log(znAmt)
        var znUnit = jsonData[i].foodNutrients[16].nutrient.unitName
        console.log(znUnit)
        var znDVAdult = daily[18].Adults
        console.log(znDVAdult)

        // Copper, Cu
        var cuName = jsonData[i].foodNutrients[17].nutrient.name
        console.log(cuName)
        var cuAmt = jsonData[i].foodNutrients[17].amount
        console.log(cuAmt)
        var cuUnit = jsonData[i].foodNutrients[17].nutrient.unitName
        console.log(cuUnit)
        var cuDVAdult = daily[20].Adults
        console.log(cuDVAdult)

        // Vitamin A, RAE
        var vitAName = jsonData[i].foodNutrients[20].nutrient.name
        console.log(vitAName)
        var vitAAmt = jsonData[i].foodNutrients[20].amount
        console.log(vitAAmt)
        var vitAUnit = jsonData[i].foodNutrients[20].nutrient.unitName
        console.log(vitAUnit)
        var vitAVAdult = daily[0].Adults
        console.log(vitAVAdult)

        // Carotene, beta
        var bcName = jsonData[i].foodNutrients[21].nutrient.name
        console.log(bcName)
        var bcAmt = jsonData[i].foodNutrients[21].amount
        console.log(bcAmt)
        var bcUnit = jsonData[i].foodNutrients[21].nutrient.unitName
        console.log(bcUnit)
        var bcDVAdult = 0
        console.log(bcDVAdult)

        // Vitamin E (alpha-tocopherol)
        var vitEName = jsonData[i].foodNutrients[23].nutrient.name
        console.log(vitEName)
        var vitEAmt = jsonData[i].foodNutrients[23].amount
        console.log(vitEAmt)
        var vitEUnit = jsonData[i].foodNutrients[23].nutrient.unitName
        console.log(vitEUnit)
        var vitEDVAdult = daily[5].Adults
        console.log(vitEDVAdult)

        // Vitamin D (D2 + D3)
        var vitDName = jsonData[i].foodNutrients[24].nutrient.name
        console.log(vitDName)
        var vitDAmt = jsonData[i].foodNutrients[24].amount
        console.log(vitDAmt)
        var vitDUnit = jsonData[i].foodNutrients[24].nutrient.unitName
        console.log(vitDUnit)
        var vitDDVAdult = daily[4].Adults
        console.log(vitDDVAdult)

        // Vitamin C, total ascorbic acid
        var vitCName = jsonData[i].foodNutrients[28].nutrient.name
        console.log(vitCName)
        var vitCAmt = jsonData[i].foodNutrients[28].amount
        console.log(vitCAmt)
        var vitCUnit = jsonData[i].foodNutrients[28].nutrient.unitName
        console.log(vitCUnit)
        var vitCDVAdult = daily[1].Adults
        console.log(vitCDVAdult)

        // Thiamin
        var thiaminName = jsonData[i].foodNutrients[29].nutrient.name
        console.log(thiaminName)
        var thiaminAmt = jsonData[i].foodNutrients[29].amount
        console.log(thiaminAmt)
        var thiaminUnit = jsonData[i].foodNutrients[29].nutrient.unitName
        console.log(thiaminUnit)
        var thiaminDVAdult = daily[7].Adults
        console.log(thiaminDVAdult)

        // Riboflavin
        var riboName = jsonData[i].foodNutrients[30].nutrient.name
        console.log(riboName)
        var riboAmt = jsonData[i].foodNutrients[30].amount
        console.log(riboAmt)
        var riboUnit = jsonData[i].foodNutrients[30].nutrient.unitName
        console.log(riboUnit)
        var riboDVAdult = daily[8].Adults
        console.log(riboDVAdult)

        // Niacin
        var niacinName = jsonData[i].foodNutrients[31].nutrient.name
        console.log(niacinName)
        var niacinAmt = jsonData[i].foodNutrients[31].amount
        console.log(niacinAmt)
        var niacinUnit = jsonData[i].foodNutrients[31].nutrient.unitName
        console.log(niacinUnit)
        var niacinDVAdult = daily[9].Adults
        console.log(niacinDVAdult)

        // Vitamin B-6
        var vitBName = jsonData[i].foodNutrients[32].nutrient.name
        console.log(vitBName)
        var vitBAmt = jsonData[i].foodNutrients[32].amount
        console.log(vitBAmt)
        var vitBUnit = jsonData[i].foodNutrients[32].nutrient.unitName
        console.log(vitBUnit)
        var vitBDVAdult = daily[10].Adults
        console.log(vitBDVAdult)

        // Cholesterol
        var cholName = jsonData[i].foodNutrients[42].nutrient.name
        console.log(cholName)
        var cholAmt = jsonData[i].foodNutrients[42].amount
        console.log(cholAmt)
        var cholUnit = jsonData[i].foodNutrients[42].nutrient.unitName
        console.log(cholUnit)
        var cholDVAdult = daily[29].Adults
        console.log(cholDVAdult)

        // Fatty acids, total saturated
        var satfatName = jsonData[i].foodNutrients[43].nutrient.name
        console.log(satfatName)
        var satfatAmt = jsonData[i].foodNutrients[43].amount
        console.log(satfatAmt)
        var satfatUnit = jsonData[i].foodNutrients[43].nutrient.unitName
        console.log(satfatUnit)
        var satfatDVAdult = daily[28].Adults
        console.log(satfatDVAdult)

        // Fatty acids, total monounsaturated
        var monofatName = jsonData[i].foodNutrients[63].nutrient.name
        console.log(monofatName)
        var monofatAmt = jsonData[i].foodNutrients[63].amount
        console.log(monofatAmt)
        var monofatUnit = jsonData[i].foodNutrients[63].nutrient.unitName
        console.log(monofatUnit)
        var monofatDVAdult = 0
        console.log(monofatDVAdult)

        // Fatty acids, total polyunsaturated
        var polyfatName = jsonData[i].foodNutrients[64].nutrient.name
        console.log(polyfatName)
        var polyfatAmt = jsonData[i].foodNutrients[64].amount
        console.log(polyfatAmt)
        var polyfatUnit = jsonData[i].foodNutrients[64].nutrient.unitName
        console.log(polyfatUnit)
        var polyfatDVAdult = 0
        console.log(polyfatDVAdult)


        // % Daily Value

    })
})