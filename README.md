Python Programming 101

Practical exercises:

1. Even or Odd?
Write a program that reads an integer from the user. Then your program should
display a message indicating whether the integer is even or odd. 

2. Avoiding Duplicates
In this exercise, you will create a program that reads words from the user until the user enters a blank line. After the user enters a blank line your program should dis- play each word entered by the user exactly once. The words should be displayed in the same order that they were entered. For example, if the user enters:

first
second
first
third
second

then your program should display:
first
second
third

3. Is a String a Palindrome?
A string is a palindrome if it is identical forward and backward. For example “anna”, “civic”, “level” and “hannah” are all examples of palindromic words. Write a program that reads a string from the user and uses a loop to determines whether or not it is a palindrome. Display the result, including a meaningful output message.

4. Caesar Cipher
One of the first known examples of encryption was used by Julius Caesar. Caesar needed to provide written instructions to his generals, but he didn’t want his enemies to learn his plans if the message slipped into their hands. As result, he developed what later became known as the Caesar Cipher.
The idea behind this cipher is simple (and as a result, it provides no protection against modern code breaking techniques). Each letter in the original message is shifted by 3 places. As a result, A becomes D, B becomes E, C becomes F, D becomes G, etc. The last three letters in the alphabet are wrapped around to the beginning: X becomes A, Y becomes B and Z becomes C. Non-letter characters are not modified by the cipher.
Write a program that implements a Caesar cipher. Allow the user to supply the message and the shift amount, and then display the shifted message. Ensure that your program encodes both uppercase and lowercase letters. Your program should also support negative shift values so that it can be used both to encode messages and decode messages.

5.  Multiple Word Palindromes
There are numerous phrases that are palindromes when spacing is ignored. Examples include “go dog”, “flee to me remote elf” and “some men interpret nine memos”, among many others. Extend your solution to Exercise 3 so that it ignores spacing while determining whether or not a string is a palindrome. For an additional challenge, extend your solution so that is also ignores punctuation marks and treats uppercase and lowercase letters as equivalent.





