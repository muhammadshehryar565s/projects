<template>
    <div class="about">
      <div class="hero is-info">
        <div class="hero-body has-text-centered">
          <h1 class="title">Courses</h1>
        </div>
      </div>
  
      <div class="container mt-3">
        <div class="row">
          <div class="col-2">
            <h5>Categories</h5>
            <ul class="list-group">
              <a class="list-group-item" @click="setActiveCategory(null)" v-bind:class="{'active': !activeCategory}">All Courses</a>
              <a class="list-group-item" v-for="Categorie in Categories" :key="Categorie.id" @click="setActiveCategory(Categorie)" v-bind:class="{'active': activeCategory?.id == Categorie.id}">{{ Categorie.title }}</a>
            </ul>
          </div>
          <div class="col-10">
            <div class="row">
              <div class="card mr-2" style="width: 18rem;" v-for="course in courses" :key="course.id">
                <img class="card-img-top" :src="course.image ? course.image : '#' " alt="Card image cap">
                <div class="card-body">
                  <h5 class="card-title">{{ course.title }}</h5>
                  <p class="card-text">{{ course.short_discription }}</p>
                  <router-link :to="{name: 'course', params: {slug: course.slug}}">open</router-link>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  
  export default {
    name: 'Courses',
    data() {
      return {
        courses: [],
        Categories: [],
        activeCategory: null
      };
    },
    async mounted() {
      console.log('mounted called');
  
      await axios
        .get('courses/categorys/')
        .then(response => {
          this.Categories = response.data;
        });
      this.getCourses();
    },
    methods: {
      setActiveCategory(Categorie) {
        this.activeCategory = Categorie;
        console.log(Categorie);
        this.getCourses();
      },
  
      getCourses() {
        let url = 'courses/';
        if (this.activeCategory) {
          url += '?category_id=' + this.activeCategory.id;
        }
        axios
          .get(url)
          .then(response => {
            console.log('courses are geeet', response.data);
            this.courses = response.data;
          })
          .catch(error => {
            console.error('Error fetching courses:', error);
          });
      }
    }
  };
  </script>
  


















<!-- <template>
    <div class="about">
      <div class="hero is-info">
        <div class="hero-body has-text-centered">
          <h1 class="title">Courses</h1>
        </div>
      </div>
  
      <div class="container mt-3">
        <div class="row">
          <div class="col-2">
            <h5>Categories</h5>
            <ul class="list-group">
              <a class="list-group-item" @click="setActiveCategory(null)" v-bind="{'active':!activeCategory}">All Courses</a>
              <a class="list-group-item" v-for="Categorie in Categories" :key="Categorie.id" @click="setActiveCategory(Categorie)" v-bind:class="{'active':activeCategory?.id==Categorie.id}">{{ Categorie.title }}</a>
            </ul>
          </div>
          <div class="col-10">
            <div class="row">
              <div class="card mr-2" style="width: 18rem;" v-for="course in courses" :key="course.id">
                <img class="card-img-top" src="#" alt="Card image cap">
                <div class="card-body">
                  <h5 class="card-title">{{ course.title }}</h5>
                  <p class="card-text">{{ course.short_discription }}</p>
                  <router-link :to="{name: 'course', params: {slug: course.slug}}">open</router-link>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  
  export default {
    name: 'Courses',
    data() {
      return {
        courses: [],
        Categories: [],
        activeCategory: null
      };
    },
    async mounted() {
      console.log('mounted called');
  
      await axios
        .get('courses/categorys/')
        .then(response => {
          this.Categories = response.data;
        });
      this.getCourses()  
     
    },
    methods: {
      setActiveCategory(Categorie) {
        this.activeCategory = Categorie;
        console.log(Categorie);
        this.getCourses()
      },

      getCourses(){
        let url = 'courses/'
        if (this.activeCategory){
            console.log('courses are geeet by click',response.data);
            url += '?category_id='+ this.activeCategory.id
        }
    axios
        .get(url)
        .then(response => {
          console.log('courses are geeet',response.data);
          this.courses = response.data;
        });
    }
    }

  }
  </script>
   -->
