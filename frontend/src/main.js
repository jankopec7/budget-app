import { createApp } from 'vue'
import App from './App.vue'
import './assets/styles.css'
import './assets/DashboardStyles.css'
import router from './router'

createApp(App).use(router).mount('#app')
