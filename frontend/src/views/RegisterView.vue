<template>
  <div>
    <h2>Rejestracja</h2>
    <form @submit.prevent="register">
      <input v-model="username" placeholder="Login" required />
      <input v-model="password" type="password" placeholder="Hasło" required />
      <button type="submit">Zarejestruj</button>
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

const register = async () => {
  try {
    const res = await axios.post('/api/register', {
      username: username.value,
      password: password.value
    })
    message.value = res.data.msg
  } catch (err) {
    message.value = err.response?.data?.msg || 'Błąd rejestracji'
  }
}
</script>
