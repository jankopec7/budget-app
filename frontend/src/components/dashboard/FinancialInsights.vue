<template>
  <div class="insights-section">
    <h2>Financial Insights</h2>

    <div class="charts-grid">
      <MonthlyOverviewChart v-if="monthlyData.length" :data="monthlyData" />
      <ExpenseBreakdownChart v-if="expenseCategories.length" :categories="expenseCategories" />
    </div>
  </div>
</template>

<script setup>
import MonthlyOverviewChart from './MonthlyOverviewChart.vue'
import ExpenseBreakdownChart from './ExpenseBreakdownChart.vue'

const props = defineProps({
  monthlyData: {
    type: Array,
    required: true
  },
  expenseCategories: {
    type: Array,
    required: true
  }
})
</script>

