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

<script>
export default {
  data() {
    return {
      email: '',
      password: ''
    };
  },
  methods: {
    handleRegister() {
      // tu możesz dodać faktyczną logikę rejestracji
      console.log('Register:', this.email, this.password);
      alert('Account created successfully!');
      this.$router.push('/login');
    }
  }
};
</script>
