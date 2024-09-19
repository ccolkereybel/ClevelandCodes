

import List from "./List.jsx";

function App() {

  const fruits = [{id: 1, name: "apple", calories: 10}, 
                  {id: 2, name: "orange", calories: 50},
                  {id: 3, name: "banana", calories: 100}]


  return (
    <>
  <List items={fruits} category="Fruits"/>
    </>
  );
}

export default App;
