<template>
  <div>
    <!-- Navigation Bar -->
    <DashboardNavbar
      :userEmail="userEmail"
      :userInitials="userInitials"
      @logout="handleLogout"
    />

    <div class="dashboard-page">
      <!-- Header -->
      <div class="dashboard-header">
        <h1>Dashboard</h1>
        <p>Welcome to your FinTracker financial overview.</p>
      </div>

      <!-- Summary Cards -->
      <SummaryCards :totalIncome="totalIncome" :totalExpenses="totalExpenses" :netBalance="netBalance" />

      <!-- Main Content Grid -->
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

      <!-- Financial Insights -->
      <FinancialInsights
        :monthlyData="monthlyData"
        :expenseCategories="expenseCategories"
      />
    </div>
  </div>
</template>

<script setup>
import { ref, computed, onMounted, onUnmounted } from 'vue'
import { useRouter } from 'vue-router'
import DashboardNavbar from '@/components/dashboard/DashboardNavbar.vue'
import SummaryCards from '@/components/dashboard/SummaryCard.vue'
import TransactionForm from '@/components/dashboard/AddTransactionForm.vue'
import RecentTransactions from '@/components/dashboard/RecentTransactions.vue'
import FinancialInsights from '@/components/dashboard/FinancialInsights.vue'

const router = useRouter()

const userEmail = ref('')
const userInitials = computed(() => userEmail.value.charAt(0).toUpperCase())

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

const totalIncome = computed(() =>
  transactions.value.filter(t => t.type === 'income')
    .reduce((sum, t) => sum + Math.abs(t.amount), 0)
)

const totalExpenses = computed(() =>
  transactions.value.filter(t => t.type === 'expense')
    .reduce((sum, t) => sum + Math.abs(t.amount), 0)
)

const netBalance = computed(() => totalIncome.value - totalExpenses.value)

const recentTransactions = computed(() =>
  [...transactions.value].sort((a, b) => new Date(b.date) - new Date(a.date)).slice(0, 5)
)

const monthlyData = ref([]) // TODO: można dodać generowanie z transakcji
const expenseCategories = ref([]) // jw.

const addTransaction = async () => {
  try {
    const token = localStorage.getItem('token')
    const payload = {
      amount: Math.abs(newTransaction.value.amount) * (newTransaction.value.type === 'expense' ? -1 : 1),
      category: newTransaction.value.category,
      description: newTransaction.value.description,
      date: newTransaction.value.date
    }

    const res = await fetch('/api/transactions', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'Authorization': `Bearer ${token}`
      },
      body: JSON.stringify(payload)
    })

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
      const err = await res.json()
      alert(err.message || 'Failed to add transaction')
    }
  } catch (err) {
    console.error(err)
  }
}

const fetchTransactions = async () => {
  try {
    const token = localStorage.getItem('token')
    const res = await fetch('/api/transactions', {
      headers: { 'Authorization': `Bearer ${token}` }
    })
    const data = await res.json()
    if (res.ok) transactions.value = data
    else throw new Error(data.message || 'Failed to fetch transactions')
  } catch (err) {
    console.error('Fetch error:', err)
  }
}

const formatDate = (dateString) => {
  return new Date(dateString).toLocaleDateString('en-US', {
    day: '2-digit', month: '2-digit', year: 'numeric'
  })
}

const handleLogout = () => {
  localStorage.removeItem('token')
  localStorage.removeItem('user')
  sessionStorage.removeItem('user')
  router.push({ path: '/' }) // przekierowanie na HomeView
}

onMounted(async () => {
  const storedUser = JSON.parse(localStorage.getItem('user'))
  if (storedUser?.email) userEmail.value = storedUser.email

  await fetchTransactions()
})

onUnmounted(() => {
  window.removeEventListener('scroll', () => {})
})
</script>

