<template>
  <div id="app">
      <Navbar></Navbar>
      <div class="columns">

        <Sidebar></Sidebar>
        <Main></Main>
      </div>
  </div>
</template>

<script>
import Navbar from './components/Navbar'
import Sidebar from './components/Sidebar'
import Main from './components/Main'
import DataTable from './components/DataTable'
import DataTableSP from './components/DataTableSP'


export default {
  name: 'app',
  components: {
    Navbar,
    Sidebar,
    Main
  }
}
</script>

<style lang="scss">
  // Import Bulma's core
  @import "~bulma/sass/utilities/_all";

  // Set your colors
  $primary: #116466;
  $primary-invert: findColorInvert($primary);
  $twitter: #ffcb9a;
  $twitter-invert: findColorInvert($twitter);
  $danger: #ff652f;
  $danger-invert: findColorInvert($danger);

  // Setup $colors to use as bulma classes (e.g. 'is-twitter')
  $colors: (
      "white": ($white, $black),
      "black": ($black, $white),
      "light": ($light, $light-invert),
      "dark": ($dark, $dark-invert),
      "primary": ($primary, $primary-invert),
      "info": ($info, $info-invert),
      "success": ($success, $success-invert),
      "warning": ($warning, $warning-invert),
      "danger": ($danger, $danger-invert),
      "twitter": ($twitter, $twitter-invert)
  );

  // Links
  $link: $primary;
  $link-invert: $primary-invert;
  $link-focus-border: $primary;

  // Import Bulma and Buefy styles
  @import "~bulma";
  @import "~buefy/src/scss/buefy";
</style>

<style>
.breadcrumb:not(:last-child) {
  margin-bottom: 0;
}
.main {
  padding: 2em 1em 0;
}
.menu-label {
  color: #00d1b2;
  margin-left: 0.5em;
}
.block {
  margin-top: 0.5em;
}
/*# sourceMappingURL=main.css.map*/
</style>