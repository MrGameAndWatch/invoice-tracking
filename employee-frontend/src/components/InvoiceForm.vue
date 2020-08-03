<template>
<ValidationObserver ref="observer" v-slot="{ invalid }">
  <form @submit.prevent="handleSubmit" class="form-container">
    <Header v-bind:title="formTitle" />
    <ValidationProvider rules="required|valid_user_id" v-slot="{ errors }">
      <b-field
        label="User ID"
        :type="errors.length > 0 ? 'is-danger' : ''"
				:message="errors.length > 0 ? errors[0] : ''"
      >
        <b-input type="text" name="user" v-model="invoice.user" />
      </b-field>
    </ValidationProvider>

    <ValidationProvider rules="required" v-slot="{ errors }">
      <b-field
        label="Description"
        :type="errors.length > 0 ? 'is-danger' : ''"
        :message="errors.length > 0 ? 'Description is required' : ''"
      >
        <b-input type="text" name="description" v-model="invoice.description" />
      </b-field>
    </ValidationProvider>

    <ValidationProvider rules="required|is_money_decimal|is_positive_monetary_amount" v-slot="{ errors }">
      <b-field
        label="Amount"
        :type="errors.length > 0 ? 'is-danger' : ''"
        :message="errors.length > 0 ? errors[0] : ''"
      >
        <b-input type="text" name="amount" v-model="invoice.amount" />
      </b-field>
    </ValidationProvider>

    <div class="form-footer">
      <b-button type="is-info" :disabled="invalid" @click="handleSubmit">
        Add
      </b-button>
    </div>
  </form>
</ValidationObserver>
</template>

<script>
  import axios from 'axios';
  import Header from './common/Header.vue'

  export default {
    name: 'InvoiceForm',
    components: {
      Header
    },
    data() {
      return {
        formTitle: "Add Invoice",
        invoice: {
          user: '',
          description: '',
          amount: 0.0
        }
      }
    },

    methods: {
      handleSubmit() {
        axios.post(`http://localhost:5000/users/${this.invoice.user}/invoices`, {
          description: this.invoice.description,
          amount: Number(this.invoice.amount)
        })
        .then((response) => {
          console.log(response)
          this.$buefy.toast.open({
            message: 'Invoice has been stored successfully!',
            position: 'is-top-right',
            type: 'is-success'
          })
        }, (error) => {
          this.$buefy.toast.open({
            duration: 5000,
            message: `An error occurred while trying to store the invoice: ${error}`,
            position: 'is-top-right',
            type: 'is-danger'
          })
        })

        this.invoice = {
          user: '',
          description: '',
          amount: 0.0
        }
      },
    }
  }
</script>

<style scoped>
  .form-container {
    max-width: 60%;
    margin-left: auto;
    margin-right: auto;
  }

  .form-footer {
    margin-top: 10px;
  }
</style>
