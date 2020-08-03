<template>
<div id="invoice-form">
    <form @submit.prevent="handleSubmit">
        <Header v-bind:title="formTitle" />

        <div>
            <label for="user">User:</label>
            <input
                v-model="invoice.user"
                type="text"
                id="user"
                name="user"
                :class="{ 'has-error': submitting && invalidUser }"
                @foucs="clearStatus"
                @keypress="clearStatus"
            />
            <Error 
                :style="{visibility: invalidUser ? 'visible' : 'hidden'}"
                v-bind:message="'Please enter a valid, non empty user name'" />
        </div>

        <div>
            <label for="description">Description:</label>
            <input
                v-model="invoice.description"
                type="text"
                id="description"
                name="description"
                :class="{ 'has-error': submitting && invalidDescription }"
                @focus="clearStatus"
            />
            <Error 
                :style="{visibility: invalidDescription ? 'visible' : 'hidden'}"
                v-bind:message="'Please enter a valid, non empty description'" />
        </div>

        <div>
            <label for="amount">Amount:</label>
            <input 
                v-model.number="invoice.amount"
                type="number"
                id="amount"
                name="amount"
                :class="{ 'has-error': submitting && invalidAmount }"
                @focus="clearStatus"
            />
            <Error 
                :style="{visibility: invalidAmount ? 'visible' : 'hidden'}"
                v-bind:message="'Please enter an amount greater 0.0'" />
        </div>

        <Error 
            v-if="error && submitting" 
            v-bind:message="'Please fill out all required fields'"
        />

        <Success 
            v-if="success"
            v-bind:message="'Invoice successfully added'"
        />

        <button>Add Invoice</button>
    </form>
</div>
</template>

<script>
    import axios from 'axios';

    import Header from './common/Header.vue'
    import Error from './common/Error.vue'
    import Success from './common/Success.vue'

    export default {
        name: 'invoice-form',
        components: {
            Header,
            Error,
            Success
        },
        data() {
            return {
                formTitle: "Add Invoice",
                submitting: false,
                error: false,
                success: false,
                invoice: {
                    user: '',
                    description: '',
                    amount: 0.0
                }
            }
        },
        methods: {
            handleSubmit() {
                this.submitting = true
                this.clearStatus()

                if (this.invalidUser || this.invalidDescription || this.invalidAmount) {
                    this.error = true
                    return
                }

                axios.post(`http://localhost:5000/users/${this.invoice.user}/invoices`, {
                    description: this.invoice.description,
                    amount: this.invoice.amount
                })
                .then((response) => {
                    console.log(response)
                }, (error) => {
                    console.error(error)
                })

                this.invoice = {
                    user: '',
                    description: '',
                    amount: 0.0
                }
                this.error = false
                this.success = true
                this.submitting = false
            },

            clearStatus() {
                this.success = false
                this.error = false
            }
        },
        computed: {
            invalidUser() {
                return this.invoice.user === ''
            },

            invalidDescription() {
                return this.invoice.description === ''
            },

            invalidAmount() {
                return this.invoice.amount <= 0
            }
        }
    }
</script>

<style scoped>
</style>
