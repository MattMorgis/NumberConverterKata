//- Courtesy of James Grenning (@jwgrenning) and Jeff Langr (@jlangr)
//- Use this to learn TDD

const toWords = (number) => {
  let result = convertNumberToWords(number);
  
    if (result) {
      return result;
    }
  
    const digits = numberOfDigits(number);
  
    switch (digits) {
      case 2: 
        return getTwoDigitNumberText(number);
      case 3: 
        return getThreeDigitNumberText(number);
      case 4: 
        return getFourFiveOrSixDigitNumberText(number);
      case 5: 
        return getFourFiveOrSixDigitNumberText(number);
      case 6: 
        return getFourFiveOrSixDigitNumberText(number);
      case 7: 
        return 'one million';
    }
  };
  
  const numberOfDigits = (number) => {
    return number.toString().length;
  }
  
  const getTwoDigitNumberText = (number) => {
    const remainder = number % 10;
    const tens = number - remainder;
  
    return toWords(tens) + '-' + toWords(remainder);
  };
  
  const getThreeDigitNumberText = (number) => {
    const remainder = number % 100;
    const hundreds = number - remainder;
    
    return toWords(hundreds) + ' ' + toWords(remainder);
  }
  
  const getFourFiveOrSixDigitNumberText = (number) => {
    const remainder = number % 1000;
    const thousands = (number - remainder) / 1000;
  
    if (remainder === 0) {
      return toWords(thousands) + ' thousand';
    }
  
    return toWords(thousands) + ' thousand ' + toWords(remainder);
  };
  
  const convertNumberToWords = (number) => {
    return numbers[number];
  }
  
  const numbers = {
    0: 'zero',
    1: 'one',
    2: 'two',
    3: 'three',
    4: 'four',
    5: 'five',
    6: 'six',
    7: 'seven',
    8: 'eight',
    9: 'nine',
    10: 'ten',
    11: 'eleven',
    12: 'twelve',
    13: 'thirteen',
    14: 'fourteen',
    15: 'fifteen',
    16: 'sixteen',
    17: 'seventeen',
    18: 'eighteen',
    19: 'nineteen',
  
    20: 'twenty',
    30: 'thirty',
    40: 'forty',
    50: 'fifty',
    60: 'sixty',
    70: 'seventy',
    80: 'eighty',
    90: 'ninety',
  
    100: "one hundred",
    200: "two hundred",
    300: "three hundred",
    400: "four hundred",
    500: "five hundred",
    600: "six hundred",
    700: "seven hundred",
    800: "eight hundred",
    900: "nine hundred"
  }
  
  module.exports = toWords;