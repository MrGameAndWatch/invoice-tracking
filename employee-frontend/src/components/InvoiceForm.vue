<template>
<div id="invoice-form">
    <form @submit.prevent="handleSubmit">
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

        <label for="description">Description:</label>
        <input
            v-model="invoice.description"
            type="text"
            id="description"
            name="description"
            :class="{ 'has-error': submitting && invalidDescription }"
            @focus="clearStatus"
        />

        <label for="amount">Amount:</label>
        <input 
            v-model="invoice.amount"
            type="number"
            id="amount"
            name="amount"
            :class="{ 'has-error': submitting && invalidAmount }"
            @focus="clearStatus"
        />

        <p v-if="error && submitting" class="error-message">
            ❗Please fill out all required fields
        </p>
        <p v-if="success" class="success-message">
            ✅ Invoice successfully added
        </p>

        <button>Add Invoice</button>
    </form>
</div>
</template>

<script>
    export default {
        name: 'invoice-form',
        data() {
            return {
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

                this.invoice = {
                    user: '',
                    description: '',
                    amount: 0.0
                }
                this.error = false
                this.success = true
                this.submitting = false
                console.log('Submitted', this.invoice)
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
    [class*='-message'] {
        font-weight: 500;
    }

    .error-message {
        color: #d33c40;
    }

    .success-message {
        color: #32a95d;
    }
</style>
