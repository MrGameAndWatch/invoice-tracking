<template>
  <section class="table-container">
    <h1 class="title">All Invoices</h1>
    <b-table
      :data="invoices"
      :columns="columns"
    >
    </b-table>
    
    <template v-if="loading">
      <b-loading :is-full-page="true" :active.sync="loading" :can-cancel="false" />
    </template>
  </section>
</template>

<script>
import axios from 'axios';
export default {
  name: 'InvoiceTable',
  data() {
    return {
      loading: false,
      invoices: [],
      columns: [
        {
          field: 'userId',
          label: 'User ID'
        },
        {
          field: 'amount',
          label: 'Amount'
        },
        {
          field: 'timestamp',
          label: 'Date'
        }
      ]
    }
  },

  created() {
    this.getInvoicesFromInvoiceService()
  },

  methods: {
    getInvoicesFromInvoiceService() {
      this.loading = true
      axios.get(`http://localhost:5000/invoices`)
      .then(response => {
        this.loading = false
        this.invoices = response.data
      })
      .catch(error => {
        this.loading = false
        this.$buefy.toast.open({
          duration: 5000,
          message: `An error occurred while loading the invoices: ${error}`,
          position: 'is-top-right',
          type: 'is-danger'
        })
      })
    }
  }
}
</script>

<style scoped>
.table-container {
  margin-top: 50px;
  max-width: 600px;
  margin-left: auto;
  margin-right: auto;
}
</style>