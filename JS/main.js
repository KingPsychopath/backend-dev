/*for (let i = 0; i <= 100; i++) {
    if (i % 3 === 0 && i % 5 === 0) {
        console.log('fizzbuzz')
    }

    if (i % 3 === 0) {
        console.log('fizz')
    }

    if (i % 5 === 0) {
        console.log('buzz')
    }
}*/

const promise = new Promise((resolve, reject) => {
    setTimeout(() => {
      if (getRandomBool()) {
        resolve("resolved!")
      } else {
        reject("rejected!")
      }
    }, 1000)
  })
  
  function getRandomBool(){
    return Math.random() < .5
  }

promise.then(message => console.log(message)).catch(message => console.log(message))

function calculateTotalIncrease() {
  const initialIncrease = 0.15; // 15 percent increase
  const finalIncrease = 0.15; // another 15 percent increase

  // Let's assume the original price is 100 for simplicity
  const originalPrice = 100;

  const newPrice = originalPrice * (1 + initialIncrease);
  const finalPrice = newPrice * (1 + finalIncrease);

  const totalIncrease = (finalPrice - originalPrice) / originalPrice;

  return totalIncrease * 100; // Convert to percentage
}

console.log(calculateTotalIncrease());