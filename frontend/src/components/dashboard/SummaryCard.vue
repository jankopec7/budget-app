<template>
  <div class="summary-cards">
    <!-- Income -->
    <div class="card summary-card income">
      <div class="card-icon">💰</div>
      <div class="card-content">
        <h3>Total Income (Month)</h3>
        <div class="amount positive">${{ totalIncome.toFixed(2) }}</div>
        <small :class="changeClass(incomeChange)">
          {{ formatChange(incomeChange) }} from last month
        </small>
      </div>
    </div>

    <!-- Expenses -->
    <div class="card summary-card expense">
      <div class="card-icon">💸</div>
      <div class="card-content">
        <h3>Total Expenses (Month)</h3>
        <div class="amount negative">${{ totalExpenses.toFixed(2) }}</div>
        <small :class="changeClass(expensesChange)">
          {{ formatChange(expensesChange) }} from last month
        </small>
      </div>
    </div>

    <!-- Net Balance -->
    <div class="card summary-card balance">
      <div class="card-icon">📊</div>
      <div class="card-content">
        <h3>Net Balance (Month)</h3>
        <div class="amount" :class="netBalance >= 0 ? 'positive' : 'negative'">
          ${{ netBalance.toFixed(2) }}
        </div>
        <small :class="changeClass(netChange)">
          {{ formatChange(netChange) }} from last month
        </small>
      </div>
    </div>
  </div>
</template>

<script setup>
const props = defineProps({
  totalIncome: Number,
  totalExpenses: Number,
  netBalance: Number,
  incomeChange: Number,
  expensesChange: Number,
  netChange: Number
})

function formatChange(value) {
  const rounded = Math.abs(value).toFixed(1)
  return value > 0 ? `+${rounded}%` : `-${rounded}%`
}

function changeClass(value) {
  return value >= 0 ? 'positive' : 'negative'
}
</script>
