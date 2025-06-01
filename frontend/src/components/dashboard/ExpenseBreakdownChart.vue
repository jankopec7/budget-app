<template>
  <div class="card chart-card">
    <h3>🥧 Expense Breakdown</h3>
    <p>How your expenses are distributed across categories.</p>
    <div class="chart-placeholder">
      <div class="pie-chart" :style="{ background: pieChartGradient }"></div>
      <div class="chart-legend">
        <span
          class="legend-item"
          v-for="category in categories"
          :key="category.name"
        >
          <span class="legend-color" :style="{ backgroundColor: category.color }"></span>
          {{ category.name }}
        </span>
      </div>
    </div>
  </div>
</template>

<script setup>
import { computed } from 'vue'

const props = defineProps({
  categories: {
    type: Array,
    required: true
  }
})

const pieChartGradient = computed(() => {
  let currentDegree = 0
  return `conic-gradient(${props.categories
    .map(cat => {
      const start = currentDegree
      const end = start + cat.percentage * 3.6
      currentDegree = end
      return `${cat.color} ${start}deg ${end}deg`
    })
    .join(', ')})`
})
</script>

