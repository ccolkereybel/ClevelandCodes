

import List from "./List.jsx";

function App() {

  const fruits = []

  const vegetables = [{id: 4, name: "carrot", calories: 10}, 
                      {id: 5, name: "tomato", calories: 50},
                      {id: 6, name: "squash", calories: 100}]
               


  return (
    <>
  {fruits.length > 0 ?  <List items={fruits} category="Fruits"/> : null}
  <List items={vegetables} category="Vegetables"/>
    </>
  );
}

export default App;
