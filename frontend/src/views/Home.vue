<template>
  <div class="home">
    <p>Content</p>
    <div>
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
      content: "Loading..."
    }
  },
  methods: {
    getContent () {
      const path = `${process.env.VUE_APP_BACKEND_ORIGIN}/api/index.md`
      axios.get(path)
        .then(response => {
          this.content = response.data.content
        })
        .catch(() => {
          this.content = "Error..."
        })
    }
  },
  created () {
    this.getContent()
  }
}
</script>
