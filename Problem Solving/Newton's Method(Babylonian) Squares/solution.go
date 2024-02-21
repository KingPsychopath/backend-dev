package main

import (
	"fmt"
	"math"
)

func Sqrt(n float64) float64 {
	guess := n / 2.0
	delta := 0.00000000001

	for true {
		betterGuess := (guess + n/guess) / 2.0
		if math.Abs(guess-betterGuess) < delta {
			return guess
		}
		guess = betterGuess
	}
	return 0.0
}

func Sqrt2(x float64) float64 {
	z := x / 2 // Initial guess
	delta := 0.0000001
	previousZ := z + delta + 1 // Initialize previousZ to ensure loop runs at least once

	for math.Abs(previousZ-z) > delta {
			previousZ = z
			z -= (z*z - x) / (2 * z)
			//fmt.Println(z)
	}
	return z
}


func main() {
	fmt.Println(Sqrt(2))
	fmt.Println(Sqrt(5))
	fmt.Println(Sqrt(25))
	fmt.Println(Sqrt(36))
	fmt.Println(Sqrt(144))


	fmt.Println(Sqrt2(2))
	fmt.Println(Sqrt2(5))
	fmt.Println(Sqrt2(25))
	fmt.Println(Sqrt2(36))
	fmt.Println(Sqrt2(144))

}
