# combinations_tree_maker

gen.py creates crafting trees for https://www.adamenglish.net/combinations/

requires graphviz to run

requires you to have the json string detailing every combinations to be stored in combinations.json
you can get it by typing the following in the console of a web browser

```js
let request = await fetch("https://eelements.apps.adamenglish.net/statistics/getElements.php");
console.log(await request.text())
```