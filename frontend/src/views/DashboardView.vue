<template>
  <div>
    <DashboardNavbar
      :userEmail="userEmail"
      :userInitials="userInitials"
      @logout="handleLogout"
    />

    <div class="dashboard-page">
      <div class="dashboard-header">
        <h1>Dashboard</h1>
        <p>Welcome to your FinTracker financial overview.</p>
      </div>

      <SummaryCards
        :totalIncome="totalIncome"
        :totalExpenses="totalExpenses"
        :netBalance="netBalance"
        :incomeChange="incomeChange"
        :expensesChange="expensesChange"
        :netChange="netBalanceChange"
      />

      <div class="dashboard-grid">
        <TransactionForm
          :newTransaction="newTransaction"
          :categories="categories"
          @submit="addTransaction"
        />

        <RecentTransactions
          :transactions="recentTransactions"
          :formatDate="formatDate"
        />
      </div>

      <FinancialInsights
        :monthlyData="monthlyData"
        :expenseCategories="expenseCategories"
      />
    </div>
  </div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue'
import { useRouter } from 'vue-router'

import DashboardNavbar from '@/components/dashboard/DashboardNavbar.vue'
import SummaryCards from '@/components/dashboard/SummaryCard.vue'
import TransactionForm from '@/components/dashboard/TransactionForm.vue'
import RecentTransactions from '@/components/dashboard/RecentTransactions.vue'
import FinancialInsights from '@/components/dashboard/FinancialInsights.vue'

// Router + user data
const router = useRouter()
const userEmail = ref('')
const userInitials = computed(() => userEmail.value.charAt(0).toUpperCase())

// Transactions
const transactions = ref([])

const newTransaction = ref({
  type: 'expense',
  description: '',
  amount: 0,
  category: '',
  date: new Date().toISOString().split('T')[0]
})

const categories = ref([
  'Food & Dining', 'Transportation', 'Shopping', 'Entertainment',
  'Bills & Utilities', 'Healthcare', 'Education', 'Travel',
  'Investment', 'Salary', 'Freelance', 'Other'
])

const formatDate = (dateString) => {
  return new Date(dateString).toLocaleDateString('en-US', {
    day: '2-digit', month: '2-digit', year: 'numeric'
  })
}

// Summary stats
const totalIncome = computed(() =>
  transactions.value
    .filter(t => t.type === 'income')
    .reduce((sum, t) => sum + t.amount, 0)
)

const totalExpenses = computed(() =>
  transactions.value
    .filter(t => t.type === 'expense')
    .reduce((sum, t) => sum + t.amount, 0)
)

const netBalance = computed(() => totalIncome.value - totalExpenses.value)

const recentTransactions = computed(() =>
  [...transactions.value]
    .sort((a, b) => new Date(b.date) - new Date(a.date))
    .slice(0, 5)
)

const monthlyData = computed(() => {
  const months = Array.from({ length: 12 }, (_, i) => ({
    month: new Date(0, i).toLocaleString('default', { month: 'short' }),
    income: 0,
    expenses: 0
  }))

  transactions.value.forEach(t => {
    const monthIndex = new Date(t.date).getMonth()
    if (t.type === 'income') {
      months[monthIndex].income += t.amount
    } else {
      months[monthIndex].expenses += t.amount
    }
  })

  return months
})

const expenseCategories = computed(() => {
  const expenses = transactions.value.filter(t => t.type === 'expense')
  const total = expenses.reduce((sum, t) => sum + t.amount, 0)
  const map = {}

  expenses.forEach(t => {
    map[t.category] = (map[t.category] || 0) + t.amount
  })

  return Object.entries(map).map(([name, amount]) => ({
    name,
    percentage: total > 0 ? Math.round((amount / total) * 100) : 0,
    color: generateColor(name)
  }))
})

function generateColor(str) {
  let hash = 0
  for (let i = 0; i < str.length; i++) {
    hash = str.charCodeAt(i) + ((hash << 5) - hash)
  }
  const hue = hash % 360
  return `hsl(${hue}, 60%, 60%)`
}

const currentMonthIndex = new Date().getMonth()
const lastMonthIndex = currentMonthIndex === 0 ? 11 : currentMonthIndex - 1

const currentMonth = computed(() => monthlyData.value[currentMonthIndex])
const previousMonth = computed(() => monthlyData.value[lastMonthIndex])

const incomeChange = computed(() => {
  const prev = previousMonth.value.income
  return prev === 0 ? 0 : ((currentMonth.value.income - prev) / prev) * 100
})

const expensesChange = computed(() => {
  const prev = previousMonth.value.expenses
  return prev === 0 ? 0 : ((currentMonth.value.expenses - prev) / prev) * 100
})

const netBalanceChange = computed(() => {
  const curr = currentMonth.value.income - currentMonth.value.expenses
  const prev = previousMonth.value.income - previousMonth.value.expenses
  return prev === 0 ? 0 : ((curr - prev) / prev) * 100
})

// Fetch from backend
const fetchTransactions = async () => {
  const token = localStorage.getItem('token')
  const res = await fetch('/api/transactions', {
    headers: {
      Authorization: `Bearer ${token}`
    }
  })

  const data = await res.json()
  if (res.ok) {
    transactions.value = data.map(t => ({
      ...t,
      amount: parseFloat(t.amount)
    }))
  } else {
    console.error('Error fetching transactions:', data)
  }
}

// 🔧 Zaktualizowana funkcja — przyjmuje `transaction`
const addTransaction = async (transaction) => {
  const token = localStorage.getItem('token')
  const payload = {
    type: transaction.type,
    amount: parseFloat(transaction.amount),
    category: transaction.category,
    description: transaction.description,
    date: transaction.date
  }

  const res = await fetch('/api/transactions', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      Authorization: `Bearer ${token}`
    },
    body: JSON.stringify(payload)
  })

  const result = await res.json()
  if (res.ok) {
    await fetchTransactions()
    newTransaction.value = {
      type: 'expense',
      description: '',
      amount: 0,
      category: '',
      date: new Date().toISOString().split('T')[0]
    }
  } else {
    alert(result.error || result.message || 'Failed to add transaction.')
  }
}

const handleLogout = () => {
  localStorage.removeItem('token')
  localStorage.removeItem('user')
  router.push('/')
}

onMounted(async () => {
  const storedUser = JSON.parse(localStorage.getItem('user'))
  if (storedUser?.email) userEmail.value = storedUser.email
  await fetchTransactions()
})
</script>
