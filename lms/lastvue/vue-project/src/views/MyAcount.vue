<template>
    <div class="about">
        <div class="hero is-info">
            <div class="hero-body has-text-centered">
                <h1 class="title">Courses</h1>
            </div>
        </div>

        <button type="button" class="btn btn-danger"  @click="logout()">Logout</button>
    </div>
</template>
  
<script>
import axios from 'axios';

export default {
    name: 'Acount',


    methods: {
        async logout() {
            console.log('logout')

            await axios
              .post('token/logout/')
              .then(response => {
                console.log('Logged out')
              })
              .catch(error => {
                console.log(error)
              })

            axios.defaults.headers.common['Authorization'] = ""

            localStorage.removeItem('token')

            this.$store.commit('removeToken')

            this.$router.push('/')
        }
    }
};
</script>
