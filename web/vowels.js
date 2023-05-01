// Function to validate input (checks if it contains only letters and spaces)
function validateInput(input) {
    return /^[a-zA-Z\s]*$/.test(input);
}

// Function to process input (replace vowels, count length, consonants, vowels, and spaces)
function processInput(input) {
    const vowelOrder = {'a': '1', 'e': '5', 'i': '9', 'o': '15', 'u': '21'};
    const replacedString = input.split('').map(char => vowelOrder[char.toLowerCase()] || char).join('');
    const length = input.length;
    const consonantCount = input.match(/[^aeiou\s]/gi)?.length || 0;
    const vowelCount = input.match(/[aeiou]/gi)?.length || 0;
    const spaceCount = input.match(/\s/g)?.length || 0;

    return {replacedString, length, consonantCount, vowelCount, spaceCount};
}

// Function to handle the submit button click
function handleSubmit() {
    const userInput = document.getElementById("userInput").value;
    if (validateInput(userInput)) {
        const result = processInput(userInput);
        document.getElementById("result").innerHTML = `
            <b>Replaced string: ${result.replacedString}</b><br>
            Length: ${result.length}<br>
            Consonant count: ${result.consonantCount}<br>
            Vowel count: ${result.vowelCount}<br>
            Space count: ${result.spaceCount}<br>
        `;
    } else {
        alert("Invalid input. Please enter a string containing only letters and spaces.");
    }
}

// Function to clear the input field and output
function handleClear() {
    document.getElementById("userInput").value = '';
    document.getElementById("result").innerText = '';
}