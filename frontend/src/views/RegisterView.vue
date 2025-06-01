<template>
  <div class="auth-container">
    <div class="auth-card">
      <span class="material-icons icon">person_add</span>
      <h2>Create an Account</h2>
      <p>Join Fintracker and start managing your finances smartly.</p>

      <form @submit.prevent="handleRegister">
        <input type="email" placeholder="Email" v-model="email" required />
        <input type="password" placeholder="Password" v-model="password" required />
        <button class="primary" type="submit">Register</button>
      </form>

      <p class="bottom-text">
        Already have an account?
        <router-link to="/login">Login here</router-link>
      </p>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'

const email = ref('')
const password = ref('')
const router = useRouter()

async function handleRegister() {
  try {
    const res = await fetch('/api/register', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ email: email.value, password: password.value })
    })

    const data = await res.json()
    if (!res.ok) return alert(data.msg || 'Registration failed')

    // Automatyczne logowanie po rejestracji
    const loginRes = await fetch('/api/login', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ email: email.value, password: password.value })
    })

    const loginData = await loginRes.json()
    if (loginRes.ok) {
      localStorage.setItem('token', loginData.access_token)
      localStorage.setItem('user', JSON.stringify({ email: email.value }))
      router.push('/dashboard')
    } else {
      router.push('/login')
    }
  } catch (err) {
    console.error(err)
    alert('Unexpected error during registration.')
  }
}
</script>
