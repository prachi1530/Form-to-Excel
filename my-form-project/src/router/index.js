import Vue from 'vue'
import Router from 'vue-router'
import Form from '@/components/Form'
import Formuser from '@/components/Formuser'
import Nonuser from '@/components/Nonuser'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Form',
      component: Form
    },
    {
      path: '/Formuser',
      name: 'Formuser',
      component: Formuser
    },
    {
      path: '/Nonuser',
      name: 'Nonuser',
      component: Nonuser
    }
  ]
})
