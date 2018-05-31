<template>
    <aside class="column is-2 aside">
    <nav class="menu">
        <p class="menu-label">General</p>
        <ul class="menu-list">
        <li><a class="is-active" href="#"><span class="icon is-small"><i class="fa fa-tachometer"></i></span>  Dashboard</a></li>
        </ul>


        <p class="menu-label">Portfolio Data</p>
        <ul class="menu-list">
        <li><a href="#"><span class="icon is-small"><i class="fa fa-pencil-square-o"></i></span>  Exchanges</a></li>
        <li><a href="#"><span class="icon is-small"><i class="fa fa-desktop"></i></span>  Wallets</a></li>
        <li><a href="#"><span class="icon is-small"><i class="fa fa-table"></i></span>  Coins</a></li>
        </ul>


        <p class="menu-label">Administration</p>
        <ul class="menu-list">
        <li><a><span class="icon is-small"><i class="fa fa-bug"></i></span>  Exchanges</a></li>
        <li><a><span class="icon is-small"><i class="fa fa-windows"></i></span>  Wallets</a></li>
        <li><a><span class="icon is-small"><i class="fa fa-laptop"></i></span>  Coins</a></li>
        <li>
            <a class=""><i class="fa fa-cog"></i>  User Administration</a>
            <ul>
            <li><a>Member List</a></li>
            <li><a>Add a member</a></li>
            </ul>
        </li>

        </ul>
    </nav>
    </aside>
</template>

<script>
export default {
  name: "Sidebar",
  data() {
    return {
      msg: "This is the sidebar"
    };
  }
};
</script>

<style scoped>

.aside {
  background: #2e363f;
  padding: 2em 0.2em 0 1em;
}
.aside a {
  color: #afb8c3;
}
.aside .menu-list li {
  margin-top: 0.5em;
}

</style>


