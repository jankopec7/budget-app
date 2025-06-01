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

// Import components
import DashboardNavbar from '@/components/dashboard/DashboardNavbar.vue'
import SummaryCards from '@/components/dashboard/SummaryCard.vue'
import TransactionForm from '@/components/dashboard/AddTransactionForm.vue'
import RecentTransactions from '@/components/dashboard/RecentTransactions.vue'
import FinancialInsights from '@/components/dashboard/FinancialInsights.vue'


const router = useRouter()

// User data
const userEmail = ref('')
const userInitials = computed(() => {
  return userEmail.value.charAt(0).toUpperCase()
})

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

const sampleTransactions = [
  { id: 1, date: '2024-01-15', description: 'Groceries', category: 'Food & Dining', type: 'expense', amount: -75.30 },
  { id: 2, date: '2024-01-14', description: 'Salary', category: 'Salary', type: 'income', amount: 3500.00 },
  { id: 3, date: '2024-01-13', description: 'Gasoline', category: 'Transportation', type: 'expense', amount: -45.00 },
  { id: 4, date: '2024-01-12', description: 'Dinner', category: 'Food & Dining', type: 'expense', amount: -89.50 },
  { id: 5, date: '2024-01-10', description: 'Freelance Payment', category: 'Freelance', type: 'income', amount: 800.00 }
]

// Computed
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

// Charts
const monthlyData = ref([
  { month: 'Jan', income: 4000, expenses: 2800 },
  { month: 'Feb', income: 3200, expenses: 2400 },
  { month: 'Mar', income: 2800, expenses: 3200 },
  { month: 'Apr', income: 3600, expenses: 2600 },
  { month: 'May', income: 2400, expenses: 2800 },
  { month: 'Jun', income: 3800, expenses: 2200 },
  { month: 'Jul', income: 4200, expenses: 3000 }
])

const expenseCategories = ref([
  { name: 'Food', percentage: 35, color: '#2d6a4f' },
  { name: 'Shopping', percentage: 25, color: '#52b788' },
  { name: 'Transport', percentage: 20, color: '#74c69d' },
  { name: 'Bills', percentage: 12, color: '#95d5b2' },
  { name: 'Other', percentage: 8, color: '#b7e4c7' }
])

// Methods
const addTransaction = () => {
  const transaction = {
    id: Date.now(),
    ...newTransaction.value,
    amount: newTransaction.value.type === 'income'
      ? Math.abs(newTransaction.value.amount)
      : -Math.abs(newTransaction.value.amount)
  }

  transactions.value.push(transaction)

  newTransaction.value = {
    type: 'expense',
    description: '',
    amount: 0,
    category: '',
    date: new Date().toISOString().split('T')[0]
  }
}

const formatDate = (dateString) => {
  return new Date(dateString).toLocaleDateString('en-US', {
    day: '2-digit',
    month: '2-digit',
    year: 'numeric'
  })
}

const handleLogout = () => {
  localStorage.removeItem('user')
  sessionStorage.removeItem('user')
  router.push('/')
}

// Mount logic
onMounted(() => {
  const storedUser = JSON.parse(localStorage.getItem('user'))
  if (storedUser?.email) {
    userEmail.value = storedUser.email
  }

  transactions.value = [...sampleTransactions]
})

onUnmounted(() => {
  window.removeEventListener('scroll', () => {})
})
</script>
