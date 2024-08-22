# combinations_tree_maker

gen.py creates crafting trees for https://www.adamenglish.net/combinations/

requires graphviz to run

requires you to have the json string detailing every combination to be stored in combinations.json
type the following in the console of a web browser and copy paste it into combinations.json

```js
let request = await fetch("https://eelements.apps.adamenglish.net/statistics/getElements.php");
console.log(await request.text())
//i could automate this but lazy
```
