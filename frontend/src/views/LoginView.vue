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
import { ref } from 'vue'
import { useRouter } from 'vue-router'

const router = useRouter()
const email = ref('')
const password = ref('')

async function handleLogin() {
  try {
    const res = await fetch('/api/login', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ email: email.value, password: password.value })
    })

    const data = await res.json()

    if (res.ok && data.access_token) {
      localStorage.setItem('token', data.access_token)
      localStorage.setItem('user', JSON.stringify({ email: email.value }))
      router.push('/dashboard')
    } else {
      alert(data.msg || 'Login failed')
    }
  } catch (error) {
    console.error('Login error:', error)
    alert('Unexpected error during login.')
  }
}
</script>

