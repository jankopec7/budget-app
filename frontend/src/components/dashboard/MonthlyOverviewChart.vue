<template>
  <div class="card chart-card placeholder">
    <h3>📈 Monthly Overview</h3>
    <p>Comparison of income and expenses over time.</p>

    <div class="coming-soon">
      <div class="icon">🚧</div>
      <p>This feature is coming soon.</p>
      <small>Monthly income and expense trends will be visualized here in the near future.</small>
    </div>
  </div>
</template>

<script setup>
</script>

<style scoped>
.placeholder {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  height: 280px;
  text-align: center;
  background-color: #f1faee;
  border: 2px dashed #a8dadc;
  border-radius: 12px;
  color: #1d3557;
  padding: 2rem;
  box-shadow: 0 4px 12px rgba(0, 64, 0, 0.05);
}

.coming-soon .icon {
  font-size: 3rem;
  margin-bottom: 1rem;
}

.coming-soon p {
  font-size: 1.1rem;
  font-weight: 600;
  margin-bottom: 0.5rem;
}

.coming-soon small {
  font-size: 0.9rem;
  color: #457b9d;
}
</style>
