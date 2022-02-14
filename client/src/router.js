import VueRouter from 'vue-router';
import Home from './pages/Home.vue';
import Items from './pages/Items.vue';
import ItemView from './pages/ItemView.vue';
import Login from './pages/Login.vue';
import SignUp from './pages/SignUp.vue';
import Profile from './pages/Profile.vue';
import AddItem from './components/AddItem.vue';
import UpdateItem from './components/UpdateItem.vue';

const routes = [
  { path: '/', component: Home, name: 'Home' },
  { path: '/items', component: Items, name: 'Items' },
  { path: '/items/:item_id', component: ItemView, name: 'ItemView' },
  { path: '/additem', component: AddItem, name: 'AddItem' },
  { path: '/updateitem/:item_id', component: UpdateItem, name: 'UpdateItem' },
  { path: '/users/:email', component: Profile, name: 'Profile' },
  { path: '/login', component: Login, name: 'Login' },
  { path: '/signup', component: SignUp, name: 'SignUp' }
];
export default new VueRouter({
  routes,
  mode: 'history'
});
