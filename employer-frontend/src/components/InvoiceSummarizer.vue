<template>
  <section class="summarizer-container">
    <h3 class="subtitle">Summarize Payments In Period</h3>
    <b-field label="Start Date">
      <b-datepicker
        v-model="summaryStartDate"
      />
    </b-field>

    <b-field label="End Date">
      <b-datepicker
        v-model="summaryEndDate"
      />
    </b-field>

    <div class="centered">
      <table class="table">
        <thead>
          <tr>
            <th>User ID</th>
            <th>Refund in €</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="refund in invoiceSummary" v-bind:key="refund.userId">
            <td>{{ refund.userId }}</td>
            <td>{{ refund.refundSum }}</td>
          </tr>
        </tbody>
      </table>
    </div>
  </section>
</template>

<script>
import _ from 'lodash'
import moment from 'moment'

export default {
  name: 'InvoiceSummarizer',
  props: {
    invoices: {
      type: Array
    }
  },
  data() {
    const today = new Date()

    return {
      summaryStartDate: new Date(today.getFullYear(), today.getMonth(), today.getDate() - 30),
      summaryEndDate: new Date(),
    }
  },
  computed: {
    invoiceSummary: function() {
      const groupedByUser = _.groupBy(
        getInvoicesInDateRange(this.invoices, this.summaryStartDate, this.summaryEndDate),
        invoice => invoice.userId
      )

      const summary = []
      for (const [userId, invoices] of Object.entries(groupedByUser)) {
        const refundSum = invoices
          .map(invoice => invoice.amount)
          .reduce((a, b) => a + b, 0)
        summary.push({ userId: userId, refundSum: refundSum })
      }
      return summary

      function getInvoicesInDateRange(invoices, startDate, endDate) {
        return invoices.filter(invoice => {
          const date = moment(invoice.timestamp, 'DD/MM/YYYY HH:mm:ss').toDate()
          return date >= startDate && date <= endDate 
        })
      }
    }
  }
}
</script>

<style scoped>
  .summarizer-container {
    height: auto;
    margin-top: 50px;
    min-height: 600px;
    min-width: 600px;
  }

  .centered {
    display: flex;
    align-items: center;
    justify-content: center;
  }
</style>
