<template>
  <div>
    <h2>Logowanie</h2>
    <form @submit.prevent="login">
      <input v-model="username" placeholder="Login" required />
      <input v-model="password" type="password" placeholder="Hasło" required />
      <button type="submit">Zaloguj</button>
    </form>
    <p>{{ message }}</p>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import axios from 'axios'

const username = ref('')
const password = ref('')
const message = ref('')

const login = async () => {
  try {
    const res = await axios.post('/api/login', {
      username: username.value,
      password: password.value
    })
    message.value = 'Zalogowano!'
    localStorage.setItem('token', res.data.access_token)
  } catch (err) {
    message.value = err.response?.data?.msg || 'Błąd logowania'
  }
}
</script>

