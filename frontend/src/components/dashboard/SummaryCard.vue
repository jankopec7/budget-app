<template>
  <div class="summary-cards">
    <div class="card summary-card income">
      <div class="card-icon">💰</div>
      <div class="card-content">
        <h3>Total Income (Month)</h3>
        <div class="amount positive">${{ totalIncome.toFixed(2) }}</div>
        <small>+12.5% from last month</small>
      </div>
    </div>

    <div class="card summary-card expense">
      <div class="card-icon">💸</div>
      <div class="card-content">
        <h3>Total Expenses (Month)</h3>
        <div class="amount negative">${{ totalExpenses.toFixed(2) }}</div>
        <small>-8.3% from last month</small>
      </div>
    </div>

    <div class="card summary-card balance">
      <div class="card-icon">📊</div>
      <div class="card-content">
        <h3>Net Balance (Month)</h3>
        <div class="amount" :class="netBalance >= 0 ? 'positive' : 'negative'">
          ${{ netBalance.toFixed(2) }}
        </div>
        <small>+4.2% from last month</small>
      </div>
    </div>
  </div>
</template>

<script setup>
defineProps({
  totalIncome: Number,
  totalExpenses: Number,
  netBalance: Number
})
</script>

