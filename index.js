/*const firebaseConfig = {
    apiKey: "AIzaSyBZhR1Jn2KVMqM_gZoyWFLkm3kJ2CIQV-E",
    authDomain: "alumniform-d45ca.firebaseapp.com",
    databaseURL: "https://alumniform-d45ca-default-rtdb.firebaseio.com",
    projectId: "alumniform-d45ca",
    storageBucket: "alumniform-d45ca.firebasestorage.app",
    messagingSenderId: "986427614878",
    appId: "1:986427614878:web:b6d9b8ef40d86c7e62bd8f",
    measurementId: "G-9FEWLSZ8TL"
  };
  //initialize firebase
  firebase.initializeApp(firebaseconfig);

  //refrence your database
  var alumniformDB = firebase.database().ref('alumniform');

document.getElementById('alumniform').addEventListener('submit', submitform);

function submitform(e){
    e.preventDefault();

    var name = getElementVal('username');
    var password = getElementVal('password');

    saveMessages(name,password);

}

const saveMessages = (name, password) =>{
   var newAlumniform = AlumniformDB.push();
   newAlumniform.set({
    name : name,
    password : password,
   })
};

const getElementVal = (id) =>{
    return document.getElementById(id).value;
};




*/

const firebaseConfig = {
    apiKey: "AIzaSyBZhR1Jn2KVMqM_gZoyWFLkm3kJ2CIQV-E",
    authDomain: "alumniform-d45ca.firebaseapp.com",
    databaseURL: "https://alumniform-d45ca-default-rtdb.firebaseio.com",
    projectId: "alumniform-d45ca",
    storageBucket: "alumniform-d45ca.appspot.com",
    messagingSenderId: "986427614878",
    appId: "1:986427614878:web:b6d9b8ef40d86c7e62bd8f",
    measurementId: "G-9FEWLSZ8TL"
};

// Initialize Firebase
firebase.initializeApp(firebaseConfig);

// Reference your database
var alumniformDB = firebase.database().ref("alumniform");

document.getElementById("alumniform").addEventListener("submit", submitform);

function submitform(e) {
    e.preventDefault();

    var name = getElementVal("username");
    var password = getElementVal("password");

    saveMessages(name, password);
}

// Function to save messages to Firebase
const saveMessages = (name, password) => {
    var newAlumniform = alumniformDB.push();
    newAlumniform.set({
        name: name,
        password: password
    }).then(() => {
        console.log("Data saved successfully!");
        alert("Login details saved successfully!");
        window.location.href = "home.html"; 
    }).catch((error) => {
        console.error("Error saving data: ", error);
        alert("Error saving data! Check console.");
    });
};

// Function to get values from input fields
const getElementVal = (id) => {
    return document.getElementById(id).value;
};






