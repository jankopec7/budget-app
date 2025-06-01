<template>
  <div class="card chart-card">
    <h3>📈 Monthly Overview</h3>
    <p>Comparison of income and expenses over time.</p>
    <div class="chart-placeholder">
      <div class="chart-bars">
        <div class="bar-group" v-for="month in data" :key="month.month">
          <div class="bar income" :style="{ height: month.income / 50 + 'px' }"></div>
          <div class="bar expense" :style="{ height: month.expenses / 50 + 'px' }"></div>
          <span class="bar-label">{{ month.month }}</span>
        </div>
      </div>
      <div class="chart-legend">
        <span class="legend-item">
          <span class="legend-color income"></span> Income
        </span>
        <span class="legend-item">
          <span class="legend-color expense"></span> Expenses
        </span>
      </div>
    </div>
  </div>
</template>

<script setup>
const props = defineProps({
  data: Array
})
</script>
