<template>
  <nav class="dashboard-navbar" :class="{ scrolled: isScrolled }">
    <router-link to="/" class="navbar-brand">FinTracker</router-link>
    <div class="navbar-user">
      <div class="user-info">
        <div class="user-avatar">{{ userInitials }}</div>
        <span>{{ userEmail }}</span>
      </div>
      <button class="logout-btn" @click="$emit('logout')">
        Logout
      </button>
    </div>
  </nav>
</template>

<script setup>
import { ref, onMounted, onUnmounted } from 'vue'

const props = defineProps({
  userEmail: String,
  userInitials: String
})

const isScrolled = ref(false)

const handleScroll = () => {
  isScrolled.value = window.scrollY > 10
}

onMounted(() => {
  window.addEventListener('scroll', handleScroll)
})

onUnmounted(() => {
  window.removeEventListener('scroll', handleScroll)
})
</script>

