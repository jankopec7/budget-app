<template>
  <div class="card transaction-form">
    <h2>Add New Transaction</h2>
    <p>Log your income or expenses quickly.</p>

    <form @submit.prevent="handleSubmit">
      <!-- Transaction Type -->
      <div class="form-group">
        <label>Transaction Type</label>
        <div class="radio-group">
          <label class="radio-label">
            <input type="radio" v-model="transaction.type" value="income" />
            Income
          </label>
          <label class="radio-label">
            <input type="radio" v-model="transaction.type" value="expense" />
            Expense
          </label>
        </div>
      </div>

      <!-- Description -->
      <div class="form-group">
        <label for="description">Description</label>
        <input
          type="text"
          id="description"
          v-model="transaction.description"
          placeholder="e.g. Groceries, Salary"
          required
        />
      </div>

      <!-- Amount -->
      <div class="form-group">
        <label for="amount">Amount</label>
        <input
          type="number"
          id="amount"
          v-model.number="transaction.amount"
          placeholder="0"
          step="0.01"
          min="0"
          required
        />
      </div>

      <!-- Category -->
      <div class="form-group">
        <label for="category">Category</label>
        <select v-model="transaction.category" required>
          <option value="">Select a category</option>
          <option
            v-for="category in categories"
            :key="category"
            :value="category"
          >
            {{ category }}
          </option>
        </select>
      </div>

      <!-- Date -->
      <div class="form-group">
        <label for="date">Date</label>
        <input
          type="date"
          id="date"
          v-model="transaction.date"
          required
        />
      </div>

      <button type="submit" class="primary">Add Transaction</button>
    </form>
  </div>
</template>

<script setup>
import { ref, reactive, watch } from 'vue'

const props = defineProps({
  categories: Array,
})

const emit = defineEmits(['add'])

const transaction = reactive({
  type: 'expense',
  description: '',
  amount: 0,
  category: '',
  date: new Date().toISOString().split('T')[0]
})

const handleSubmit = () => {
  const newEntry = {
    ...transaction,
    id: Date.now(),
    amount:
      transaction.type === 'income'
        ? Math.abs(transaction.amount)
        : -Math.abs(transaction.amount)
  }

  emit('add', newEntry)

  // Reset form
  transaction.type = 'expense'
  transaction.description = ''
  transaction.amount = 0
  transaction.category = ''
  transaction.date = new Date().toISOString().split('T')[0]
}
</script>
