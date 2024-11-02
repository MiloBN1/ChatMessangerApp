<script setup lang="ts">
import axios from 'axios';
import { ref } from 'vue';

let username = ref('')
let password = ref('')

const login = async () => {
  try {
    const response = await axios.post('http://localhost:8000/auth/login/', {
      username: username.value,
      password: password.value,
    });
    console.log(response.data); // Handle successful response
    getData()
  } catch (error) {
    console.error('Login failed:', error); // Handle errors
  }
};

function getData() {
  axios.get('http://localhost:8000/account/whoami/')
    .then((res) => {
      console.log(res.data);  // Log the response from whoami
    })
    .catch((error) => {
      console.error('Failed to fetch whoami:', error);
    });
}

// Define the handleSubmit function
const handleSubmit = () => {
  login(); // Call the login function when the form is submitted
};
</script>
<template>
  <div class="login-container">
    <h1>Welcome Back!</h1>
    <form @submit.prevent="handleSubmit">
      <div class="form-group">
        <label for="username">Username</label>
        <input type="text" id="username" v-model="username" required />
      </div>
      <div class="form-group">
        <label for="password">Password</label>
        <input type="password" id="password" v-model="password" required />
      </div>
      <button class="login-button" @click="handleSubmit()">Log In</button>
      <div class="links">
        <router-link to="/forgot-password">Forgot Password?</router-link>
        <router-link to="/register">Create an Account</router-link>
      </div>
    </form>
  </div>
</template>


<style scoped>
.login-container {
  max-width: 400px;
  margin: 50px auto;
  padding: 20px;
  border-radius: 8px;
  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.1);
  background-color: #fff;
  text-align: center;
}

h1 {
  margin-bottom: 20px;
  color: #333;
}

.form-group {
  margin-bottom: 15px;
  text-align: left;
}

label {
  display: block;
  margin-bottom: 5px;
  color: #666;
}

input {
  width: 100%;
  padding: 10px;
  border: 1px solid #ddd;
  border-radius: 4px;
  font-size: 16px;
}

input:focus {
  border-color: #007bff;
  outline: none;
}

.login-button {
  width: 100%;
  padding: 10px;
  border: none;
  border-radius: 4px;
  background-color: #007bff;
  color: white;
  font-size: 16px;
  cursor: pointer;
  transition: background-color 0.3s ease;
}

.login-button:hover {
  background-color: #0056b3;
}

.links {
  margin-top: 10px;
}

.links a {
  color: #007bff;
  text-decoration: none;
}

.links a:hover {
  text-decoration: underline;
}
</style>
