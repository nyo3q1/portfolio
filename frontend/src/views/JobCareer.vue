<template>
  <div class="home">
    <p>職務履歴</p>
    <div v-if="isdir">
      <ul>
        <li v-for="c in content" v-bind:key="c.index">
          <a :href="`${c.path}`">{{ c.name }}</a>
        </li>
      </ul>
    </div>
    <div v-else>
      <markdown-it-vue class="md-body" :content="content" />
    </div>
  </div>
</template>

<script>
import MarkdownItVue from 'markdown-it-vue'
import 'markdown-it-vue/dist/markdown-it-vue.css'
import axios from 'axios'

export default {
  components: {
    MarkdownItVue
  },
  data () {
    return {
      isdir: false,
      content: "Loading..."
    }
  },
  methods: {
    getContent (path) {
      const url = `/api/${path}`
      axios.get(url)
        .then(response => {
          this.isdir = response.data.isdir
          this.content = response.data.content
        })
        .catch(() => {
          this.content = "Error..."
        })
    }
  },
  created () {
    const path = this.$route.params.pathMatch? this.$route.params.pathMatch: "job-career"
    this.getContent(path)
  },
  beforeRouteUpdate (to, from, next) {
    next();
  }
}
</script>
