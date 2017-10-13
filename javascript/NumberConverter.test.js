//- Courtesy of James Grenning (@jwgrenning) and Jeff Langr (@jlangr)
//- Use this to learn TDD

const toWords = require('./NumberConverter');

test('0', () => {
  expect(toWords(0)).toBe('zero');
});

test('single digit (1 - 9)', () => {
  expect(toWords(1)).toBe('one');
  expect(toWords(9)).toBe('nine');
});

test('double digit under twenty (10 - 19)', () => {
  expect(toWords(10)).toBe('ten');
  expect(toWords(19)).toBe('nineteen');
});

test('multiples of ten (10, 50, 90)', () => {
  expect(toWords(20)).toBe('twenty');
  expect(toWords(90)).toBe('ninety');
});

test('not multiples of ten (21-99)', () => {
  expect(toWords(21)).toBe('twenty-one');
  expect(toWords(55)).toBe('fifty-five');
  expect(toWords(99)).toBe('ninety-nine');
});

test('hundreds (100, 500, 900)', () => {
  expect(toWords(100)).toBe('one hundred');
  expect(toWords(900)).toBe('nine hundred');
});

test('not multiples of one hundred (101-999)', () => {
  expect(toWords(101)).toBe('one hundred one');
  expect(toWords(999)).toBe('nine hundred ninety-nine');
});

test('thousands (1000, 5000, 9000)', () => {
  expect(toWords(1000)).toBe('one thousand');
  expect(toWords(9000)).toBe('nine thousand');
});

test('not even thousands (9999, 9911)', () => {
  expect(toWords(9999)).toBe('nine thousand nine hundred ninety-nine');
  expect(toWords(9911)).toBe('nine thousand nine hundred eleven');
});

test('tens of thousands (10,000, 19,000)', () => {
  expect(toWords(10000)).toBe('ten thousand');
  expect(toWords(19000)).toBe('nineteen thousand');
});

test('tens of thousands and some (19,999)', () => {
  expect(toWords(19999)).toBe('nineteen thousand nine hundred ninety-nine');
});

test('hundred thousand (100,000, 700,000)', () => {
  expect(toWords(100000)).toBe('one hundred thousand');
  expect(toWords(700000)).toBe('seven hundred thousand');
});

test('not exactly hundred thousand (198,000, 701,020)', () => {
  expect(toWords(198000)).toBe('one hundred ninety-eight thousand');
  expect(toWords(701020)).toBe('seven hundred one thousand twenty');
});

test('millions (1,000,000)', () => {
  expect(toWords(1000000)).toBe('one million');
});
