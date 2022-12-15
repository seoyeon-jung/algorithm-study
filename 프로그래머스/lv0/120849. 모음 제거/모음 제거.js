function solution(my_string) {
   const str = ['a', 'e', 'i', 'o', 'u']
   
   return [...my_string].filter(al => !(str.includes(al))).join('')
}