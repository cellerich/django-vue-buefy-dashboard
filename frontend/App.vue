<template>
  <div id="app">
        <Main></Main>
  </div>
</template>

<script>
import Main from './components/Main'
import DataTable from './components/DataTable'
import DataTableSP from './components/DataTableSP'


export default {
  name: 'app',
  components: {
    Main
  }
}
</script>


<style>
.breadcrumb:not(:last-child) {
  margin-bottom: 0;
}
.main {
  padding: 2em 1em 0;
}
/* .menu-label {
  color: #00d1b2;
  margin-left: 0.5em;
} */
.block {
  margin-top: 0.5em;
}
/*# sourceMappingURL=main.css.map*/
</style>