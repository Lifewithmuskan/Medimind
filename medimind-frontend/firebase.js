// Import needed Firebase functions
import { initializeApp } from "https://www.gstatic.com/firebasejs/11.6.0/firebase-app.js";
import { getFirestore } from "https://www.gstatic.com/firebasejs/11.6.0/firebase-firestore.js";
import { getAuth, signInAnonymously, onAuthStateChanged } from "https://www.gstatic.com/firebasejs/11.6.0/firebase-auth.js";

// Your Firebase config
const firebaseConfig = {
  apiKey: "AIzaSyAiS7xSF0eka4980xvlR0iFl5xPOSTLFZo",
  authDomain: "medimind-8911a.firebaseapp.com",
  projectId: "medimind-8911a",
  storageBucket: "medimind-8911a.appspot.com",
  messagingSenderId: "1041027715710",
  appId: "1:1041027715710:web:2f82c0b3e8b55a68163e2f",
  measurementId: "G-DJYHC7ENCC"
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);
const db = getFirestore(app);
const auth = getAuth(app);

// Auto sign-in anonymously
signInAnonymously(auth).catch((error) => {
  console.error("Anonymous Sign-in Failed", error);
});

onAuthStateChanged(auth, (user) => {
  if (user) {
    console.log("Signed in as:", user.uid);
  } else {
    console.log("User signed out.");
  }
});
console.log("Firebase initialized");

export { db, auth };
