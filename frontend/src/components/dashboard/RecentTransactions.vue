<template>
  <div class="card transactions-list">
    <div class="card-header">
      <h2>Recent Transactions</h2>
      <p>A quick overview of your latest financial activities.</p>
    </div>

    <div class="transactions-table" v-if="transactions.length">
      <div class="table-header">
        <span>Date</span>
        <span>Description</span>
        <span>Category</span>
        <span>Type</span>
        <span>Amount</span>
      </div>

      <div class="table-body">
        <div
          v-for="transaction in transactions"
          :key="transaction.id"
          class="table-row"
        >
          <span class="date">{{ formatDate(transaction.date) }}</span>
          <span class="description">{{ transaction.description }}</span>
          <span class="category">{{ transaction.category }}</span>
          <span class="type-badge" :class="transaction.type">
            {{ transaction.type === 'income' ? 'Income' : 'Expense' }}
          </span>
          <span
            class="amount"
            :class="transaction.type === 'income' ? 'positive' : 'negative'"
          >
            {{ transaction.type === 'income' ? '+' : '-' }}${{
              Math.abs(transaction.amount).toFixed(2)
            }}
          </span>
        </div>
      </div>
    </div>

    <div v-else class="no-transactions">
      <p>No recent transactions yet.</p>
    </div>

    <div class="table-footer">
      <small>A list of your recent transactions.</small>
    </div>
  </div>
</template>

<script setup>
const props = defineProps({
  transactions: {
    type: Array,
    default: () => []
  }
})

const formatDate = (dateString) => {
  return new Date(dateString).toLocaleDateString('en-US', {
    day: '2-digit',
    month: '2-digit',
    year: 'numeric'
  })
}
</script>
