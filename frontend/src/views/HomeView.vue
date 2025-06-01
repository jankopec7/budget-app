<template>
  <div>
    <div class="navbar">
      <div class="logo">Fintracker</div>
      <div class="actions">
        <RouterLink to="/dashboard" class="secondary button-link">Dashboard</RouterLink>
        <RouterLink to="/login" class="secondary button-link">Login</RouterLink>
        <RouterLink to="/register" class="primary button-link">Register</RouterLink>
      </div>
    </div>

    <div class="hero">
      <h1>Welcome to Fintracker</h1>
      <p>
        Track your financial health, manage expenses and income, and visualize your growth — simply and clearly.
      </p>
      <div style="margin-top: 2rem;">
        <RouterLink to="/register" class="primary button-link">Get Started</RouterLink>
        <RouterLink to="/login" class="secondary button-link">Login</RouterLink>
      </div>
    </div>

    <div class="cards">
      <div class="card">
        <h3>📊 Track Everything</h3>
        <p>Log your income and expenses effortlessly. Stay organized and in control of your cash flow.</p>
      </div>
      <div class="card">
        <h3>📈 Visualize Growth</h3>
        <p>See your financial health at a glance with intuitive charts and summaries. Make informed decisions.</p>
      </div>
      <div class="card">
        <h3>🌱 Simple & Fresh</h3>
        <p>A calming, clean interface designed to help you focus on your financial goals with ease.</p>
      </div>
    </div>
  </div>
</template>

<script setup>
</script>
