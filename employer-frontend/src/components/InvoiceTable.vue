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

    <InvoiceSummarizer v-bind:invoices="invoices" />
  </section>
</template>

<script>
import axios from 'axios';
import InvoiceSummarizer from './InvoiceSummarizer.vue'

export default {
  name: 'InvoiceTable',
  components: {
    InvoiceSummarizer
  },
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
          label: 'Amount in €'
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
  max-width: 1000px;
  margin-left: auto;
  margin-right: auto;
}
</style>
