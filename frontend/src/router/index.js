import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import LoginView from '../views/LoginView.vue'
import RegisterView from '../views/RegisterView.vue'
import DashboardView from '../views/DashboardView.vue'

const routes = [
  { path: '/', component: HomeView },
  { path: '/login', component: LoginView, meta: { guestOnly: true } },
  { path: '/register', component: RegisterView, meta: { guestOnly: true } },
  { path: '/dashboard', component: DashboardView, meta: { requiresAuth: true } }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

router.beforeEach((to, from, next) => {
  const token = localStorage.getItem('token')

  // Jeśli trasa wymaga zalogowania, ale tokena brak
  if (to.meta.requiresAuth && !token) {
    return next('/login')
  }

  // Jeśli jesteś zalogowany i próbujesz wejść na login/register
  if (to.meta.guestOnly && token) {
    return next('/dashboard')
  }

  next()
})

export default router


