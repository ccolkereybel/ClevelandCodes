import React, {useState} from 'react'

function Counter (){

const [count, setCount] = useState(0)

const increment = () => {
    setCount(count + 1)
    setCount(c => c + 1)
    setCount(c => c + 1)
}

const decrement = () => {
        setCount(count - 1)
}

const reset = () => {
    setCount(0)

}

return(
    <div>
        <p>{count}</p>
        <button onClick = {decrement}>Decrement</button> 
       <button onClick = {increment}>Increment</button> 
       <button onClick = {reset}>Reset</button> 

    </div>
)

}

export default Counter