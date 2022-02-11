import VueRouter from 'vue-router';
import Home from './pages/Home.vue';
import Items from './pages/Items.vue';
import ItemView from './pages/ItemView.vue';
import Login from './pages/Login.vue';
import SignUp from './pages/SignUp.vue';

const routes = [
  { path: '/', component: Home, name: 'Home' },
  { path: '/items', component: Items, name: 'Items' },
  { path: '/items/:item_id', component: ItemView, name: 'ItemView' },
  { path: '/users/:user_id', component: Login, name: 'Login' },
  { path: '/users', component: SignUp, name: 'SignUp' }
];
export default new VueRouter({
  routes,
  mode: 'history'
});
