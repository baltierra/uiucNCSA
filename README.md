# Research Software Engineer: Prescreening Questions
## National Center of Supercomputing Applications (NCSA)
## University of Illinois Urbana-Champaign
#
### **Fabián A. Baltierra**
#
Below you will find the description of the most important files and folders inside this repository
<br>



1. **vowels.py**: This is a functional Python solution that addresses exactly what it was requested in question od the prescreening document.

2. **vowels_extended.py**: This is an extension of the previous code, but this time it allows the user to continue interacting with the program through the terminal by entering their own phrases or words. It implements a simple menu, input validation and also for each word that is processed it is able to create an entry in an external JSON file where it stores the following data: string entered, string length, number of vowels in the string, number of consonants in the string, a timestamp of the last time that string was used and how many times it has been used.

3. **web**: This is a folder with an *index.html* file and a subfolder inside (*src*). This is a web implementation of the point *(ii)* using JavaScript. Inside the *src* folder you can find *vowels.js* and *vowels.css*, which implements the logic and the style, respectively. The idea is the same, the simple web application offers a text field, a submit and a clear button, so the user can enter words or sentences and those are processed in the background and an answer is returned to the web page. In this case there is no JSON file, and the complete answer is displayed on screen.

