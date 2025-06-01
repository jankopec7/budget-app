<template>
  <div class="auth-container">
    <div class="auth-card">
      <span class="material-icons icon">login</span>
      <h2>Welcome Back</h2>
      <p>Sign in to your Fintracker account</p>

      <form @submit.prevent="handleLogin">
        <input type="email" placeholder="Email" v-model="email" required />
        <input type="password" placeholder="Password" v-model="password" required />
        <button class="primary" type="submit">Login</button>
      </form>

      <p class="bottom-text">
        Don't have an account?
        <router-link to="/register">Register here</router-link>
      </p>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue';

const email = ref('');
const password = ref('');

function handleLogin() {
  // logika logowania
  console.log('Login attempt:', email.value, password.value);
}
</script>

