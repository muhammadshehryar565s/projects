
 <template>
    <div class="about">
        <div class="hero is-info">
            <div class="hero-body has-text-centered">
                <h1 class="title">{{ course.title }}</h1>
            </div>
        </div>

        <div class="container mt-3">
            <div class="row">
                <div class="col-2">
                    <h5>Course Details</h5>

                    <ul>
                        <li v-for="myless in lesson" :key="myless.id">
                            <a @click="activefunction(myless)">{{ myless.title }}</a>
                        </li>
                    </ul>
                </div>
                <div class="col-10">
                    <template v-if="$store.state.user.isAuthenticated">
                        <template v-if="activelesson">

                            <template v-if="activelesson.lesson_type === 'quiz'">
                                <div v-for="quiz in quizs" :key="quiz.id">
                                    <h3>{{ quiz.question }}</h3>

                                    <div class="form-check">
                                        <input class="form-check-input" type="radio" name="flexRadioDefault"
                                            id="flexRadioDefault1" v-model="selectAnswer" :value="quiz.op1">
                                        <label class="form-check-label" for="flexRadioDefault1">
                                            {{ quiz.op1 }}
                                        </label>
                                    </div>
                                    <div class="form-check">
                                        <input class="form-check-input" type="radio" name="flexRadioDefault"
                                            id="flexRadioDefault2" v-model="selectAnswer" :value="quiz.op2">
                                        <label class="form-check-label" for="flexRadioDefault2">
                                            {{ quiz.op2 }}
                                        </label>
                                    </div>
                                    <div class="form-check">
                                        <input class="form-check-input" type="radio" name="flexRadioDefault"
                                            id="flexRadioDefault3" v-model="selectAnswer" :value="quiz.op3">
                                        <label class="form-check-label" for="flexRadioDefault3">
                                            {{ quiz.op3 }}
                                        </label>
                                    </div>
                                    <br>

                                    <template v-if="selectAnswer !== null">
                                        <template v-if="selectAnswer === quiz.answer">
                                            <div class="alert alert-success" role="alert">
                                                Correct Answer
                                            </div>
                                        </template>
                                        <template v-else>
                                            <div class="alert alert-dark" role="alert">
                                                Wrong Answer
                                            </div>
                                        </template>
                                    </template>
                                </div>
                            </template>

                         

                            <template v-if="activelesson.lesson_type === 'vedio'">

                                <div class="embed-responsive embed-responsive-16by9">
                                    <iframe :src="'https://www.youtube.com/embed/' + activelesson.vedio_id" width="100%" height="400"
                                        frameborder="0"
                                        allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture;"
                                        allowfullscreen></iframe>
                                </div>
                            </template>  








                            <template v-else>
                                {{ activelesson.long_discription }}
                            </template>
                        </template>
                        <template v-else>
                            {{ course.long_discription }}
                        </template>
                    </template>
                    <template v-else>
                        <h4>You have to create an account to access the course</h4>
                    </template>

                    <br><br><br><br>

                    <!-- Comments section -->
                    <h3>Comments</h3>
                    <div class="card mb-4">
                        <div class="card-body">
                            <p>Type your note, and hit enter to add it</p>

                            <div class="d-flex justify-content-between">
                                <div class="d-flex flex-row align-items-center">
                                    <!-- ... (rest of your comments section) -->
                                    <p class="small mb-0 ms-2">Mary Kate</p>
                                </div>
                            </div>
                        </div>
                    </div>

                    <template v-if="$store.state.user.isAuthenticated">
                        <form v-on:submit.prevent="submitcomment">
                            <div class="form-group">

                                <label for="name">Enter Your Name</label>
                                <input class="form-control" id="name" v-model="comments.name">
                            </div>

                            <div class="form-group">
                                <label for="exampleFormControlTextarea1">Enter Comment</label>
                                <textarea class="form-control" id="exampleFormControlTextarea1" rows="3"
                                    v-model="comments.content"></textarea>
                            </div>
                            <br>
                            <button type="submit" class="btn btn-primary">Submit</button>
                        </form>
                    </template>
                </div>
            </div>
        </div>
    </div>
</template>















<script>
import axios from 'axios';

export default {
    name: 'Course',
    data() {
        return {
            course: "",
            lesson: [],
            activelesson: null,
            activecategory: null,
            quizs: {},
            selectAnswer: null,
            comments: {
                name: '',
                content: '',
            }
        }
    },
    mounted() {
        const slug = this.$route.params.slug;

        axios
            .get(`courses/${slug}/`)
            .then(response => {
                console.log("getting same data", response.data.course);
                this.course = response.data.course;
                this.lesson = response.data.lesson;
                console.log('checking lesson type', response.data.lesson)
            })
            .catch(error => {
                console.error('Error fetching course and lesson data:', error);
            });
    },

    methods: {
        activefunction(myless) {
            console.log("active function called")
            this.activelesson = myless;
            if (myless.lesson_type === 'quiz') {
                this.get_Quiz()
            }
        },
        submitcomment() {
            console.log('submitcomment');
            axios
                .post(`courses/${this.course.slug}/${this.activelesson.slug}/get-comment/`, this.comments)
                .then(response => {
                    this.comments.name = '';
                    this.comments.content = '';
                })
                .catch(error => {
                    console.error('Error submitting comment:', error);
                });
        },
        get_Quiz() {
            axios
                .get(`courses/${this.course.slug}/${this.activelesson.slug}/get_quiz/`)
                .then(response => {
                    console.log("get quiz", response.data)
                    this.quizs = response.data
                })
                .catch(error => {
                    console.error('Error fetching quiz data:', error);
                });
        }
    }
}
</script>


















<!-- 
<script>
import axios from 'axios';

export default {
    name: 'Course',
    data() {
        return {
            course: "",
            lesson: [],
            activelesson: null,
            activecategory: null,
            quizs: {},
            selectAnswer: null,
            comments: {
                name: '',
                content: '',
            }
        }
    },
    mounted() {
        const slug = this.$route.params.slug;

        axios
            .get(`courses/${slug}/`)
            .then(response => {
                console.log("getting same data", response.data.course);
                this.course = response.data.course;
                this.lesson = response.data.lesson;
                console.log('checking lesson type', response.data.lesson)
            })
            .catch(error => {
                console.error('Error fetching course and lesson data:', error);
            });

            get_Quiz() {
        axios
            .get(`courses/${this.course.slug}/${this.activelesson.slug}/`)
            .then(response => {
                console.log("get quiz", response.data)
                this.quizs = response.data
            })
        }    
            
    },

    methods: {
        activefunction(myless) {
            console.log("active function called")
            this.activelesson = myless;
            if (myless.lesson_type === 'quiz') {
                this.get_Quiz()
            }
        },
        submitcomment() {
            console.log('submitcomment');
            axios
                .post(`courses/${this.course.slug}/${this.activelesson.slug}/get-comment/`, this.comments)
                .then(response => {
                    this.comments.name = '';
                    this.comments.content = '';
                })
                .catch(error => {
                    console.error('Error submitting comment:', error);
                });
        },
        get_Quiz() {
            axios
                .get(`courses/${this.course.slug}/${this.activelesson.slug}/get_quiz/`)
                .then(response => {
                    console.log("get quiz", response.data)
                    this.quizs = response.data
                })
        }
    }
}
</script>

 -->






















