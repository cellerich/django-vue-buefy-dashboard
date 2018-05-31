<template>

    <nav class="navbar" role="navigation" aria-label="main navigation">

        <!-- ### Brand Icon or Text -->   
        <div class="navbar-brand">
            <a class="navbar-item is-size-3" href="#">
                <p>DVB - Dashboard</p>
            </a>

            <a role="button" class="navbar-burger" aria-label="menu" aria-expanded="false">
            <span aria-hidden="true"></span>
            <span aria-hidden="true"></span>
            <span aria-hidden="true"></span>
            </a>
        </div>

        <!-- ### Navbar Menu Items -->   
        <div class="navbar-menu">
            <!-- ### Navbar Menu Items on the left side-->   
            <div class="navbar-start">
                <!-- navbar items -->
            </div>

            <!-- ### Navbar Menu Items on the right side -->   
            <div class="navbar-end">
                <!-- navbar items -->

                <a class="navbar-item nav-tag">
                    <span class="icon is-small">
                    <i class="fa fa-envelope-o"></i>
                    </span>
                    <span class="tag is-danger tag-notif">9</span>
                </a>
                <div class="navbar-item has-dropdown is-hoverable">
                    <a class="navbar-link is-size-4">
                        <figure class="image is-32x32" style="margin-right:.5em;">
                            <img src="https://avatars2.githubusercontent.com/u/13665468?s=32&v=4">
                        </figure>
                        <p class="is-size-4">Cello</p>
                    </a>

                    <div class="navbar-dropdown is-right">
                        <a class="navbar-item">
                        <span class="icon is-small">
                            <i class="fa fa-user-o"></i>
                        </span>
                        Profile
                        </a>
                        <hr class="navbar-divider">
                        <a class="navbar-item">
                        <span class="icon is-small">
                            <i class="fa fa-power-off"></i>
                        </span>
                        Logout
                        </a>
                    </div>
                </div>



            </div>
        </div>
    </nav>

</template>

<script>
export default {
  name: "Navbar",
  data() {
    return {
      msg: "Navbar View"
    };
  }
};
</script>


<style scoped>
    .nav-tag {
    padding-right: 30px;
    }
    .tag-notif {
    border-radius: 50%;
    position: absolute;
    top: 5px;
    margin-left: 10px;
    }
    @media (max-width: 768px) {
    .tag-notif {
        margin-left: -2px;
    }
    }
    .navbar {
    background: #2e363f;
    }
    .navbar-item {
    background-color: #2e363f;
    color: #afb8c3 !important;
    }
    .navbar-item.is-active,
    .navbar-item:hover {
    background-color: #116466 !important;
    color: #363636 !important;
    }
    .navbar .is--brand:hover {
    background-color: #2e363f !important;
    }
    .navbar-brand-logo {
    max-height: 3rem !important;
    border-radius: 0.25em;
    padding: 0.25em;
    }
    .navbar-brand-logo,
    .navbar-dropdown .navbar-item {
    background-color: #fff;
    }
    .navbar-burger {
    background-color: #2e363f !important;
    border: 0;
    }
    .navbar-burger span {
    background-color: #00d1b2;
    }
    .navbar-link figure img {
    border-radius: 50%;
    max-height: 2em;
    }

    .navbar-link p {
        color: #D9B08C
    }
</style>