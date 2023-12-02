package main

import (
	"fmt"
	"os"
	"strconv"
	"strings"
	"unicode"
)

func main() {	
	data, err := os.ReadFile("input01.txt")
	if err != nil {
		panic("Cannot read input file")
	}
	lines := strings.Split(string(data), "\n")	
	part1(lines)
	part2(lines)
}	

func part1(lines []string){	
	res := 0
	for _, line := range lines {
		var digits []rune
		for _, digit := range line {
			if unicode.IsDigit(digit) {
				digits = append(digits, digit)				
			}
		}
		sum := string(digits[0]) + string(digits[len(digits)-1])
		invValue, err := strconv.Atoi(sum)
		if err != nil {
			panic("Cannot convert to int")
		}
		res += invValue
	}

	fmt.Println("part1:", res)	
}

func part2( lines []string){
	sum := 0
	for _, line := range lines {	
		sum +=processLine(line)
	}
	fmt.Println("part2:", sum)	
}

func processLine(input string)int {
	// Mapping of number words to their numeric values
	numberWords := map[string]string{
		"zero": "0", "one": "1", "two": "2", "three": "3", "four": "4",
		"five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9",
	}

	output := ""
	i := 0

	for i < len(input) {		
		matched := false
		for word, value := range numberWords {
			if strings.HasPrefix(input[i:], word) {
				output += value
				matched = true
			}
		}	
		if !matched{
			if input[i] >= '0' && input[i] <= '9' {
				output += string(input[i])
				
			}
		}
		i++
	}
	res, err := strconv.Atoi(string(output[0]) + string(output[len(output)-1]))
	if err != nil {	
		panic("Cannot convert to int")	
	}
	return res
}