// This script handles the user's input & sends it to the backend.
// It uses OpenAI's GPT-3 to generate a response & also handles Googgle authentication

import bot from 'images/bot.svg'
import user from 'images/user.svg'


const form = document.querySelector('form')
const chatContainer = document.querySelector('#chat_container')

let loadInterval

function loader(element) {
    // Display loading indicator while the bot is generating a response
    element.textContent = ''

    loadInterval = setInterval(() => {
        // Update the text content of the loading indicator
        element.textContent += '.';

        // If the loading indicator has reached three dots, reset it
        if (element.textContent === '....') {
            element.textContent = '';
        }
    }, 300);
}

function typeText(element, text) {
    // Type bot's response letter by letter in the chat container
    let index = 0

    let interval = setInterval(() => {
        if (index < text.length) {
            element.innerHTML += text.charAt(index)
            index++
        } else {
            clearInterval(interval)
        }
    }, 20)
}

// generate unique ID for each message div of bot
// necessary for typing text effect for that specific reply
// without unique ID, typing text will work on every element
function generateUniqueId() {
    const timestamp = Date.now();
    const randomNumber = Math.random();
    const hexadecimalString = randomNumber.toString(16);

    return `id-${timestamp}-${hexadecimalString}`;
}

function chatStripe(isAi, value, uniqueId) {
    // Creates the HTML structure for each chat message
    return (
        `
        <div class="wrapper ${isAi && 'ai'}">
            <div class="chat">
                <div class="profile">
                    <img 
                      src=${isAi ? bot : user} 
                      alt="${isAi ? 'bot' : 'user'}" 
                    />
                </div>
                <div class="message" id=${uniqueId}>${value}</div>
            </div>
        </div>
    `
    )
}

const handleSubmit = async (e) => {
    // Handles form submission event
    e.preventDefault()

    const data = new FormData(form)

    // user's chatstripe
    chatContainer.innerHTML += chatStripe(false, data.get('prompt'))

    // to clear the textarea input 
    form.reset()

    // bot's chatstripe
    const uniqueId = generateUniqueId()
    chatContainer.innerHTML += chatStripe(true, " ", uniqueId)

    // to focus scroll to the bottom 
    chatContainer.scrollTop = chatContainer.scrollHeight;

    // specific message div 
    const messageDiv = document.getElementById(uniqueId)

    // messageDiv.innerHTML = "..."
    loader(messageDiv)

    const response = await fetch('http://localhost:5000/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            prompt: data.get('prompt')
        })
    })

    clearInterval(loadInterval)
    messageDiv.innerHTML = " "

    if (response.ok) {
        const data = await response.json();
        const parsedData = data.bot.trim() // trims any trailing spaces/'\n' 

        typeText(messageDiv, parsedData)
    } else {
        const err = await response.text()

        messageDiv.innerHTML = "Something went wrong"
        alert(err)
    }
}

form.addEventListener('submit', handleSubmit)
form.addEventListener('keyup', (e) => {
    if (e.keyCode === 13) {
        handleSubmit(e)
    }
})

/*
// Google authentication
function onSignIn(googleUser) {
    const id_token = googleUser.getAuthResponse().id_token;
    const xhr = new XMLHttpRequest();
    xhr.open('POST', '/google_login');
    xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
    xhr.onload = function() {
      console.log(xhr.responseText);
    };
    xhr.send('id_token=' + id_token);
  }
  
  // Function to handle logging out
  function handleLogout() {
    const xhr = new XMLHttpRequest();
    xhr.open('POST', '/logout');
    xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
    xhr.onload = function() {
      console.log(xhr.responseText);
      location.reload();
    };
    xhr.send();
  }
  */
 