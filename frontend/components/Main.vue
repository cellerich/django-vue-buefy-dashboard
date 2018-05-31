<template>
      <main class="column main">
        <nav class="breadcrumb is-small" aria-label="breadcrumbs">
          <ul>
            <li><a href="#">Home</a></li>
            <li class="is-active"><a href="#" aria-current="page">Dashboard</a></li>
          </ul>
        </nav>

        <div class="level">
          <div class="level-left">
            <div class="level-item">
              <div class="title has-text-primary"><i class="fa fa-tachometer"></i> Dashboard</div>
            </div>
          </div>
          <div class="level-right">
            <div class="level-item">
              <button type="button" class="button is-small">
                March 8, 2017 - April 6, 2017
              </button>
            </div>
          </div>
        </div>

        <div class="columns is-multiline">
          <div class="column">
            <div class="box notification is-primary">
              <div class="heading">Top Seller Total</div>
              <div class="title">56,950</div>
              <div class="level">
                <div class="level-item">
                  <div class="">
                    <div class="heading">Sales $</div>
                    <div class="title is-5">250K</div>
                  </div>
                </div>
                <div class="level-item">
                  <div class="">
                    <div class="heading">Overall $</div>
                    <div class="title is-5">750K</div>
                  </div>
                </div>
                <div class="level-item">
                  <div class="">
                    <div class="heading">Sales %</div>
                    <div class="title is-5">25%</div>
                  </div>
                </div>
              </div>
            </div>
          </div>
          <div class="column">
            <div class="box notification is-warning">
              <div class="heading">Revenue / Expenses</div>
              <div class="title">55% / 45%</div>
              <div class="level">
                <div class="level-item">
                  <div class="">
                    <div class="heading">Rev Prod $</div>
                    <div class="title is-5">30%</div>
                  </div>
                </div>
                <div class="level-item">
                  <div class="">
                    <div class="heading">Rev Serv $</div>
                    <div class="title is-5">25%</div>
                  </div>
                </div>
                <div class="level-item">
                  <div class="">
                    <div class="heading">Exp %</div>
                    <div class="title is-5">45%</div>
                  </div>
                </div>
              </div>
            </div>
          </div>
          <div class="column">
            <div class="box notification is-info">
              <div class="heading">Feedback Activity</div>
              <div class="title">78% &uarr;</div>
              <div class="level">
                <div class="level-item">
                  <div class="">
                    <div class="heading">Pos</div>
                    <div class="title is-5">1560</div>
                  </div>
                </div>
                <div class="level-item">
                  <div class="">
                    <div class="heading">Neg</div>
                    <div class="title is-5">368</div>
                  </div>
                </div>
                <div class="level-item">
                  <div class="">
                    <div class="heading">Pos/Neg %</div>
                    <div class="title is-5">77% / 23%</div>
                  </div>
                </div>
              </div>
            </div>
          </div>
          <div class="column">
            <div class="box notification is-danger">
              <div class="heading">Orders / Returns</div>
              <div class="title">75% / 25%</div>
              <div class="level">
                <div class="level-item">
                  <div class="">
                    <div class="heading">Orders $</div>
                    <div class="title is-5">425K</div>
                  </div>
                </div>
                <div class="level-item">
                  <div class="">
                    <div class="heading">Returns $</div>
                    <div class="title is-5">106K</div>
                  </div>
                </div>
                <div class="level-item">
                  <div class="">
                    <div class="heading">Success %</div>
                    <div class="title is-5">+ 28,5%</div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>

        <div class="columns is-multiline">
          <div class="column is-6">
            <div class="panel">
              <p class="panel-heading">
                Buefy Table
              </p>
              <div class="panel-block">
                    <DataTable></DataTable>
              </div>
            </div>
          </div>
          <div class="column is-6">
            <div class="panel">
              <p class="panel-heading">
                Some other table
              </p>
              <div class="panel-block">
                  <!-- Hier kommt dann die sortable Data Table -->
                  <DataTableSP></DataTableSP>
              </div>
            </div>
          </div>
          <div class="column is-6">
            <div class="panel">
              <p class="panel-heading">
                Chart - Line Style (Chart.js)
              </p>
              <div class="panel-block">
                <canvas id="chartLine" width="400" height="400"></canvas>
              </div>
            </div>
          </div>
          <div class="column is-6">
            <div class="panel">
              <p class="panel-heading">
                Chart - Scatter Style (Chart.js)
              </p>
              <div class="panel-block">
                <canvas id="chartScatter" width="400" height="400"></canvas>
              </div>
            </div>
          </div>
        </div>
      </main>
</template>

<script>
import DataTable from './DataTable'
import DataTableSP from './DataTableSP'

export default {
  name: 'Main',
  data () {
    return {
      msg: 'This is the Main Area'
    }
  },
  components: {
    DataTable,
    DataTableSP
  }
}    
</script>
